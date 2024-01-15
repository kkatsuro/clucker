# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InstallationWizard.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget,
    QWizard, QWizardPage)

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        if not Wizard.objectName():
            Wizard.setObjectName(u"Wizard")
        Wizard.resize(541, 551)
        self.wizardPage1 = QWizardPage()
        self.wizardPage1.setObjectName(u"wizardPage1")
        self.verticalLayout_3 = QVBoxLayout(self.wizardPage1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.wizardPage1)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.textBrowser = QTextBrowser(self.wizardPage1)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.label = QLabel(self.wizardPage1)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label)

        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        self.verticalLayout_4 = QVBoxLayout(self.wizardPage2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.venv_page_label = QLabel(self.wizardPage2)
        self.venv_page_label.setObjectName(u"venv_page_label")
        self.venv_page_label.setFont(font)

        self.verticalLayout_4.addWidget(self.venv_page_label)

        self.venv_page_text_browser = QTextBrowser(self.wizardPage2)
        self.venv_page_text_browser.setObjectName(u"venv_page_text_browser")

        self.verticalLayout_4.addWidget(self.venv_page_text_browser)

        self.venv_page_list = QListView(self.wizardPage2)
        self.venv_page_list.setObjectName(u"venv_page_list")

        self.verticalLayout_4.addWidget(self.venv_page_list)

        self.venv_page_button = QPushButton(self.wizardPage2)
        self.venv_page_button.setObjectName(u"venv_page_button")

        self.verticalLayout_4.addWidget(self.venv_page_button)

        Wizard.addPage(self.wizardPage2)
        self.wizardPage3 = QWizardPage()
        self.wizardPage3.setObjectName(u"wizardPage3")
        self.verticalLayout_5 = QVBoxLayout(self.wizardPage3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.wizardPage3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_5.addWidget(self.label_4)

        self.textBrowser_3 = QTextBrowser(self.wizardPage3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout_5.addWidget(self.textBrowser_3)

        self.listView_2 = QListView(self.wizardPage3)
        self.listView_2.setObjectName(u"listView_2")

        self.verticalLayout_5.addWidget(self.listView_2)

        self.pushButton_2 = QPushButton(self.wizardPage3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_5.addWidget(self.pushButton_2)

        Wizard.addPage(self.wizardPage3)
        self.wizardPage4 = QWizardPage()
        self.wizardPage4.setObjectName(u"wizardPage4")
        self.verticalLayout_6 = QVBoxLayout(self.wizardPage4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.wizardPage4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_6.addWidget(self.label_5)

        self.textBrowser_4 = QTextBrowser(self.wizardPage4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.verticalLayout_6.addWidget(self.textBrowser_4)

        self.listView_3 = QListView(self.wizardPage4)
        self.listView_3.setObjectName(u"listView_3")

        self.verticalLayout_6.addWidget(self.listView_3)

        self.pushButton_3 = QPushButton(self.wizardPage4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_6.addWidget(self.pushButton_3)

        Wizard.addPage(self.wizardPage4)

        self.retranslateUi(Wizard)

        QMetaObject.connectSlotsByName(Wizard)
    # setupUi

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QCoreApplication.translate("Wizard", u"Clucker Wizard", None))
        self.label_2.setText(QCoreApplication.translate("Wizard", u"Installing dependencies", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Wizard", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you haven't installed dependencies for Redbot yet, please do so now. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install only dependencies, ignore Creating Virtual Environment and next steps, they are automated in our software.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\">In future, maybe this page won't appear after checking for availibility of dependencies, or it would appear listing all missing dependencies.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://docs.discord.red/en/stable/install_guides/index.html. </p></body></html>", None))
        self.label.setText("")
        self.venv_page_label.setText(QCoreApplication.translate("Wizard", u"Add Redbot versions", None))
        self.venv_page_text_browser.setHtml(QCoreApplication.translate("Wizard", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add new Virtual Environment with Redbot version. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If Python is unavailable here, make sure it is installed and added to path (mention this in dependency page?).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\">If desired Redbot version is unavailable, it's probably because you can't install it on choosen Python version.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Virtual Environments here are loaded in a way there are loaded in installed version of program, so we detect them and display if anyone is reinstalling our software or something.. What if someone decided to move venv to our venv directory? It just won't work.. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">@todo: Maybe detect not working venvs? Maybe fix them? Or maybe use some venv alternative which is good and doesn't have issues with moved directory..</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Also @todo: support adding venv from other location ?</p></body></html>", None))
        self.venv_page_button.setText(QCoreApplication.translate("Wizard", u"Add new version (dialog will appear?)", None))
        self.label_4.setText(QCoreApplication.translate("Wizard", u"Add Bot Tokens", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Wizard", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You need at least one Token to create your Redbot application.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is recommended to have seperate bots for development in this application and for running 'in production' on your server.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\">https://docs.discord.red/en/stable/bot_application_guide.html</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">@todo: when we add new token, maybe verify if its working and then we could add support for loading: avatar, name, status, if we're the only thing connected to that token..</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Wizard", u"Add New Token", None))
        self.label_5.setText(QCoreApplication.translate("Wizard", u"Add new Redbot Instance", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("Wizard", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Each redbot instance works on different version, has different settings and cogs installed.</p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("Wizard", u"Add New Instance", None))
    # retranslateUi

