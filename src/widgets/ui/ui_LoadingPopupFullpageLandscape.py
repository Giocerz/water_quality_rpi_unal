# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadingPopupFullpageLandscapeThShwD.ui'
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
        self.LabelInfo.setGeometry(QRect(120, 150, 241, 91))
        self.LabelInfo.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"color: white;\n"
"font-weight: 500;\n"
"")
        self.LabelInfo.setAlignment(Qt.AlignCenter)
        self.firstCircle = QLabel(Form)
        self.firstCircle.setObjectName(u"firstCircle")
        self.firstCircle.setGeometry(QRect(180, 110, 31, 31))
        self.firstCircle.setStyleSheet(u"background-color: white;\n"
"border-radius: 15px;")
        self.secondCircle = QLabel(Form)
        self.secondCircle.setObjectName(u"secondCircle")
        self.secondCircle.setGeometry(QRect(220, 110, 31, 31))
        self.secondCircle.setStyleSheet(u"background-color: white;\n"
"border-radius: 15px;")
        self.thirdCircle = QLabel(Form)
        self.thirdCircle.setObjectName(u"thirdCircle")
        self.thirdCircle.setGeometry(QRect(260, 110, 31, 31))
        self.thirdCircle.setStyleSheet(u"background-color: white;\n"
"border-radius: 15px;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-6, 0, 491, 281))
        self.label.setStyleSheet(u"background-color: #266676;")
        self.label.raise_()
        self.LabelInfo.raise_()
        self.firstCircle.raise_()
        self.secondCircle.raise_()
        self.thirdCircle.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LabelInfo.setText(QCoreApplication.translate("Form", u"Cargando...", None))
        self.firstCircle.setText("")
        self.secondCircle.setText("")
        self.thirdCircle.setText("")
        self.label.setText("")
    # retranslateUi

