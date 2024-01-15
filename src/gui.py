#!/usr/bin/python3.9

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from PySide6.QtNetwork import QTcpServer


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

red = None

from MyDataclasses import BotToken, RedInstance
from data_manager import global_config, save_config, colorscheme
from helpers import combobox_clear

from AddInstance import get_add_instance_window

GRID_SPACING_SIZE = 6


# @todo: User should not connect to the same token twice, but there may be some reason for running 2 different instances on the same token - if user wants to open 2nd, but he didnt close first one yet, we should tell him its running on same token, so it might not work.

def horizontal_spacer():
    return QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

def vertical_spacer():
    return QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)


class QWidgetResize(QWidget):
    resized = Signal()
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resized.emit()

# @todo: We need to make a custom widget for this which will give us capability to put img, text and second button inside it.
class InstanceTile(QPushButton):
    def __init__(self, instance):
        super().__init__()
        self.setFixedSize(200, 200)
        self.loaded = False
        self.instance = instance

        self.reload_name()

        self.clicked.connect(self.set_loaded)
        self.clicked.connect(self.instance.open)

    def reload_name(self):
        self.setText(f'{self.instance.name} {self.instance.version}')
        self.setIcon(QIcon('img/icon-online.png' if self.loaded else 'img/icon-offline.png'))

    # @todo: this is really dumb currently
    def set_loaded(self):
        self.loaded = True
        self.reload_name()

class InstanceMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Clucker - Redbot Development Manager (name subject to change)')
        self.setWindowIcon(QIcon('img/icon.png'))

        self.resize(856, 520)
        self.setStyleSheet(colorscheme())

        self.scroll_area = QScrollArea(self)
        self.setCentralWidget(self.scroll_area)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area_qwidget = QWidgetResize()
        self.scroll_area_qwidget.resized.connect(self.layout_tiles_if_possible)
        self.scroll_area.setWidget(self.scroll_area_qwidget)
        self.main_grid = QGridLayout(self.scroll_area_qwidget)
        self.main_grid.setSpacing(GRID_SPACING_SIZE)

        # @todo: Wouldn't this be clearer if done together with loading config?
        self.tokens = { name: BotToken(name, value) for name, value in global_config['tokens'].items() }
        self.instances = [ RedInstance(**instance) for instance in global_config['instances'] ]
        self.buttons = [ InstanceTile(instance) for instance in self.instances ]
        self.sort_buttons()

        self.add_instance_dialog = None
        self.add_instance_button = QPushButton('Add new instance')
        self.add_instance_button.setFixedSize(200, 200)
        self.add_instance_button.clicked.connect(self.open_add_new_instance_dialog)

        self.tiles = 0

        # gui wrapper (launcher.py), @todo: all of the code from it should probably be in this file
        try:
            self.server = QTcpServer()
            self.server.listen(port=12748)
        except OSError:   # @todo: add normal debug statement
            print('port already in use... use config file to setup different port for your application')
            sys.exit()

        self.server.newConnection.connect(self.new_connection)

    # for gui wrapper (launcher.py)
    def new_connection(self, *args):
        self.show()
        self.raise_()
        self.activateWindow()
        client = self.server.nextPendingConnection()
        client.write(b'done!')
        client.disconnectFromHost()

    def open_add_new_instance_dialog(self):
        self.add_instance_dialog = get_add_instance_window()
        self.add_instance_dialog.newInstance.connect(self.new_instance)

    def new_instance(self, instance):
        self.instances.append(instance)
        self.buttons.append(InstanceTile(instance))
        self.sort_buttons()
        self.layout_tiles_if_possible(force=True)

    def sort_buttons(self):
        self.buttons.sort(key=lambda b: b.instance.name.lower())

    # This whole button layouting code is wrong, I should find a way to do this with core QT.
    def layout_tiles_if_possible(self, force=False):
        # @todo: Resizing (less columns) stops working when scrollbar appears. Is width measure wrong for some reason?
        tiles = self.scroll_area.viewport().size().width() // 206
        if tiles == 0:
            return

        if not force:
            if tiles == self.tiles:
                return

        self.tiles = tiles
        
        for button in self.buttons:
            self.main_grid.removeWidget(button)
        self.main_grid.removeWidget(self.add_instance_button)

        def generator():
            y = 0
            while True:
                for x in range(tiles):
                    yield y, x
                y += 1

        g = generator()

        for button in self.buttons:
            self.main_grid.addWidget(button, *next(g))

        self.main_grid.addWidget(self.add_instance_button, *next(g))

        self.main_grid.addItem(horizontal_spacer(), 0, tiles)
        self.main_grid.addItem(  vertical_spacer(), len(self.buttons)//tiles+1, 0)

    def closeEvent(self, event):
        for instance in self.instances:
            if instance.window != None:
                self.hide()
                event.ignore()
                return

        self.stop_all_instances()

    # this actually executes twice.. @todo: does it?
    def stop_all_instances(self):
        for instance in self.instances:
            if instance.process == None:
                continue
            instance.process.terminate()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InstanceMenu()
    window.show()
    app.lastWindowClosed.connect(window.stop_all_instances)
    sys.exit(app.exec()) 

