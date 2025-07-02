# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LocationSectionmsLZKd.ui'
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -1, 481, 61))
        self.label.setAlignment(Qt.AlignCenter)
        self.gpsBtn = QPushButton(self.centralwidget)
        self.gpsBtn.setObjectName(u"gpsBtn")
        self.gpsBtn.setGeometry(QRect(100, 80, 280, 42))
        self.gpsBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #22577a;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.setManualLocationBtn = QPushButton(self.centralwidget)
        self.setManualLocationBtn.setObjectName(u"setManualLocationBtn")
        self.setManualLocationBtn.setGeometry(QRect(120, 130, 240, 21))
        self.setManualLocationBtn.setStyleSheet(u"QPushButton {\n"
"	color: #22577a;\n"
"	font-size: 12px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 190, 281, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Localizaci\u00f3n de la muestra", None))
        self.gpsBtn.setText(QCoreApplication.translate("MainWindow", u"Localizar con el GPS", None))
        self.setManualLocationBtn.setText(QCoreApplication.translate("MainWindow", u"Ingresar manualmente", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Latitud, longitud</p></body></html>", None))
    # retranslateUi

