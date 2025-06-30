# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WifiListCnPXYR.ui'
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
"font-size:18px;\n"
"font-weight: 500;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.networkList = QListView(self.centralwidget)
        self.networkList.setObjectName(u"networkList")
        self.networkList.setGeometry(QRect(0, 0, 441, 221))
        self.networkList.setStyleSheet(u"border: none;\n"
"")
        self.networkList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.networkList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(440, 1, 41, 221))
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical{ \n"
"	background-color: rgb(234, 234, 234);\n"
"	height: 221px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical { \n"
"	background-color: #22577a;\n"
"    height: 60px;\n"
"    width: 20px;\n"
"    line-height: 10px; \n"
"	margin-top: 0px; \n"
"	margin-bottom: 0px;\n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"QSlider{\n"
"	background-color: rgb(234, 234, 234);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.verticalSlider.setPageStep(2)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(False)
        self.infoLbl = QLabel(self.centralwidget)
        self.infoLbl.setObjectName(u"infoLbl")
        self.infoLbl.setEnabled(True)
        self.infoLbl.setGeometry(QRect(50, 70, 321, 81))
        self.infoLbl.setStyleSheet(u"color: grey;\n"
"font-size: 24px;")
        self.refreshBtn = QPushButton(self.centralwidget)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setGeometry(QRect(240, 221, 240, 51))
        self.refreshBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #266676;\n"
"	color: white;\n"
"}")
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(0, 221, 240, 51))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	border: 1px solid #266676;\n"
"}")
        self.backBtn.setIconSize(QSize(50, 50))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.infoLbl.setText(QCoreApplication.translate("MainWindow", u"No se encontraron redes", None))
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
    # retranslateUi

