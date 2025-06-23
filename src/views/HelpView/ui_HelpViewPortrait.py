# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HelpViewPortraitYSoIPz.ui'
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
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font: 14px Poppins;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 181, 41))
        self.label.setStyleSheet(u"font-size: 20px;\n"
"color: #266676;")
        self.label.setAlignment(Qt.AlignCenter)
        self.sensorsBtn = QPushButton(self.centralwidget)
        self.sensorsBtn.setObjectName(u"sensorsBtn")
        self.sensorsBtn.setGeometry(QRect(35, 130, 251, 61))
        self.sensorsBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"	font-size: 20px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border-radius: 10px;\n"
"}")
        self.moreHelpBtn = QPushButton(self.centralwidget)
        self.moreHelpBtn.setObjectName(u"moreHelpBtn")
        self.moreHelpBtn.setGeometry(QRect(35, 270, 251, 61))
        self.moreHelpBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #DDB622;\n"
"	color: white;\n"
"	font-size: 20px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border-radius: 10px;\n"
"}")
        self.aboutBtn = QPushButton(self.centralwidget)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setGeometry(QRect(35, 200, 251, 61))
        self.aboutBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #9B482F;\n"
"	color: white;\n"
"	font-size: 20px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border-radius: 10px;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.backBtn.raise_()
        self.sensorsBtn.raise_()
        self.moreHelpBtn.raise_()
        self.aboutBtn.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.sensorsBtn.setText(QCoreApplication.translate("MainWindow", u"Ubicaci\u00f3n sensores", None))
        self.moreHelpBtn.setText(QCoreApplication.translate("MainWindow", u"M\u00e1s ayuda", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"Acerca", None))
    # retranslateUi

