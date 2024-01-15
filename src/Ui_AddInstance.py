# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AddInstance.ui'
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
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddInstance(object):
    def setupUi(self, AddInstance):
        if not AddInstance.objectName():
            AddInstance.setObjectName(u"AddInstance")
        AddInstance.resize(398, 306)
        self.verticalLayout = QVBoxLayout(AddInstance)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AddInstance)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.name_label = QLabel(AddInstance)
        self.name_label.setObjectName(u"name_label")

        self.verticalLayout.addWidget(self.name_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_line_edit = QLineEdit(AddInstance)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.horizontalLayout.addWidget(self.name_line_edit)

        self.name_label_version = QLabel(AddInstance)
        self.name_label_version.setObjectName(u"name_label_version")

        self.horizontalLayout.addWidget(self.name_label_version)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.prefix_label = QLabel(AddInstance)
        self.prefix_label.setObjectName(u"prefix_label")

        self.verticalLayout.addWidget(self.prefix_label)

        self.prefix_line_edit = QLineEdit(AddInstance)
        self.prefix_line_edit.setObjectName(u"prefix_line_edit")

        self.verticalLayout.addWidget(self.prefix_line_edit)

        self.venv_label = QLabel(AddInstance)
        self.venv_label.setObjectName(u"venv_label")

        self.verticalLayout.addWidget(self.venv_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.venv_combo_box = QComboBox(AddInstance)
        self.venv_combo_box.setObjectName(u"venv_combo_box")

        self.horizontalLayout_2.addWidget(self.venv_combo_box)

        self.venv_add_button = QPushButton(AddInstance)
        self.venv_add_button.setObjectName(u"venv_add_button")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.venv_add_button.sizePolicy().hasHeightForWidth())
        self.venv_add_button.setSizePolicy(sizePolicy)
        self.venv_add_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.venv_add_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.token_label = QLabel(AddInstance)
        self.token_label.setObjectName(u"token_label")

        self.verticalLayout.addWidget(self.token_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.token_combo_box = QComboBox(AddInstance)
        self.token_combo_box.setObjectName(u"token_combo_box")

        self.horizontalLayout_3.addWidget(self.token_combo_box)

        self.token_add_button = QPushButton(AddInstance)
        self.token_add_button.setObjectName(u"token_add_button")
        sizePolicy.setHeightForWidth(self.token_add_button.sizePolicy().hasHeightForWidth())
        self.token_add_button.setSizePolicy(sizePolicy)
        self.token_add_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.token_add_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.dialog_buttons = QDialogButtonBox(AddInstance)
        self.dialog_buttons.setObjectName(u"dialog_buttons")
        self.dialog_buttons.setOrientation(Qt.Horizontal)
        self.dialog_buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.dialog_buttons)


        self.retranslateUi(AddInstance)
        self.dialog_buttons.accepted.connect(AddInstance.accept)
        self.dialog_buttons.rejected.connect(AddInstance.reject)

        QMetaObject.connectSlotsByName(AddInstance)
    # setupUi

    def retranslateUi(self, AddInstance):
        AddInstance.setWindowTitle(QCoreApplication.translate("AddInstance", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddInstance", u"Add New Instance", None))
        self.name_label.setText(QCoreApplication.translate("AddInstance", u"Instance Name", None))
        self.name_label_version.setText("")
        self.prefix_label.setText(QCoreApplication.translate("AddInstance", u"Bot prefix", None))
        self.prefix_line_edit.setText(QCoreApplication.translate("AddInstance", u"&", None))
        self.venv_label.setText(QCoreApplication.translate("AddInstance", u"Venv (Redbot Version)", None))
        self.venv_add_button.setText(QCoreApplication.translate("AddInstance", u"+", None))
        self.token_label.setText(QCoreApplication.translate("AddInstance", u"Token", None))
        self.token_add_button.setText(QCoreApplication.translate("AddInstance", u"+", None))
    # retranslateUi

