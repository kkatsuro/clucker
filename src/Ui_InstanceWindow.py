# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InstanceWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_InstanceWindow(object):
    def setupUi(self, InstanceWindow):
        if not InstanceWindow.objectName():
            InstanceWindow.setObjectName(u"InstanceWindow")
        InstanceWindow.resize(1013, 713)
        InstanceWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(InstanceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.instance_info_text_browser = QTextBrowser(self.centralwidget)
        self.instance_info_text_browser.setObjectName(u"instance_info_text_browser")
        self.instance_info_text_browser.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_2.addWidget(self.instance_info_text_browser)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_2.addWidget(self.label)

        self.cog_choice_combobox = QComboBox(self.centralwidget)
        self.cog_choice_combobox.setObjectName(u"cog_choice_combobox")
        self.cog_choice_combobox.setMinimumSize(QSize(200, 0))
        self.cog_choice_combobox.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_2.addWidget(self.cog_choice_combobox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.terminal = QTextBrowser(self.centralwidget)
        self.terminal.setObjectName(u"terminal")
        self.terminal.setStyleSheet(u"font: 500 11pt \"SourceCodeVF\";")
        self.terminal.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout.addWidget(self.terminal)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.reload_cog_button = QPushButton(self.centralwidget)
        self.reload_cog_button.setObjectName(u"reload_cog_button")

        self.verticalLayout.addWidget(self.reload_cog_button)

        InstanceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(InstanceWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1013, 23))
        InstanceWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(InstanceWindow)
        self.statusbar.setObjectName(u"statusbar")
        InstanceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InstanceWindow)

        QMetaObject.connectSlotsByName(InstanceWindow)
    # setupUi

    def retranslateUi(self, InstanceWindow):
        InstanceWindow.setWindowTitle(QCoreApplication.translate("InstanceWindow", u"MainWindow", None))
        self.instance_info_text_browser.setHtml(QCoreApplication.translate("InstanceWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Instance info..</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Name: botname</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\">Prefix: $</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Token: secret</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("InstanceWindow", u"Cog", None))
        self.reload_cog_button.setText(QCoreApplication.translate("InstanceWindow", u"RELOAD", None))
    # retranslateUi

