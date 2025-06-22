# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Top_BareqxOZY.ui'
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
        Form.resize(480, 48)
        Form.setStyleSheet(u"QLabel {\n"
"	font-family: Poppins;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: white;\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 111, 48))
        self.label.setStyleSheet(u"font-size: 18px;")
        self.batteryExtBorder = QLabel(Form)
        self.batteryExtBorder.setObjectName(u"batteryExtBorder")
        self.batteryExtBorder.setGeometry(QRect(380, 11, 60, 26))
        self.batteryExtBorder.setStyleSheet(u"border: 2px solid #00007f;\n"
"border-radius: 12px;\n"
"background-color: transparent;")
        self.baterryLevel = QLabel(Form)
        self.baterryLevel.setObjectName(u"baterryLevel")
        self.baterryLevel.setGeometry(QRect(380, 11, 60, 26))
        self.baterryLevel.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 0,\n"
"    stop:0 rgba(255, 255, 255, 255),\n"
"	stop:0 rgba(255, 255, 255, 255), \n"
"	stop:0 rgba(0, 0, 127, 255), \n"
"	stop:1 rgba(0, 0, 127, 255)\n"
");\n"
"border-radius: 12px;\n"
"\n"
"")
        self.batteryIntBorder = QLabel(Form)
        self.batteryIntBorder.setObjectName(u"batteryIntBorder")
        self.batteryIntBorder.setGeometry(QRect(382, 13, 56, 22))
        self.batteryIntBorder.setStyleSheet(u"border: 2px solid white;\n"
"background-color: transparent;\n"
"border-radius: 10px;")
        self.batteryLbl = QLabel(Form)
        self.batteryLbl.setObjectName(u"batteryLbl")
        self.batteryLbl.setGeometry(QRect(445, 14, 31, 20))
        self.batteryLbl.setStyleSheet(u"color: #00007f;\n"
"font-weight: bold;")
        self.chargeIndicator = QLabel(Form)
        self.chargeIndicator.setObjectName(u"chargeIndicator")
        self.chargeIndicator.setGeometry(QRect(350, 10, 26, 26))
        self.border = QLabel(Form)
        self.border.setObjectName(u"border")
        self.border.setGeometry(QRect(0, 45, 480, 3))
        self.border.setStyleSheet(u"background-color: rgb(199, 199, 199);")
        self.timeLbl = QLabel(Form)
        self.timeLbl.setObjectName(u"timeLbl")
        self.timeLbl.setGeometry(QRect(170, 1, 91, 41))
        self.timeLbl.setStyleSheet(u"color: #00007f;\n"
"font-weight: bold;\n"
"font-size: 18px;")
        self.networkLbl = QLabel(Form)
        self.networkLbl.setObjectName(u"networkLbl")
        self.networkLbl.setGeometry(QRect(130, 5, 31, 31))
        self.networkLbl.setStyleSheet(u"	font-size: 14pt;")
        self.baterryLevel.raise_()
        self.batteryExtBorder.raise_()
        self.label.raise_()
        self.batteryIntBorder.raise_()
        self.batteryLbl.raise_()
        self.chargeIndicator.raise_()
        self.border.raise_()
        self.timeLbl.raise_()
        self.networkLbl.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.batteryExtBorder.setText("")
        self.baterryLevel.setText("")
        self.batteryIntBorder.setText("")
        self.batteryLbl.setText(QCoreApplication.translate("Form", u"100%", None))
        self.chargeIndicator.setText("")
        self.border.setText("")
        self.timeLbl.setText(QCoreApplication.translate("Form", u"10:34", None))
        self.networkLbl.setText("")
    # retranslateUi

