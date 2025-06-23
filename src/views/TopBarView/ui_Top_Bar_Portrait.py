# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Top_Bar_PortraitvEUNtS.ui'
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
        Form.resize(320, 48)
        Form.setStyleSheet(u"QLabel {\n"
"	font-family: Poppins;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: white;\n"
"}")
        self.baterryLevel = QLabel(Form)
        self.baterryLevel.setObjectName(u"baterryLevel")
        self.baterryLevel.setGeometry(QRect(250, 11, 60, 26))
        self.baterryLevel.setStyleSheet(u"background: qlineargradient(\n"
"    x1: 0, y1: 0, x2: 1, y2: 0,\n"
"    stop:0 rgba(102, 164, 181, 255),\n"
"	stop:0.5 rgba(102, 164, 181, 255), \n"
"	stop:0.51 rgba(38, 102, 118, 255), \n"
"	stop:1 rgba(38, 102, 118, 255)\n"
");\n"
"border-radius: 12px;\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.baterryLevel.setAlignment(Qt.AlignCenter)
        self.chargeIndicator = QLabel(Form)
        self.chargeIndicator.setObjectName(u"chargeIndicator")
        self.chargeIndicator.setGeometry(QRect(210, 10, 26, 26))
        self.border = QLabel(Form)
        self.border.setObjectName(u"border")
        self.border.setGeometry(QRect(0, 45, 480, 3))
        self.border.setStyleSheet(u"background-color: rgb(199, 199, 199);")
        self.timeLbl = QLabel(Form)
        self.timeLbl.setObjectName(u"timeLbl")
        self.timeLbl.setGeometry(QRect(10, 0, 61, 41))
        self.timeLbl.setStyleSheet(u"color: #266676;\n"
"font-weight: bold;\n"
"font-size: 18px;")
        self.networkLbl = QLabel(Form)
        self.networkLbl.setObjectName(u"networkLbl")
        self.networkLbl.setGeometry(QRect(70, 5, 31, 31))
        self.networkLbl.setStyleSheet(u"	font-size: 14pt;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.baterryLevel.setText(QCoreApplication.translate("Form", u"100", None))
        self.chargeIndicator.setText("")
        self.border.setText("")
        self.timeLbl.setText(QCoreApplication.translate("Form", u"10:34", None))
        self.networkLbl.setText("")
    # retranslateUi

