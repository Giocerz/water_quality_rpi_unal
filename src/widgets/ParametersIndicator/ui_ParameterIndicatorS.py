# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParameterIndicatorSCneYHJ.ui'
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
        Form.resize(461, 46)
        Form.setStyleSheet(u"QLabel {\n"
"	font-family: Poppins;\n"
"	font-size: 16px;\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 0, 461, 46))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border-radius: 0px;\n"
"    background-color: #66a4b5;\n"
"	border-bottom: 2px solid white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #266676;\n"
"    border-radius: 0px;\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)
        self.nameLbl = QLabel(Form)
        self.nameLbl.setObjectName(u"nameLbl")
        self.nameLbl.setGeometry(QRect(10, 0, 201, 46))
        self.nameLbl.setStyleSheet(u"color: white;")
        self.valueLbl = QLabel(Form)
        self.valueLbl.setObjectName(u"valueLbl")
        self.valueLbl.setGeometry(QRect(290, 0, 101, 46))
        self.valueLbl.setStyleSheet(u"color: white;")
        self.stableLbl = QLabel(Form)
        self.stableLbl.setObjectName(u"stableLbl")
        self.stableLbl.setGeometry(QRect(400, 3, 40, 40))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nameLbl.setText(QCoreApplication.translate("Form", u"title", None))
        self.valueLbl.setText(QCoreApplication.translate("Form", u"2000 uScm", None))
        self.stableLbl.setText("")
    # retranslateUi

