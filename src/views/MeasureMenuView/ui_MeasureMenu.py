# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MeasureMenuVqeJkJ.ui'
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
        MainWindow.setStyleSheet(u"background-color: white;\n"
"font-family: Poppins;\n"
"font-size:20px;\n"
"font-weight: 500;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.calibrationBtn = QPushButton(self.centralwidget)
        self.calibrationBtn.setObjectName(u"calibrationBtn")
        self.calibrationBtn.setGeometry(QRect(0, 142, 481, 71))
        self.calibrationBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"}")
        self.calibrationBtn.setIconSize(QSize(50, 50))
        self.monitoringBtn = QPushButton(self.centralwidget)
        self.monitoringBtn.setObjectName(u"monitoringBtn")
        self.monitoringBtn.setGeometry(QRect(0, 0, 481, 71))
        self.monitoringBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #22577a;\n"
"	color: white;\n"
"}")
        self.monitoringBtn.setIconSize(QSize(50, 50))
        self.historyBtn = QPushButton(self.centralwidget)
        self.historyBtn.setObjectName(u"historyBtn")
        self.historyBtn.setGeometry(QRect(0, 71, 481, 71))
        self.historyBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"}")
        self.historyBtn.setIconSize(QSize(50, 50))
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(0, 213, 481, 59))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"}")
        self.backBtn.setIconSize(QSize(50, 50))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.calibrationBtn.setText(QCoreApplication.translate("MainWindow", u"Calibraci\u00f3n", None))
        self.monitoringBtn.setText(QCoreApplication.translate("MainWindow", u"Medir", None))
        self.historyBtn.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
    # retranslateUi

