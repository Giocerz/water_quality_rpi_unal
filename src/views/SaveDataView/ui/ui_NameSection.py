# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NameSectionfHJPlH.ui'
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
        self.backBtn.setGeometry(QRect(0, 100, 240, 42))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 16px;\n"
"	border: 1px solid #266676;\n"
"}")
        self.nextBtn = QPushButton(self.centralwidget)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setGeometry(QRect(240, 100, 240, 42))
        self.nextBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.widgetKeyboard = QWidget(self.centralwidget)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 140, 480, 135))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.inputPlace = QLineEdit(self.centralwidget)
        self.inputPlace.setObjectName(u"inputPlace")
        self.inputPlace.setGeometry(QRect(20, 45, 441, 31))
        self.inputPlace.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"background-color: rgb(234, 234, 234);\n"
"font: 14px Poppins;")
        self.inputPlace.setMaxLength(50)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 221, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.widgetKeyboard.raise_()
        self.backBtn.raise_()
        self.nextBtn.raise_()
        self.inputPlace.raise_()
        self.label.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
        self.inputPlace.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: Colegio de Manaure", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nombre de la muestra</p></body></html>", None))
    # retranslateUi

