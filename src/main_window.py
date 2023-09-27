# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from QComboBoxChangeIndex import QComboBoxChangeIndex

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 549)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.left_layout = QVBoxLayout()
        self.left_layout.setObjectName(u"left_layout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.left_layout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cog_choice = QComboBoxChangeIndex(self.centralwidget)
        self.cog_choice.setObjectName(u"cog_choice")

        self.horizontalLayout_2.addWidget(self.cog_choice)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.cog_add_new = QPushButton(self.centralwidget)
        self.cog_add_new.setObjectName(u"cog_add_new")

        self.horizontalLayout_2.addWidget(self.cog_add_new)


        self.left_layout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.left_layout.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.server_choice = QComboBoxChangeIndex(self.centralwidget)
        self.server_choice.setObjectName(u"server_choice")

        self.horizontalLayout_3.addWidget(self.server_choice)

        self.server_edit_button = QPushButton(self.centralwidget)
        self.server_edit_button.setObjectName(u"server_edit_button")

        self.horizontalLayout_3.addWidget(self.server_edit_button)

        self.server_add_new = QPushButton(self.centralwidget)
        self.server_add_new.setObjectName(u"server_add_new")

        self.horizontalLayout_3.addWidget(self.server_add_new)

        self.server_remove_button = QPushButton(self.centralwidget)
        self.server_remove_button.setObjectName(u"server_remove_button")

        self.horizontalLayout_3.addWidget(self.server_remove_button)


        self.left_layout.addLayout(self.horizontalLayout_3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.left_layout.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bot_choice = QComboBoxChangeIndex(self.centralwidget)
        self.bot_choice.setObjectName(u"bot_choice")

        self.horizontalLayout_4.addWidget(self.bot_choice)

        self.bot_edit_button = QPushButton(self.centralwidget)
        self.bot_edit_button.setObjectName(u"bot_edit_button")

        self.horizontalLayout_4.addWidget(self.bot_edit_button)

        self.bot_remove_button = QPushButton(self.centralwidget)
        self.bot_remove_button.setObjectName(u"bot_remove_button")

        self.horizontalLayout_4.addWidget(self.bot_remove_button)

        self.bot_add_new = QPushButton(self.centralwidget)
        self.bot_add_new.setObjectName(u"bot_add_new")

        self.horizontalLayout_4.addWidget(self.bot_add_new)


        self.left_layout.addLayout(self.horizontalLayout_4)

        self.bot_reload = QPushButton(self.centralwidget)
        self.bot_reload.setObjectName(u"bot_reload")

        self.left_layout.addWidget(self.bot_reload)


        self.horizontalLayout_5.addLayout(self.left_layout)

        self.right_layout = QVBoxLayout()
        self.right_layout.setObjectName(u"right_layout")
        self.console_output_tab_view = QTabWidget(self.centralwidget)
        self.console_output_tab_view.setObjectName(u"console_output_tab_view")
        self.console_output_tab_view.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.console_output_tab_view.setTabPosition(QTabWidget.South)
        self.console_output_tab_view.setTabsClosable(True)
        self.console_output_tab_view.setMovable(True)

        self.right_layout.addWidget(self.console_output_tab_view)

        self.reload_cog_button = QPushButton(self.centralwidget)
        self.reload_cog_button.setObjectName(u"reload_cog_button")
        font1 = QFont()
        font1.setPointSize(14)
        self.reload_cog_button.setFont(font1)

        self.right_layout.addWidget(self.reload_cog_button)


        self.horizontalLayout_5.addLayout(self.right_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1088, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.console_output_tab_view.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cog", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.cog_add_new.setText(QCoreApplication.translate("MainWindow", u"Add new", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Servers", None))
        self.server_edit_button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.server_add_new.setText(QCoreApplication.translate("MainWindow", u"Add new", None))
        self.server_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bots", None))
        self.bot_edit_button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.bot_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.bot_add_new.setText(QCoreApplication.translate("MainWindow", u"Add new", None))
        self.bot_reload.setText(QCoreApplication.translate("MainWindow", u"reload for current server", None))
        self.reload_cog_button.setText(QCoreApplication.translate("MainWindow", u"RELOAD COG", None))
    # retranslateUi

