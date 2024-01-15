from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from helpers import find_all_python_binaries, PythonVersion, combobox_clear
from data_manager import global_config, save_config, colorscheme

from Ui_AddVenv import Ui_AddVenv

window = None
def get_add_venv_window():
    global window
    if window == None:
        window = AddVenv()
        window.show()
    else:
        window.raise_()
        window.activateWindow()
    return window

# @todo: Maybe sort by pythons recommended version order, or change index to one which has latest redbot available.
class AddVenv(QDialog):
    newVenv = Signal(str, str)  # signals python path and venv

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.ui = Ui_AddVenv()
        self.ui.setupUi(self)

        self.setStyleSheet(colorscheme())

        self.reload_pythons()

        self.accepted.connect(self.my_accept)
        self.rejected.connect(self.my_reject)

        self.ui.python_version_combo_box.currentIndexChanged.connect(self.load_redbot_versions)

    def reload_pythons(self):
        # @todo: Should we cache this somewhere? You can notice waiting for this window, so.. We can do that, Once we add reload button for refreshing.
        self.python_versions = [ PythonVersion(path) for path in find_all_python_binaries() ]

        for py in self.python_versions:
            self.ui.python_version_combo_box.addItem(str(py))

        self.load_redbot_versions()


    # @todo: This should actually download version info from pypi, because we can't update this with every new RedBot release.
    def load_redbot_versions(self):
        combobox_clear(self.ui.redbot_version_combo_box)

        index = self.ui.python_version_combo_box.currentIndex()
        if index == -1:
            return
        version = self.python_versions[index].version

        # @todo: Version comparison; @temporary
        if version == '3.12.0':
            self.ui.redbot_version_combo_box.addItem('redbot unavaible for this python version')
            return

        if version == '3.11.5':
            self.ui.redbot_version_combo_box.addItem('3.5.5')
            return

        if version == '3.9.18':
            self.ui.redbot_version_combo_box.addItem('3.5.5')
            self.ui.redbot_version_combo_box.addItem('3.4.18')
            return

        self.ui.redbot_version_combo_box.addItem('redbot unavaible for this python version')

    def my_accept(self):
        _, python_path = self.ui.python_version_combo_box.currentText().split(' - ')
        redbot_version = self.ui.redbot_version_combo_box.currentText()

        # @todo: Check if this version is already in config, ask if want to overwrite it.
        
        if redbot_version == 'redbot unavaible for this python version':
            return

        global_config['venvs'][redbot_version] = python_path
        save_config()

        self.newVenv.emit(python_path, redbot_version)

        global window
        window = None

    def my_reject(self):
        global window
        window = None
