from PySide6.QtWidgets import QComboBox

# cause there is no such method in this class... may be kinda useless but whatever

class QComboBoxChangeIndex(QComboBox): 
    def setIndexMatch(self, text):
        self.setCurrentIndex(self.findText(text))
