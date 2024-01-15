from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from Ui_AddInstance import Ui_AddInstance

from AddVenv import get_add_venv_window

from data_manager import global_config, save_config, colorscheme
from MyDataclasses import RedInstance
from helpers import combobox_clear

# @todo: Do we really want to use this? Maybe there's a smart way to abstract it..
window = None
# 'singleton pattern' for a window
def get_add_instance_window():
    global window
    if window == None:
        window = AddInstance()
        window.show()
    else:
        window.raise_()
        window.activateWindow()
    return window

class AddInstance(QDialog):
    newInstance = Signal(RedInstance)

    def __init__(self):
        super().__init__()
        self.ui = Ui_AddInstance()
        self.ui.setupUi(self)
        self.setStyleSheet(colorscheme())
        self.setWindowTitle('Add new instance')

        self.venv_choice = self.ui.venv_combo_box

        self.venv_choice.currentTextChanged.connect(self.update_name_version_label)

        self.update_venvs()
        self.update_tokens()

        self.accepted.connect(self.my_accept)
        self.rejected.connect(self.my_reject)

        self.ui.venv_add_button.clicked.connect(self.open_add_venv_dialog)

    def open_add_venv_dialog(self):
        self.add_venv_dialog = get_add_venv_window()
        self.add_venv_dialog.show()
        self.add_venv_dialog.newVenv.connect(self.add_venv)

    def add_venv(self, python_path, redbot_version):
        self.venv_choice.addItem(redbot_version)
        self.venv_choice.setCurrentIndex(self.venv_choice.count()-1)

    def update_tokens(self):
        combobox_clear(self.ui.token_combo_box)
        for token_name in global_config['tokens'].keys():
            self.ui.token_combo_box.addItem(token_name)

    def update_venvs(self):
        combobox_clear(self.venv_choice)
        for venv in global_config['venvs']:
            self.venv_choice.addItem(venv)

    def update_name_version_label(self, text):
        self.ui.name_label_version.setText('_' + text)


    def my_accept(self):
        name = self.ui.name_line_edit.text()
        prefix = self.ui.prefix_line_edit.text()

        # @todo: NoneType object has no attribute 'text'.
        version = self.venv_choice.currentText()
        token = self.ui.token_combo_box.currentText()

        # @todo: Verify information here, if error - show dialog with it or all data (or don't allow to make accept happen? like when you register on website and do something incorrect, it marks input place on red and tells you what you did wrong).

        instance = RedInstance(name, version, prefix, token)
        # @todo: What is better place for this, here, or in signal slot - QMainWindow gui.py?
        global_config['instances'].append(instance.as_dict())
        save_config()

        self.newInstance.emit(instance)

        global window
        window = None

    def my_reject(self):
        global window
        window = None
