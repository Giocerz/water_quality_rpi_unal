# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenuyjbIPj.ui'
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
        self.settingBtn = QPushButton(self.centralwidget)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setGeometry(QRect(0, 182, 481, 90))
        self.settingBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #22577a;\n"
"	color: white;\n"
"}")
        self.settingBtn.setIconSize(QSize(50, 50))
        self.monitoringBtn = QPushButton(self.centralwidget)
        self.monitoringBtn.setObjectName(u"monitoringBtn")
        self.monitoringBtn.setGeometry(QRect(0, 0, 481, 91))
        self.monitoringBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"}")
        self.monitoringBtn.setIconSize(QSize(50, 50))
        self.connectionsBtn = QPushButton(self.centralwidget)
        self.connectionsBtn.setObjectName(u"connectionsBtn")
        self.connectionsBtn.setGeometry(QRect(0, 91, 481, 91))
        self.connectionsBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"}")
        self.connectionsBtn.setIconSize(QSize(50, 50))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.monitoringBtn.setText(QCoreApplication.translate("MainWindow", u"Mediciones", None))
        self.connectionsBtn.setText(QCoreApplication.translate("MainWindow", u"Conexiones", None))
    # retranslateUi

