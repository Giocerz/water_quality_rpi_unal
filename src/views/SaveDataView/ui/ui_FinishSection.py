# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FinishSectionhdKaUp.ui'
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
"	background-color: #266676;\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.finishBtn = QPushButton(self.centralwidget)
        self.finishBtn.setObjectName(u"finishBtn")
        self.finishBtn.setGeometry(QRect(120, 220, 240, 42))
        self.finishBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 16px;\n"
"	border: none;\n"
"}")
        self.messageLbl = QLabel(self.centralwidget)
        self.messageLbl.setObjectName(u"messageLbl")
        self.messageLbl.setGeometry(QRect(0, 150, 481, 61))
        self.messageLbl.setStyleSheet(u"color: white;")
        self.messageLbl.setAlignment(Qt.AlignCenter)
        self.iconLbl = QLabel(self.centralwidget)
        self.iconLbl.setObjectName(u"iconLbl")
        self.iconLbl.setGeometry(QRect(180, 20, 120, 120))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.finishBtn.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.messageLbl.setText(QCoreApplication.translate("MainWindow", u"\u00a1Guardado completado!", None))
        self.iconLbl.setText("")
    # retranslateUi

