# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManualGPSPopupsKXaxV.ui'
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
        self.Widget1 = QWidget(Form)
        self.Widget1.setObjectName(u"Widget1")
        self.Widget1.setEnabled(True)
        self.Widget1.setGeometry(QRect(0, 0, 480, 272))
        self.Widget1.setStyleSheet(u"QLabel {\n"
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
        self.lbl = QLabel(self.Widget1)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setGeometry(QRect(220, 130, 191, 31))
        self.lbl.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"")
        self.latitudeInput = QLineEdit(self.Widget1)
        self.latitudeInput.setObjectName(u"latitudeInput")
        self.latitudeInput.setGeometry(QRect(220, 160, 201, 26))
        self.latitudeInput.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"background-color: rgb(234, 234, 234);\n"
"font: 14px \"Poppins\";")
        self.latitudeInput.setMaxLength(50)
        self.latitudeInput.setEchoMode(QLineEdit.Normal)
        self.longitudeInput = QLineEdit(self.Widget1)
        self.longitudeInput.setObjectName(u"longitudeInput")
        self.longitudeInput.setGeometry(QRect(220, 190, 201, 26))
        self.longitudeInput.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"background-color: rgb(234, 234, 234);\n"
"font: 14px \"Poppins\";")
        self.longitudeInput.setMaxLength(50)
        self.longitudeInput.setEchoMode(QLineEdit.Normal)
        self.lbl_2 = QLabel(self.Widget1)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setGeometry(QRect(170, 0, 311, 31))
        self.lbl_2.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"")
        self.lbl_2.setAlignment(Qt.AlignCenter)
        self.QRLbl = QLabel(self.Widget1)
        self.QRLbl.setObjectName(u"QRLbl")
        self.QRLbl.setGeometry(QRect(275, 30, 100, 100))
        self.QRLbl.setStyleSheet(u"")
        self.widgetKeyboard = QWidget(self.Widget1)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 0, 171, 271))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.closeBtn = QPushButton(self.Widget1)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(170, 230, 141, 42))
        self.closeBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 16px;\n"
"	border: 1px solid #266676;\n"
"}")
        self.confirmBtn = QPushButton(self.Widget1)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(310, 230, 171, 42))
        self.confirmBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl.setText(QCoreApplication.translate("Form", u"Ingrese la ubicaci\u00f3n", None))
        self.latitudeInput.setPlaceholderText(QCoreApplication.translate("Form", u"Latitud", None))
        self.longitudeInput.setPlaceholderText(QCoreApplication.translate("Form", u"Longitud", None))
        self.lbl_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">Escanea el QR</span></p></body></html>", None))
        self.QRLbl.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.closeBtn.setText(QCoreApplication.translate("Form", u"Cerrar", None))
        self.confirmBtn.setText(QCoreApplication.translate("Form", u"Confirmar", None))
    # retranslateUi

