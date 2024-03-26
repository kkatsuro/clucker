from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import pretty_errors

import sys
import os
import json
import time
import socket
import subprocess
import shutil
import random
import websocket

from Ui_InstanceWindow import Ui_InstanceWindow
from CogDirectoryManager import CogDirManager

from helpers import extract_cogname_from_path, get_random_available_port, combobox_clear
from data_manager import global_config, colorscheme

# @todo: It is possible we want to abstract choice combo box.

# @todo: Move to helpers, @note: this seemed to me to be very dumb apparently.
def combobox_switch_index_if_matches(combobox, data):
    for n in range(combobox.count()):
        if data in combobox.itemText(n):
            combobox.setCurrentIndex(n)
            return

class InstanceWindow(QMainWindow):
    def __init__(self, red_instance):
        super().__init__()
        self.ui = Ui_InstanceWindow()
        self.ui.setupUi(self)

        self.setStyleSheet(colorscheme())

        self.setWindowTitle(red_instance.instance_name()) # - Redbot Development Manager')

        self.red_instance = red_instance
        self.reader = red_instance.reader
        self.red = red_instance.process

        self.cog_choice = self.ui.cog_choice_combobox
        # self.instance_choice = self.ui.instance_choice_combobox

        self.cog_directories = global_config['cog-directories']
        self.last_cog_path = global_config.get('last-cog-path', 'NO-LAST-COG')

        # @todo: All the directory watcher stuff... Each window has its own separate one and we don't need it. We can have one class which deals with looking for new directories, which signals when new directory was found.
        self.reload_cog_directories()

        self.timer = QTimer()
        self.timer.timeout.connect(self.terminal_read_data)
        self.timer.start(33)
        CogDirManager.watcher.directoryChanged.connect(self.reload_cog_directories)  # @todo: verify this works

        self.cursor = self.ui.terminal.textCursor()
        self.cursor.movePosition(QTextCursor.End)
        self.cursor.insertText(self.red_instance.output)

        # @todo: Make this button inactive untill we know redbot loaded.
        self.ui.reload_cog_button.clicked.connect(self.call_reload_cog)

        self.cog_choice.activated.connect(self.cog_choice_changed)

    # @todo: I wondered if its worth it to abstract it into 'CogChoiceComboBox' later
    def reload_cog_directories(self): #, arg_from_callback=None):  # @todo: tf is arg_from_callback
        cogs_list = CogDirManager.get_cogs()
        combobox_clear(self.cog_choice)
        for cog in cogs_list:
            self.cog_choice.addItem(
                f'{extract_cogname_from_path(cog)} - {cog}'
            )

        combobox_switch_index_if_matches(self.cog_choice, self.last_cog_path)

    def cog_choice_current_path(self):
        name, path = self.cog_choice.currentText().split(' - ')
        return path

    def cog_choice_changed(self):
        self.last_cog_path = self.cog_choice_current_path()

    def call_reload_cog(self):
        self.red_instance.reload_cog(self.cog_choice_current_path())


    def terminal_read_data(self):
        try:
            data = self.reader.read()
        except TypeError:  # happens when no data
            return
        self.cursor.insertText(data)
        print(data, end='')
        self.red_instance.output += data

        # @todo: If user did scroll up to read something, ignore this.
        down = self.ui.terminal.verticalScrollBar().maximum()
        self.ui.terminal.verticalScrollBar().setValue(down)


    def log(self, message):
        self.console_main_tab.log(message)

    def closeEvent(self, event):
        self.red_instance.window = None
