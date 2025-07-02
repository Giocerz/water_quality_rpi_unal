# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FolderSectionGQjtwb.ui'
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
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 431, 231))
        self.scrollArea.setStyleSheet(u"border: opx;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 431, 231))
        self.emptyFoldersNoticeLbl = QLabel(self.scrollAreaWidgetContents)
        self.emptyFoldersNoticeLbl.setObjectName(u"emptyFoldersNoticeLbl")
        self.emptyFoldersNoticeLbl.setGeometry(QRect(50, 70, 351, 81))
        self.emptyFoldersNoticeLbl.setStyleSheet(u"color: grey;\n"
"font-size: 24px;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalSlider = QSlider(self.page)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(430, 0, 41, 231))
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical{ \n"
"	background-color: rgb(234, 234, 234);\n"
"	height: 231px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical { \n"
"	background-color: #22577a;\n"
"    height: 50px;\n"
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
        self.backBtn = QPushButton(self.page)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(0, 230, 160, 42))
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	color: #266676;\n"
"	font-size: 16px;\n"
"	border: 1px solid #266676;\n"
"}")
        self.nextBtn = QPushButton(self.page)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setGeometry(QRect(320, 230, 160, 42))
        self.nextBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1a759f;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
        self.saveBtn = QPushButton(self.page)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(160, 230, 160, 42))
        self.saveBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #22577a;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	height: 50px;\n"
"	border: none;\n"
"}")
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
        self.emptyFoldersNoticeLbl.setText(QCoreApplication.translate("MainWindow", u"No hay carpetas guardadas", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Nueva Carpeta", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nombre de la nueva carpeta</p></body></html>", None))
        self.inputPlace.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: Colegio de Manaure", None))
        self.backBtn_2.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.saveBtn_2.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
    # retranslateUi

