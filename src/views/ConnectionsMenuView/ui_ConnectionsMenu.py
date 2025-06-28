# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConnectionsMenueFJxTJ.ui'
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
        self.wifiBtn = QPushButton(self.centralwidget)
        self.wifiBtn.setObjectName(u"wifiBtn")
        self.wifiBtn.setGeometry(QRect(0, 0, 481, 106))
        self.wifiBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #22577a;\n"
"	color: white;\n"
"}")
        self.wifiBtn.setIconSize(QSize(50, 50))
        self.bluetoothBtn = QPushButton(self.centralwidget)
        self.bluetoothBtn.setObjectName(u"bluetoothBtn")
        self.bluetoothBtn.setGeometry(QRect(0, 106, 481, 106))
        self.bluetoothBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"}")
        self.bluetoothBtn.setIconSize(QSize(50, 50))
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(0, 212, 481, 60))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"}")
        self.backBtn.setIconSize(QSize(50, 50))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.wifiBtn.setText(QCoreApplication.translate("MainWindow", u"WiFi", None))
        self.bluetoothBtn.setText(QCoreApplication.translate("MainWindow", u"Bluetooth", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
    # retranslateUi

