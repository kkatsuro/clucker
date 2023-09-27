#!/usr/bin/python3

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pretty_errors

import sys
import os
import json
import time
import paramiko
import threading
import websocket

from jsonrpc_websocket import Server

from update_directory import update_directory
from ConnectionThread import ConnectionThread

from main_window import Ui_MainWindow

import faulthandler
faulthandler.enable()

CONFIG_FILE = 'conf.json'

# to add as option to configure:
# ssh key - rn can use ~/.ssh/id_rsa
# ssh username and ip - can use just one line rn
# cog to send update - location

# attempt to open up a session on a server change?
# and close before opening another?

# after first connection:
# * finds every bot
# * finds every unit? (can be used to find every bot?
#   but there can be 2 units for one bot?)
#   'grep -R redbot' in every possible directory
# * finds corresponding rpc ports
# * saves everything to config file

# what if redbot isnt enabled from systemd unit?  - a way to add it manually

# inform about rpc not enabled?

# @todo:
# * edit config in app

# * reload bots for current server function

# * add connect button (server and bot?)
# * close connection and tab
# * put 3 edit buttons into one hamburger

# https://docs.discord.red/en/stable/cog_guides/cog_manager_ui.html
# ^ this is very unecessary and complicates stuff a lot :( 

# * terminal font size change

# do we...
# start connection with every bot, or do it same as with server?


# RELOAD BUTTON:
# * RPC connection
# * rsync transfer


# errors:
# opc@*some_ip* - unknown error:
# opc@*some_ip* - Server '*some_ip*' not found in known_hosts


SYSTEM_UNIT_SEARCH_PATH = '''
/etc/systemd/system.control/
/run/systemd/system.control/
/run/systemd/transient/
/run/systemd/generator.early/
/etc/systemd/system/
/etc/systemd/system.attached/
/run/systemd/system/
/run/systemd/system.attached/
/run/systemd/generator/
/usr/lib/systemd/system/
/run/systemd/generator.late/
'''.replace('\n', ' ')

USER_UNIT_SEARCH_PATH = '''
˜/.config/systemd/user.control/
$XDG_RUNTIME_DIR/systemd/user.control/
$XDG_RUNTIME_DIR/systemd/transient/
$XDG_RUNTIME_DIR/systemd/generator.early/
˜/.config/systemd/user/
$XDG_CONFIG_DIRS/systemd/user/
/etc/systemd/user/
$XDG_RUNTIME_DIR/systemd/user/
/run/systemd/user/
$XDG_RUNTIME_DIR/systemd/generator/
$XDG_DATA_HOME/systemd/user/
$XDG_DATA_DIRS/systemd/user/
/usr/lib/systemd/user/
$XDG_RUNTIME_DIR/systemd/generator.late/
'''.replace('\n', ' ')

lock = threading.Lock()


# @todo: is this good to create this?
# is it better to have self.console.add_tab('name')
# than do ConsoleTab('name', self.console_output_main) every time?
#
# well... probably?
class Console():
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        self.tabs = []

    def add_tab(self, name):
        text_browser = QTextBrowser()
        new_tab_index = self.tab_widget.addTab(text_browser, name)
        tab = ConsoleTab(name, text_browser)
        self.tabs.append(tab)

        self.tab_widget.setCurrentIndex(new_tab_index)

        return tab


class ConsoleTab():
    def __init__(self, name, text_browser):
        self.name = name
        self.text_browser = text_browser

        self.cursor = self.text_browser.textCursor()
        self.cursor.movePosition(QTextCursor.End)

    # @todo: error log - in color?
    def log(self, message):

        # @todo: move cursor to self and do this only once?
        # cursor = self.text_browser.textCursor()
        # cursor.movePosition(QTextCursor.End)
        # cursor.insertText(f'[{ time.strftime("%H:%M:%S", time.localtime()) }]: {message}\n')

        self.cursor.insertText(f'[{ time.strftime("%H:%M:%S", time.localtime()) }]: {message}\n')

        lock.acquire()
        print(self.name, '-', message, flush=True)
        lock.release()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        try:
            with open(CONFIG_FILE, 'r') as f:
                self.config = json.loads(f.read())
        except FileNotFoundError:
            self.config = {
                'cogs': {},
                'servers': {},
                'last_cog': None,
                'last_server': None,
            }

        self.connections = {}

        self.console = Console(self.ui.console_output_tab_view)
        self.console_main_tab = self.console.add_tab('rfap')

        self.load_ui_from_config()

        if self.last_server:
            server = self.last_server
        else:
            server = self.ui.server_choice.currentText()

        if server != '':
            # @todo: abstract into connect_to_a_server() or something?
            self.connections[server] = ConnectionThread(server, self.console.add_tab(server))
            # pass

        # open up a thread trying connect to a newly selected server
        # also, update bot list to relevant to current server
        self.ui.cog_choice.activated.connect(self.new_cog_chosen)
        self.ui.server_choice.activated.connect(self.new_server_chosen)
        self.ui.bot_choice.activated.connect(self.new_bot_chosen)

        self.ui.bot_reload.clicked.connect(self.reload_bots_for_current_server)
        self.ui.reload_cog_button.clicked.connect(self.reload_cog)
        
        self.log('finished initializaiton')

    def reload_bots_for_current_server(self):
        # @todo: can I always access it like this?
        conn = self.connections[self.last_server]
        conn.add_task(conn.refresh_bots)

    def reload_cog(self):
        conn = self.connections[self.last_server]

        cog_path = self.config['cogs'][self.last_cog]
        server_conf = self.config['servers'][self.last_server]
        bot_rpc_port = server_conf['bots'][server_conf['last_bot']]['rpc']

        conn.add_task(conn.reload_cog, self.last_cog, cog_path, server_conf['last_bot'], bot_rpc_port)


    # we can easily edit config and then just reaload ui
    # instead of trying to add new cogs, servers and bots to both of them
    def load_ui_from_config(self):
        self.last_cog = self.config.get('last_cog')
        self.last_server = self.config.get('last_server')

        self.ui.cog_choice.clear()
        self.ui.bot_choice.clear()
        self.ui.server_choice.clear()

        # load config to gui
        for cog in self.config['cogs']:
            self.ui.cog_choice.addItem(cog)

        for server in self.config['servers']:
            self.ui.server_choice.addItem(server)
        
        if self.last_server:
            server = self.config['servers'].get(self.last_server)
        else:
            server = self.config['servers'].get( self.ui.server_choice.currentText() )

        if server:
            for bot in server['bots']:
                self.ui.bot_choice.addItem(bot)


        # set comboBoxes indices to ones that were saved previously
        if self.last_cog and self.config['cogs'].get(self.last_cog):
            self.ui.cog_choice.setIndexMatch(self.last_cog)

        if self.last_server and self.config['servers'].get(self.last_server):
            self.ui.server_choice.setIndexMatch(self.last_server)

            last_bot = self.config['servers'][self.last_server]['last_bot']
            if last_bot and self.config['servers'][self.last_server].get(last_bot):
                self.ui.bot_choice.setIndexMatch(last_bot)


    def new_cog_chosen(self):
        self.last_cog = self.ui.cog_choice.currentText()

    def new_server_chosen(self):
        self.last_server = self.ui.server_choice.currentText()

        self.ui.bot_choice.clear()
        for bot in self.config['servers'][self.last_server]['bots']:
            self.ui.bot_choice.addItem(bot)

        last_bot = self.config['servers'][self.last_server]['last_bot']
        if last_bot:
            self.ui.bot_choice.setIndexMatch(last_bot)

        server = self.last_server
        if self.connections.get(server) == None:
            self.connections[server] = ConnectionThread(server, self.console.add_tab(server))

    def new_bot_chosen(self):
        self.config['servers'][self.last_server]['last_bot'] = self.ui.bot_choice.currentText()

    def closeEvent(self, event):
        # @todo: we have to check here first if connection is not used currently
        # then wait a while for it to finish
        # otherwise just exit
        # prints here are for debugging currently
        for connection in self.connections.values():
            for tunnel in connection.forward_threads:
                print('cancelling tunnel..', flush=True)
                tunnel.cancel()
                print(tunnel, flush=True)

            print('cancelling connection..', flush=True)
            connection.cancel()
            while connection.is_alive():
                pass
            print(connection, flush=True)

        print('cancelled everything..', flush=True)
        self.save_config_file()
        print('config file saved..', flush=True)

    def log(self, message):
        self.console_main_tab.log(message)

    def save_config_file(self):
        self.config['last_server'] = self.last_server
        self.config['last_cog'] = self.last_cog

        with open(CONFIG_FILE, 'w') as f:
            f.write(json.dumps(self.config, indent=4))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    result = app.exec()

    print('EXITTING??', flush=True)

    sys.exit(result) 
