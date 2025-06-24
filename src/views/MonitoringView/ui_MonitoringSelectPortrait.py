# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MonitoringSelectPortraitCJULrr.ui'
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
        MainWindow.resize(320, 432)
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
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-size: 14px;\n"
"	font-family: Poppins;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QLabel {\n"
"	text-align: center;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.initBtn = QPushButton(self.centralwidget)
        self.initBtn.setObjectName(u"initBtn")
        self.initBtn.setGeometry(QRect(80, 350, 171, 41))
        self.initBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border-radius: 10px;\n"
"}")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(10, 10, 41, 41))
        self.backBtn.setStyleSheet(u"	height: 40px;\n"
"	border-radius: 10px;\n"
"	border: 2px solid #266276;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-weight: 500;\n"
"	font-size: 16px;")
        self.tdsCheckBox = QCheckBox(self.centralwidget)
        self.tdsCheckBox.setObjectName(u"tdsCheckBox")
        self.tdsCheckBox.setGeometry(QRect(90, 120, 151, 31))
        self.tdsCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.tdsCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.phCheckBox = QCheckBox(self.centralwidget)
        self.phCheckBox.setObjectName(u"phCheckBox")
        self.phCheckBox.setGeometry(QRect(100, 150, 141, 31))
        self.phCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.phCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.oxygenCheckBox = QCheckBox(self.centralwidget)
        self.oxygenCheckBox.setObjectName(u"oxygenCheckBox")
        self.oxygenCheckBox.setGeometry(QRect(70, 180, 171, 31))
        self.oxygenCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.oxygenCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.allCheckBox = QCheckBox(self.centralwidget)
        self.allCheckBox.setObjectName(u"allCheckBox")
        self.allCheckBox.setGeometry(QRect(80, 210, 161, 31))
        self.allCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.allCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 14px \"Poppins\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    border: 2px solid #666; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #00007f; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.imageLbl = QLabel(self.centralwidget)
        self.imageLbl.setObjectName(u"imageLbl")
        self.imageLbl.setGeometry(QRect(200, 310, 121, 121))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, -2, 201, 51))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-20, 300, 361, 31))
        self.label_2.setStyleSheet(u"font-size: 14px;\n"
"border: 2px solid #266676;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 35, 201, 21))
        self.label_3.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.imageLbl.raise_()
        self.backBtn.raise_()
        self.tdsCheckBox.raise_()
        self.phCheckBox.raise_()
        self.oxygenCheckBox.raise_()
        self.allCheckBox.raise_()
        self.initBtn.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.initBtn.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.backBtn.setText("")
        self.tdsCheckBox.setText(QCoreApplication.translate("MainWindow", u"CE/TDS/Salinidad", None))
        self.phCheckBox.setText(QCoreApplication.translate("MainWindow", u"pH", None))
        self.oxygenCheckBox.setText(QCoreApplication.translate("MainWindow", u"Ox\u00edgeno Disuelto", None))
        self.allCheckBox.setText(QCoreApplication.translate("MainWindow", u"Seleccionar todos", None))
        self.imageLbl.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Escoja los par\u00e1metros", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>La temperatura est\u00e1 activada por defecto</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"que desea monitorear", None))
    # retranslateUi

