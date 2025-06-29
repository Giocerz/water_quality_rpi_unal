# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsMenucCDFbk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 272)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font-family: Poppins;\n"
"font-size:20px;\n"
"font-weight: 500;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.helpBtn = QPushButton(self.centralwidget)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setGeometry(QRect(0, 0, 481, 70))
        self.helpBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #22577a;\n"
"	color: white;\n"
"}")
        self.helpBtn.setIconSize(QSize(50, 50))
        self.aboutBtn = QPushButton(self.centralwidget)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setGeometry(QRect(0, 70, 481, 70))
        self.aboutBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"}")
        self.aboutBtn.setIconSize(QSize(50, 50))
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(0, 210, 240, 62))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"}")
        self.backBtn.setIconSize(QSize(50, 50))
        self.settingsBtn = QPushButton(self.centralwidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setGeometry(QRect(0, 140, 481, 70))
        self.settingsBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"}")
        self.settingsBtn.setIconSize(QSize(50, 50))
        self.powerBtn = QPushButton(self.centralwidget)
        self.powerBtn.setObjectName(u"powerBtn")
        self.powerBtn.setGeometry(QRect(240, 210, 240, 62))
        self.powerBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #ee4b6a;\n"
"	color: white;\n"
"}")
        self.powerBtn.setIconSize(QSize(50, 50))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"Acerca del dispositivo", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.powerBtn.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
    # retranslateUi

