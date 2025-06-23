# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenuPortraitNbDVyo.ui'
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
        MainWindow.resize(320, 480)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font-family: Poppins;\n"
"font-size: 20px;\n"
"font-weight: 500;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 50px;\n"
"	border-radius: 10px;\n"
"}")
        self.powerBtn = QPushButton(self.centralwidget)
        self.powerBtn.setObjectName(u"powerBtn")
        self.powerBtn.setGeometry(QRect(160, 400, 71, 71))
        self.powerBtn.setStyleSheet(u"border: 2px solid #266276;")
        self.wifiBtn = QPushButton(self.centralwidget)
        self.wifiBtn.setObjectName(u"wifiBtn")
        self.wifiBtn.setGeometry(QRect(200, 210, 111, 91))
        self.wifiBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #DDB622;\n"
"	color: white;\n"
"}")
        self.updateBtn = QPushButton(self.centralwidget)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setGeometry(QRect(10, 310, 301, 81))
        self.updateBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"}")
        self.helpBtn = QPushButton(self.centralwidget)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setGeometry(QRect(10, 400, 141, 71))
        self.helpBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"}")
        self.monitoringBtn = QPushButton(self.centralwidget)
        self.monitoringBtn.setObjectName(u"monitoringBtn")
        self.monitoringBtn.setGeometry(QRect(10, 10, 301, 91))
        self.monitoringBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"}")
        self.calibrationBtn = QPushButton(self.centralwidget)
        self.calibrationBtn.setObjectName(u"calibrationBtn")
        self.calibrationBtn.setGeometry(QRect(10, 110, 151, 91))
        self.calibrationBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #DDB622;\n"
"	color: white;\n"
"}")
        self.bluetoothBtn = QPushButton(self.centralwidget)
        self.bluetoothBtn.setObjectName(u"bluetoothBtn")
        self.bluetoothBtn.setGeometry(QRect(10, 210, 181, 91))
        self.bluetoothBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #9B482F;\n"
"	color: white;\n"
"}")
        self.dataBtn = QPushButton(self.centralwidget)
        self.dataBtn.setObjectName(u"dataBtn")
        self.dataBtn.setGeometry(QRect(170, 110, 141, 91))
        self.dataBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #8EB9AF;\n"
"	color: white;\n"
"}")
        self.settingsBtn = QPushButton(self.centralwidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setGeometry(QRect(240, 400, 71, 71))
        self.settingsBtn.setStyleSheet(u"border: 2px solid #266276;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.powerBtn.setText("")
        self.wifiBtn.setText(QCoreApplication.translate("MainWindow", u"WiFi", None))
        self.updateBtn.setText(QCoreApplication.translate("MainWindow", u"Actualizaciones", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.monitoringBtn.setText(QCoreApplication.translate("MainWindow", u"Monitoreo", None))
        self.calibrationBtn.setText(QCoreApplication.translate("MainWindow", u"Calibraci\u00f3n", None))
        self.bluetoothBtn.setText(QCoreApplication.translate("MainWindow", u"Bluetooth", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.settingsBtn.setText("")
    # retranslateUi

