# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WifiConnectpllFyy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 272)
        self.lblOpacity = QLabel(Form)
        self.lblOpacity.setObjectName(u"lblOpacity")
        self.lblOpacity.setGeometry(QRect(0, 0, 480, 320))
        self.lblOpacity.setStyleSheet(u"background-color: black;")
        self.Widget1 = QWidget(Form)
        self.Widget1.setObjectName(u"Widget1")
        self.Widget1.setEnabled(True)
        self.Widget1.setGeometry(QRect(65, 10, 351, 171))
        self.Widget1.setStyleSheet(u"border-radius: 20px;\n"
"background-color: white;")
        self.connectBtn = QPushButton(self.Widget1)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setGeometry(QRect(174, 90, 122, 31))
        self.connectBtn.setStyleSheet(u"font: 500 18px \"Poppins\";\n"
"border-radius: 10px;\n"
"border: 1px solid #00007f;\n"
"background-color: white;\n"
"color: #00007f;")
        self.ssidLbl = QLabel(self.Widget1)
        self.ssidLbl.setObjectName(u"ssidLbl")
        self.ssidLbl.setGeometry(QRect(20, 10, 311, 31))
        self.ssidLbl.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"font-weight: bold;\n"
"")
        self.inputPlace = QLineEdit(self.Widget1)
        self.inputPlace.setObjectName(u"inputPlace")
        self.inputPlace.setGeometry(QRect(55, 50, 241, 26))
        self.inputPlace.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 6px;\n"
"font: 12pt \"Poppins\";\n"
"background-color: rgb(234, 234, 234);")
        self.inputPlace.setMaxLength(50)
        self.inputPlace.setEchoMode(QLineEdit.Password)
        self.widgetKeyboard = QWidget(Form)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 140, 480, 135))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblOpacity.setText("")
        self.connectBtn.setText(QCoreApplication.translate("Form", u"Conectar", None))
        self.ssidLbl.setText(QCoreApplication.translate("Form", u"titulo", None))
        self.inputPlace.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
    # retranslateUi

