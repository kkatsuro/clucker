# import pretty_errors

import sys
import os
import json
import time
import paramiko
import threading
import websocket

from update_directory import update_directory
from forward import Handler, ForwardServer

import signal

def segfault():
    signal.raise_signal(signal.SIGSEGV)


class ForwardThread(threading.Thread):
    def __init__(self, local_port, remote_host, remote_port, transport):
        super().__init__(name=f'ForwardThread:{local_port}->{remote_port}')

        self.local_port = local_port
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.transport = transport

        self.start()

    def run(self):
        class SubHander(Handler):
            chain_host = self.remote_host
            chain_port = self.remote_port
            ssh_transport = self.transport

        self.server = ForwardServer(("", self.local_port), SubHander)
        self.server.serve_forever()

    def cancel(self):
        self.server.shutdown()

class ConnectionThread(threading.Thread):
    def __init__(self, server_info, console_tab, loop_wait_time=1):
        print('ConnectionThread init..')
        super().__init__(name='ConnectionThread-' + server_info)
        self.server_info = server_info
        self.tasks = []
        self.loop_wait_time = loop_wait_time

        self.console = console_tab
        self.initialized = False

        self.start()  # @todo: can we do this??? also in ForwardThread

    def run(self):
        username, host = self.server_info.split('@')

        self.console.log(f'connecting to {host}@{username}...')

        # @todo: get keypath
        self.client = paramiko.client.SSHClient()
        self.client.load_system_host_keys()
        try:
            self.client.connect(host, username=username)

        # @todo: what if error happens and we return below? - make the rest of app behave correctly
        except paramiko.ssh_exception.AuthenticationException:
            self.console.log('authentication error!! try to change method from default')
            return
        except Exception as e:
            self.console.log('unknown error:')
            self.console.log(str(e))
            return

        self.console.log('connected!')

        stdin, stdout, stderr = self.client.exec_command('echo "$HOME"')
        self.home = stdout.read(4096).decode().strip()

        self.console.log(f'home directory is {self.home}')

        # start SFTP connection
        self.sftp = self.client.open_sftp()
        self.console.log(f'sftp opened')
        self.transport = self.client.get_transport()

        # @todo: start it according to current bot.. and maybe abstract into a bot class?
        self.forward_threads = []
        self.forward_threads.append(ForwardThread(6134, 'localhost', 6134, self.client.get_transport()))
        self.console.log('started forward thread')

        self.initialized = True

        self.start_main_loop()
        self.console.log('leaving thread..')


    # somehow it is a little bit clearer this way?
    def start_main_loop(self):
        # segfault()
        while True:
            if len(self.tasks) != 0:
                task = self.tasks.pop()

                try:
                    if len(task) == 1:
                        func = task[0]
                        result = func()
                    else:
                        func, args = task[0], task[1:]
                        result = func(*args)

                except Exception as e:
                    self.console.log('Error when trying to execute task in this ConnectionThread:')
                    self.console.log(e)
                    result = 0

                if result == -1:
                    self.console.log('leaving main loop function')
                    return  # why it segfaulted here?

            time.sleep(self.loop_wait_time/1000)


    def cancel(self):
        # self.tasks.insert(0, (self.finish_connection_task, ))  # @todo: is this right?
        self.tasks.append((self.finish_connection_task, ))

    def finish_connection_task(self):
        for tunnel in self.forward_threads:
            tunnel.cancel()
            tunnel.join()  # wait for it to cancel..

        # @todo: close connection
        self.console.log('closing connection..')

        # close all connections with bots here...
        # @todo: is this correct order and everything i should close?
        self.sftp.close()
        self.transport.close()
        self.client.close()
        self.console.log('closed!')

        # segfault()

        return -1

    # pass function and arguments if needed
    # example:
    # * add_task(some_function)
    # * add_task(some_function, argument_to_be_passed1, argument_to_be_passed2)
    def add_task(self, *task):
        if len(task) == 0:
            raise Exception('You have to pass at least one argument to add_task method')

        self.tasks.append(task)

    def refresh_bots(self):
        stdin, stdout, stderr = self.client.exec_command(f'ls {self.home}/.local/share/Red-DiscordBot/data/')
        bot_list = stdout.read(4096).decode().strip().split('\n')
        self.console.log(f'bots: {bot_list}')

        # for bot in bot_list:
        #     if bot not in self.config['servers'][current_server]['bots']:
        #         self.config['servers'][current_server]['bots'].append(bot)
        #         self.ui.bot_choice.addItem(bot)

        # self.save_config_file()

    # this will be a little bit complicated because...
    # https://docs.discord.red/en/stable/autostart_systemd.html
    # says you should create one unit file and then start it with `systemctl start red@instancename`
    # but what i do is unit for every file that exists.
    # i do this because documentation doesnt mention rpc
    # and each instance needs different rpc port...
    # can we still do this with one unit file? - apparently: NO
    # 
    # @todo: some things wrong with docs and redbot
    # * bad systemd unit file example - rpc, rpc ports ?
    # * no mention about starting arguments in docs, --co-owner ?
    # * shouldnt all of the starting be managed by redbot too? for example:
    #   * start all instances of redbot with one binary and use config file
    #   * start different instances with systemd but configure it with config file, not launch options

    # @todo: finish this
    def run_grep_on_units(self):
        stdin, stdout, stderr = self.client.exec_command(
            f'grep -R redbot {SYSTEM_UNIT_SEARCH_PATH} {USER_UNIT_SEARCH_PATH}'
        )
        # @todo: how to properly do reads to be sure it won't cut output??
        grep_result = stdout.read(8096).decode().strip().split('\n')

        for line in grep_result:
            if 'ExecStart' in line:
                self.console.log(line)

    # @todo:
    # * pass cog object instead, to get name and path of it, and do the same with bot
    # * move it to bot classs?
    def reload_cog(self, cog_name, cog_path, bot_name, bot_rpc_port):
        self.console.log(f'local list: {os.listdir(cog_path)}')

        remote_list = self.sftp.listdir(f'{self.home}/.local/share/Red-DiscordBot/data/{bot_name}/cogs/CogManager/cogs/')
        self.console.log(f'remote list: {remote_list}')

        # @todo: local port has to be available
        self.console.log(f'connecting to rpc ws://localhost:{bot_rpc_port}...')
        ws = websocket.create_connection(f'ws://localhost:{bot_rpc_port}')
        self.console.log('connected')

        mess = '{"jsonrpc": "2.0", "method": "CORE__RELOAD", "params": [["%s"]], "id": "%s"}' % (cog_name, "some_id")
        self.console.log('sending message: ' + mess)
        ws.send(mess)

        self.console.log('sent; receiving..')
        self.console.log('received:\n' + json.dumps(json.loads(ws.recv()), indent=4) )
        ws.close()
