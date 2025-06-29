# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopupWidgetSWMvTy.ui'
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
        self.WidgetInfo = QWidget(Form)
        self.WidgetInfo.setObjectName(u"WidgetInfo")
        self.WidgetInfo.setEnabled(True)
        self.WidgetInfo.setGeometry(QRect(29, 55, 422, 162))
        self.WidgetInfo.setStyleSheet(u"border-radius: 5px;\n"
"background-color: white;")
        self.si = QPushButton(self.WidgetInfo)
        self.si.setObjectName(u"si")
        self.si.setGeometry(QRect(211, 111, 211, 51))
        self.si.setStyleSheet(u"font: 500 16px \"Poppins\";\n"
"border-radius: 0px;\n"
"background-color: #266676;\n"
"color: white;")
        self.LabelInfo = QLabel(self.WidgetInfo)
        self.LabelInfo.setObjectName(u"LabelInfo")
        self.LabelInfo.setGeometry(QRect(80, 10, 331, 91))
        self.LabelInfo.setStyleSheet(u"font: 16px \"Poppins\";\n"
"background-color: transparent;\n"
"border: none;")
        self.IconInfo = QLabel(self.WidgetInfo)
        self.IconInfo.setObjectName(u"IconInfo")
        self.IconInfo.setGeometry(QRect(10, 30, 61, 61))
        self.IconInfo.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.no = QPushButton(self.WidgetInfo)
        self.no.setObjectName(u"no")
        self.no.setGeometry(QRect(0, 111, 211, 51))
        self.no.setStyleSheet(u"font: 500 16px \"Poppins\";\n"
"border-radius: 0px;\n"
"background-color: #1a759f;\n"
"color: white;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblOpacity.setText("")
        self.si.setText(QCoreApplication.translate("Form", u"Si", None))
        self.LabelInfo.setText(QCoreApplication.translate("Form", u"\u00a1Ajustes aplicados exitosamente!", None))
        self.IconInfo.setText("")
        self.no.setText(QCoreApplication.translate("Form", u"No", None))
    # retranslateUi

