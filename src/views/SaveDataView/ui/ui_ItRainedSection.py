# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ItRainedSectionrBqstI.ui'
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
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(0, 230, 240, 42))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 16px;\n"
"	border: 1px solid #266676;\n"
"}")
        self.nextBtn = QPushButton(self.centralwidget)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setGeometry(QRect(240, 230, 240, 42))
        self.nextBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.noCheckBox = QCheckBox(self.centralwidget)
        self.noCheckBox.setObjectName(u"noCheckBox")
        self.noCheckBox.setGeometry(QRect(180, 110, 91, 31))
        self.noCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #266676; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -1, 481, 41))
        self.label.setAlignment(Qt.AlignCenter)
        self.yesCheckBox = QCheckBox(self.centralwidget)
        self.yesCheckBox.setObjectName(u"yesCheckBox")
        self.yesCheckBox.setGeometry(QRect(180, 70, 91, 31))
        self.yesCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #266676; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.idkCheckBox = QCheckBox(self.centralwidget)
        self.idkCheckBox.setObjectName(u"idkCheckBox")
        self.idkCheckBox.setGeometry(QRect(180, 150, 91, 31))
        self.idkCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #266676; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.noCheckBox.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00bfLlovi\u00f3 recientemente?", None))
        self.yesCheckBox.setText(QCoreApplication.translate("MainWindow", u"S\u00ed", None))
        self.idkCheckBox.setText(QCoreApplication.translate("MainWindow", u"No lo s\u00e9", None))
    # retranslateUi

