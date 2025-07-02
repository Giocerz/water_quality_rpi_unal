# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadingPopupGPScMsJWe.ui'
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
        Form.setStyleSheet(u"")
        self.LabelInfo = QLabel(Form)
        self.LabelInfo.setObjectName(u"LabelInfo")
        self.LabelInfo.setGeometry(QRect(0, 140, 480, 91))
        self.LabelInfo.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"color: white;\n"
"font-weight: 500;\n"
"")
        self.LabelInfo.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 480, 281))
        self.label.setStyleSheet(u"background-color: #266676;")
        self.satelliteLbl = QLabel(Form)
        self.satelliteLbl.setObjectName(u"satelliteLbl")
        self.satelliteLbl.setGeometry(QRect(200, 60, 81, 81))
        self.cancelBtn = QPushButton(Form)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(120, 220, 240, 42))
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 16px;\n"
"	border: none;\n"
"	font-family: \"Poppins\";\n"
"}")
        self.label.raise_()
        self.LabelInfo.raise_()
        self.satelliteLbl.raise_()
        self.cancelBtn.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LabelInfo.setText(QCoreApplication.translate("Form", u"Cargando...", None))
        self.label.setText("")
        self.satelliteLbl.setText("")
        self.cancelBtn.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

