# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FolderSectionnrNdCx.ui'
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
"	background-color: white;\n"
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
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 480, 272))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.backBtn = QPushButton(self.page)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(0, 230, 160, 42))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 16px;\n"
"	border: 1px solid #266676;\n"
"}")
        self.saveBtn = QPushButton(self.page)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(320, 230, 160, 42))
        self.saveBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.createBtn = QPushButton(self.page)
        self.createBtn.setObjectName(u"createBtn")
        self.createBtn.setGeometry(QRect(160, 230, 160, 42))
        self.createBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #22577a;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.folderList = QListView(self.page)
        self.folderList.setObjectName(u"folderList")
        self.folderList.setGeometry(QRect(20, 61, 401, 131))
        self.folderList.setStyleSheet(u"border: none;")
        self.folderList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.folderList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.verticalSlider = QSlider(self.page)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(430, 61, 41, 161))
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical{ \n"
"	background-color: rgb(234, 234, 234);\n"
"	height: 161px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical { \n"
"	background-color: #22577a;\n"
"    height: 50;\n"
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
        self.verticalSlider.setPageStep(1)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(False)
        self.selectFolderLbl = QLabel(self.page)
        self.selectFolderLbl.setObjectName(u"selectFolderLbl")
        self.selectFolderLbl.setGeometry(QRect(20, 201, 401, 21))
        self.selectFolderLbl.setStyleSheet(u"border: 1px solid black;")
        self.selectFolderLbl.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 481, 61))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.widgetKeyboard = QWidget(self.page_2)
        self.widgetKeyboard.setObjectName(u"widgetKeyboard")
        self.widgetKeyboard.setGeometry(QRect(0, 140, 480, 135))
        self.widgetKeyboard.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 15, 241, 21))
        self.inputPlace = QLineEdit(self.page_2)
        self.inputPlace.setObjectName(u"inputPlace")
        self.inputPlace.setGeometry(QRect(20, 50, 441, 31))
        self.inputPlace.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"background-color: rgb(234, 234, 234);\n"
"font: 14px Poppins;")
        self.inputPlace.setMaxLength(50)
        self.backBtn_2 = QPushButton(self.page_2)
        self.backBtn_2.setObjectName(u"backBtn_2")
        self.backBtn_2.setGeometry(QRect(0, 100, 240, 42))
        self.backBtn_2.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 16px;\n"
"	border: 1px solid #266676;\n"
"}")
        self.saveBtn_2 = QPushButton(self.page_2)
        self.saveBtn_2.setObjectName(u"saveBtn_2")
        self.saveBtn_2.setGeometry(QRect(240, 100, 240, 42))
        self.saveBtn_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.createBtn.setText(QCoreApplication.translate("MainWindow", u"Nueva Carpeta", None))
        self.selectFolderLbl.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seleccione la carpeta en la que guardara la muestra", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nombre de la nueva carpeta</p></body></html>", None))
        self.inputPlace.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: Colegio de Manaure", None))
        self.backBtn_2.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.saveBtn_2.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
    # retranslateUi

