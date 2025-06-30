# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MonitoringSelectbxLEhG.ui'
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
        self.initBtn.setGeometry(QRect(149, 221, 331, 51))
        self.initBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"	font-size: 18px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(0, 221, 151, 51))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 18px;\n"
"	border: none;\n"
"}")
        self.tdsCheckBox = QCheckBox(self.centralwidget)
        self.tdsCheckBox.setObjectName(u"tdsCheckBox")
        self.tdsCheckBox.setGeometry(QRect(110, 40, 261, 35))
        self.tdsCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.tdsCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 16px \"Poppins\";\n"
"	color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border: 2px solid white; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: white; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 480, 41))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 180, 480, 41))
        self.label_2.setStyleSheet(u"font-size: 14px;\n"
"background-color: #e76f51;\n"
"color: white;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 41, 480, 35))
        self.label_3.setStyleSheet(u"background-color: #22577a;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 76, 480, 35))
        self.label_4.setStyleSheet(u"background-color: #1a759f;")
        self.phCheckBox = QCheckBox(self.centralwidget)
        self.phCheckBox.setObjectName(u"phCheckBox")
        self.phCheckBox.setGeometry(QRect(110, 76, 261, 35))
        self.phCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.phCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 16px \"Poppins\";\n"
"	color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border: 2px solid white; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: white; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 111, 480, 35))
        self.label_5.setStyleSheet(u"background-color: #22577a;")
        self.oxygenCheckBox = QCheckBox(self.centralwidget)
        self.oxygenCheckBox.setObjectName(u"oxygenCheckBox")
        self.oxygenCheckBox.setGeometry(QRect(110, 111, 261, 35))
        self.oxygenCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.oxygenCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 16px \"Poppins\";\n"
"	color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border: 2px solid white; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: white; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 146, 480, 35))
        self.label_6.setStyleSheet(u"background-color: #1a759f;")
        self.allCheckBox = QCheckBox(self.centralwidget)
        self.allCheckBox.setObjectName(u"allCheckBox")
        self.allCheckBox.setGeometry(QRect(110, 146, 261, 35))
        self.allCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.allCheckBox.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	height: 10px;\n"
"	font: 16px \"Poppins\";\n"
"	color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Ancho del indicador */\n"
"    height: 20px; /* Alto del indicador */\n"
"    border: 2px solid white; /* Borde del indicador */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: white; /* Color de fondo cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.initBtn.raise_()
        self.backBtn.raise_()
        self.tdsCheckBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.phCheckBox.raise_()
        self.oxygenCheckBox.raise_()
        self.allCheckBox.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.initBtn.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.tdsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Conductividad El\u00e9ctrica/TDS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Escoja los par\u00e1metros que desea monitorear</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>La temperatura est\u00e1 activada por defecto</p></body></html>", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.phCheckBox.setText(QCoreApplication.translate("MainWindow", u"pH", None))
        self.label_5.setText("")
        self.oxygenCheckBox.setText(QCoreApplication.translate("MainWindow", u"Ox\u00edgeno Disuelto", None))
        self.label_6.setText("")
        self.allCheckBox.setText(QCoreApplication.translate("MainWindow", u"Seleccionar todos", None))
    # retranslateUi

