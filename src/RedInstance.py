import os
import subprocess
import shutil
import time
import websocket
import json

from dataclasses import dataclass, field
from InstanceWindow import InstanceWindow
from helpers import *

from PySide6.QtCore import QProcess, QObject, Signal

from data_manager import global_config

@dataclass
class RedCog:
    name: str
    path: str

@dataclass
class BotToken:
    name: str
    value: str

tokens={}

CO_OWNERS = [ '992441146754224128' ]

UNLOADED=0
LOADING=1
LOADED=1

class SignalBS(QObject):
    '''I am almost certain something won't work if I try to create signal for dataclass which doesn't inherit from QObject, so I created this.. But maybe we can get rid of this, @todo'''
    ready_read = Signal()

# @todo: We may want to somehow combine this with InstanceWindow, or rethink how to connect these 2, ownerships etc.
# @todo: Implement stopping.
# @todo (maybe in the future): Make it possible for user to specify port or path.
# @todo: I made it dataclass at start, but now it changed too much and I will have to rethink if it's correct. But currently, initialization won't work if I do simple changes to make it a class.
@dataclass
class RedInstance:
    """
    This stores all the information related to Redbot Instance, window and process.
    Maybe I should separate these 2 in the future, but maybe not.
    """
    name: str
    version: str
    prefix: str
    token: str

    # @todo: Maybe abstract it into red process.
    port: str = None
    window: str = None  # @todo: Change to QMainWindow type.
    process: subprocess.Popen = None
    output = ''
    loaded = False

    process_signals = []

    state = UNLOADED

    def __post_init__(self):
        self.process = QProcess()
        self.signal = SignalBS()

        self.process.readyReadStandardOutput.connect(self.process_read_forward)
        self.process.readyReadStandardError.connect(self.process_read_forward)

        self.output_stdout = ''
        self.output_stderr = ''


    def as_dict(self):
        return {
            'name': self.name,
            'version': self.version,
            'prefix': self.prefix,
            'token': self.token
        }       

    # path of venv
    def path(self):
        return f'{os.environ["HOME"]}/.local/share/clucker/redbot-{self.version}/'

    def red_path(self):
        return self.path() + 'bin/redbot'

    def instance_name(self):
        return f'{self.name}_{self.version}'

    def redbot_path(self):
        return f'{os.environ["HOME"]}/.local/share/Red-DiscordBot/data/{self.instance_name()}/'

    def cogs_path(self):
        return f'{self.redbot_path()}/cogs/CogManager/cogs/'

    # @todo: Maybe we should abstract all of this printing code to make it better defined. Currently I feel it's kinda mess with how to actually use it.
    def process_finish_connect(self, new_signal):
        '''Disconnects all previously connected signals, connects new signal and saves it.'''
        for signal in self.process_signals:
            self.process.finished.disconnect(signal)
        self.process_signals = [new_signal]  # @todo: This may make not much sense, it probably always will be 1 element at max, but for now - whatever.
        self.process.finished.connect(new_signal)

    def print(self, *args):
        self.output_stdout = ' '.join(args) + '\n'
        self.signal.ready_read.emit()

    def process_read_forward(self):
        self.output_stdout = self.process.readAllStandardOutput().toStdString()
        self.output_stderr = self.process.readAllStandardError().toStdString()
        self.signal.ready_read.emit()

    # @todo: Verify if we do all of this in right way and order.
    # @todo: what if we call this twice?
    def open(self):
        """
        Makes instance window appear. Manages starting and even installing, if instance isn't installed yet.
        """
        if self.window != None:
            self.window.raise_()
            self.window.activateWindow()
        else:
            self.window = InstanceWindow(self)
            self.window.show()

        if self.state == UNLOADED:
            self.state = LOADING
            self.load_and_stuff()

    def load_and_stuff(self):
        if not self.redbot_installed():
            self.install_process_create_venv()

        elif not self.instance_installed():
            self.install_instance()
            
        elif not self.loaded:
            self.start_process()

    # @todo: Check if all necessary packages installed?
    def redbot_installed(self):
        try:  # @standards: It may be incorrect way to check if path exists, can be found in different places too.
            with open(f'{self.path()}/bin/redbot-setup', 'r'):
                pass
            return True
        except FileNotFoundError:
            return False

    def instance_installed(self):
        try:
            with open(f'{os.environ["HOME"]}/.config/Red-DiscordBot/config.json') as f:
                conf = json.loads(f.read())

            if conf.get(self.instance_name()) == None:
                return False

            os.listdir(self.redbot_path())
            return True

        except FileNotFoundError:
            return False

    # @todo: It seems a lot of things can go wrong in this installation process, like if we stop program during it. Shouldn't we give more options for starting these functions(processes)? 3 of them were in one function earlier, but it's possible we may want to do more conditionals and start from 2nd one, or 3rd?
    def install_process_create_venv(self):
        python_path = global_config['venvs'][self.version]
        # @todo: Can be `-m venv` unavailable?
        # @todo: Venv creation is possible even if directory already exists, but it doesnt remove 'additional' files.. What do we do with that? How do we behave here if Venv already exists?
        self.print(f'Creating new Virtual Environment with {python_path} at {self.path()}')
        self.process_finish_connect(self.install_process_pip_ugrade)
        self.process.start(python_path, [ '-m', 'venv', self.path() ])

    def install_process_pip_ugrade(self):
        self.print(f'Upgrading pip and wheel packages')
        self.process_finish_connect(self.install_process_install_red)
        self.process.start(f'{self.path()}/bin/pip', ['install', '-U', 'pip', 'wheel' ])

    def install_process_install_red(self):
        self.print(f'Running pip installation of Redbot, version:', self.version)
        self.process_finish_connect(self.install_instance)
        self.process.start(f'{self.path()}/bin/pip', [
            'install', '-Iv', f'Red-DiscordBot=={self.version}'
        ])

    def install_instance(self):
        self.print('Running redbot setup for instance:', self.instance_name())
        self.process.start( f'{self.path()}/bin/redbot-setup', [
            '--no-prompt', '--instance-name', self.instance_name()
        ])
        # success - prints: Your basic configuration has been saved.
        # already exists - prints: An instance with this name already exists. 
        # @todo: Do we: check error code for this error and handle it somehow? But this shouldn't happen now.

        # @todo: make this happen
        # if process.returncode != 0:  # @debug @todo: Inform user about error.
        #     self.print('ERROR: instance with this name already exists')
        #     return
        self.process_finish_connect(self.start_process)

    def start_process(self):
        self.port = str(get_random_available_port())

        self.print('Starting Redbot instance:', self.instance_name())
        self.print('Token:', self.token)
        self.print('RPC port:', self.port)

        self.process.start(self.red_path(), [
            self.instance_name(),
            '--no-prompt',
            '--token', global_config['tokens'][self.token],  # @nocheckin
            '--prefix', self.prefix,
            '--rpc', '--rpc-port', self.port,
            '--co-owner', CO_OWNERS[0],
            # @todo: Enable/disable it from gui.
            # '--debug',
            # '--rich-traceback-show-locals',  
            # '--rich-traceback-extra-lines',
        ])

        self.loaded = True
        # @todo: This can actually fail, for example due to not all Privileged Intents enabled. We want something to be able to tell if redbot is currently working, and display that as 'running' status.


    # @todo: ModuleNotFoundError: No module named 'httpx'
    # Implement installation from setup.py but also a way to avoid this situation somehow (list all dependencies with grep-like function?). It would be great to prompt user with 'module not found, do you want to install it now?' after this happens, but we also should inform him that he should add all necessary modules to setup.py to install them aannnddd maybe (probably) we want to give a way to install all modules which were added (during development). So, we need to keep track of all imports, or setup.py file, before reloading any cog.

    # @todo: Do this in different thread because it is blocking the whole gui code..
    # @todo: Wait for execution of it untill all is initialized, is this neccessary?
    def reload_cog(self, cog_path):
        cogname = extract_cogname_from_path(cog_path)
        destination = f'{self.cogs_path()}/{cogname}'
        self.print('reloading cog:', cogname, destination)

        shutil.rmtree(destination, ignore_errors=True)
        shutil.copytree(cog_path, destination)
        
        ws = websocket.create_connection(f'ws://localhost:{self.port}')
        self.print('connected to instance')

        # @todo: Probably put it into real dictionary, although I don't really an idea of parsing it "needlessly" if I can just do this... Still, it probably is a mess to do this here.
        mess = '{"jsonrpc": "2.0", "method": "CORE__RELOAD", "params": [["%s"]], "id": "%s"}' % (cogname, "some_id")
        self.print('sending message: ' + mess)
        ws.send(mess)

        self.print('sent; receiving..')
        self.print('received:\n' + json.dumps(json.loads(ws.recv()), indent=4) )

        ws.close()


    # @todo: Do we do something with this?
    def wait_till_loaded(self):
        start = time.time()
        while True:
            try:
                ws = websocket.create_connection(f'ws://localhost:{self.port}')
                ws.close()
                print('loaded after:', time.time() - start, 'seconds')
                self.loaded = True
                return
            except ConnectionRefusedError:
                time.sleep(0.01)
