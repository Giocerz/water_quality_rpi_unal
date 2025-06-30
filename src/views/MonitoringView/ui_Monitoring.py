# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MonitoringPVcrvG.ui'
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
        MainWindow.setStyleSheet(u"QLabel {\n"
"	font-family: Poppins;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"	background-color: white;\n"
"	font-size: 14px;\n"
"	font-family: Poppins;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.indicatorsWidget = QWidget(self.centralwidget)
        self.indicatorsWidget.setObjectName(u"indicatorsWidget")
        self.indicatorsWidget.setGeometry(QRect(20, 0, 461, 230))
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(0, 230, 160, 42))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 16px;\n"
"	border: 1px solid #266676;\n"
"}")
        self.pauseBtn = QPushButton(self.centralwidget)
        self.pauseBtn.setObjectName(u"pauseBtn")
        self.pauseBtn.setGeometry(QRect(160, 230, 160, 42))
        self.pauseBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.saveBtn = QPushButton(self.centralwidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(320, 230, 160, 42))
        self.saveBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.optionsBtn = QPushButton(self.centralwidget)
        self.optionsBtn.setObjectName(u"optionsBtn")
        self.optionsBtn.setGeometry(QRect(0, 0, 19, 231))
        self.optionsBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.pauseBtn.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.optionsBtn.setText("")
    # retranslateUi

