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

from helpers import extract_cogname_from_path, is_cog_path, get_random_available_port, combobox_clear
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

        self.load_config()

        # ============================== MAYBE ABSTRACT THIS INTO CogChoiceComboBox LATER ===============================
        self.reload_cog_directories()
        self.watcher = QFileSystemWatcher()
        self.watcher.directoryChanged.connect(self.reload_cog_directories)
        for path in self.cog_directories:
            self.watcher.addPath(path)
        # ============================== MAYBE ABSTRACT THIS INTO CogChoiceComboBox LATER ===============================


        self.timer = QTimer()
        self.timer.timeout.connect(self.terminal_read_data)
        self.timer.start(33)

        self.cursor = self.ui.terminal.textCursor()
        self.cursor.movePosition(QTextCursor.End)
        self.cursor.insertText(self.red_instance.output)

        # @todo: Make this button inactive untill we know redbot loaded.
        self.ui.reload_cog_button.clicked.connect(self.call_reload_cog)

        self.cog_choice.activated.connect(self.cog_choice_changed)


    def load_config(self):
        self.cog_directories = global_config['cog-directories']
        self.last_cog_path = global_config.get('last-cog-path', 'NO-LAST-COG')


    # ============================== MAYBE ABSTRACT THIS INTO CogChoiceComboBox LATER ================================

    def reload_cog_directories(self, arg_from_callback=None):
        cogs_list = set()
        for directory in self.cog_directories:
            try:
                cogs_list |= { node.path for node in os.scandir(directory) if node.is_dir() and is_cog_path(node.path) }
            except Exception as e:
                print(f'error: something rong when listing {directory}')  # @debug statement
                print(e)
                continue

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

    # ============================== MAYBE ABSTRACT THIS INTO CogChoiceComboBox LATER ================================


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
