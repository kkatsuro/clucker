# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AddVenv.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_AddVenv(object):
    def setupUi(self, AddVenv):
        if not AddVenv.objectName():
            AddVenv.setObjectName(u"AddVenv")
        AddVenv.resize(433, 284)
        self.verticalLayout_2 = QVBoxLayout(AddVenv)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(AddVenv)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.python_version_label = QLabel(AddVenv)
        self.python_version_label.setObjectName(u"python_version_label")

        self.verticalLayout_2.addWidget(self.python_version_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.python_version_combo_box = QComboBox(AddVenv)
        self.python_version_combo_box.setObjectName(u"python_version_combo_box")

        self.horizontalLayout.addWidget(self.python_version_combo_box)

        self.filepicker_button = QPushButton(AddVenv)
        self.filepicker_button.setObjectName(u"filepicker_button")
        self.filepicker_button.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.filepicker_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.redbot_version_label = QLabel(AddVenv)
        self.redbot_version_label.setObjectName(u"redbot_version_label")

        self.verticalLayout_2.addWidget(self.redbot_version_label)

        self.redbot_version_combo_box = QComboBox(AddVenv)
        self.redbot_version_combo_box.setObjectName(u"redbot_version_combo_box")

        self.verticalLayout_2.addWidget(self.redbot_version_combo_box)

        self.dialog_buttons = QDialogButtonBox(AddVenv)
        self.dialog_buttons.setObjectName(u"dialog_buttons")
        self.dialog_buttons.setOrientation(Qt.Horizontal)
        self.dialog_buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.dialog_buttons)


        self.retranslateUi(AddVenv)
        self.dialog_buttons.accepted.connect(AddVenv.accept)
        self.dialog_buttons.rejected.connect(AddVenv.reject)

        QMetaObject.connectSlotsByName(AddVenv)
    # setupUi

    def retranslateUi(self, AddVenv):
        AddVenv.setWindowTitle(QCoreApplication.translate("AddVenv", u"Add Version", None))
        self.textBrowser.setHtml(QCoreApplication.translate("AddVenv", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Redbot isn't supported on every Python version, you can install Python 3.11 if you wan't latest Redbot, or check compability on PyPi. https://pypi.org/project/Red-DiscordBot/</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If installed Python didn't get detected, make sure it's added to PATH, or you can add it by hand.</p></body></html>", None))
        self.python_version_label.setText(QCoreApplication.translate("AddVenv", u"Python Version", None))
        self.filepicker_button.setText(QCoreApplication.translate("AddVenv", u"Browse", None))
        self.redbot_version_label.setText(QCoreApplication.translate("AddVenv", u"Redbot Version", None))
    # retranslateUi

