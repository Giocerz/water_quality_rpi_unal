# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatosrcBjRO.ui'
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
        MainWindow.setStyleSheet(u"font-family: Poppins;\n"
"background-color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QTableWidget {\n"
"	border: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 40px;\n"
"	border-radius: 20px;\n"
"	border: 1px solid #00007f;\n"
"	background-color: white;\n"
"	color: #00007f;\n"
"	font-weight: 500;\n"
"	font-size: 18px;\n"
"}")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 13):
            self.tableWidget.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(1, 5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(2, 5, __qtablewidgetitem27)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 481, 191))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #d9d9d9;\n"
"}")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(13)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(10, 220, 41, 41))
        self.backBtn.setStyleSheet(u"")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 195, 461, 21))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{ \n"
"    background-color: rgb(234, 234, 234);\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: #00007f;\n"
"    width: 60px;\n"
"    height: 20px;\n"
"    margin-left: 0px; \n"
"    margin-right: 0px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider{\n"
"    background-color: rgb(234, 234, 234);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.horizontalSlider.setPageStep(2)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.nextPageBtn = QPushButton(self.centralwidget)
        self.nextPageBtn.setObjectName(u"nextPageBtn")
        self.nextPageBtn.setGeometry(QRect(425, 220, 41, 41))
        self.nextPageBtn.setStyleSheet(u"")
        self.prevPageBtn = QPushButton(self.centralwidget)
        self.prevPageBtn.setObjectName(u"prevPageBtn")
        self.prevPageBtn.setGeometry(QRect(380, 220, 41, 41))
        self.prevPageBtn.setStyleSheet(u"")
        self.dataCountLbl = QLabel(self.centralwidget)
        self.dataCountLbl.setObjectName(u"dataCountLbl")
        self.dataCountLbl.setGeometry(QRect(260, 220, 111, 41))
        self.dataCountLbl.setStyleSheet(u"font-size: 10pt;")
        self.graphBtn = QPushButton(self.centralwidget)
        self.graphBtn.setObjectName(u"graphBtn")
        self.graphBtn.setGeometry(QRect(70, 220, 41, 41))
        self.graphBtn.setStyleSheet(u"")
        self.deleteBtn = QPushButton(self.centralwidget)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setGeometry(QRect(130, 220, 41, 41))
        self.deleteBtn.setStyleSheet(u"background-color: #e63946;\n"
"border: 0px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Etiqueta", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"OD", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"TDS", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"pH", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CE", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Calidad", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Valledupar", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"31.92", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"14.84", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"457.30", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"9.65", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"914.6", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Manaure", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"25.37", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"7.75", None));
        ___qtablewidgetitem16 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"526.49", None));
        ___qtablewidgetitem17 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"11.98", None));
        ___qtablewidgetitem18 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"1052.98", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"La Paz", None));
        ___qtablewidgetitem20 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"28.80", None));
        ___qtablewidgetitem21 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"21.96", None));
        ___qtablewidgetitem22 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"706.50", None));
        ___qtablewidgetitem23 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"7.89", None));
        ___qtablewidgetitem24 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"1413.00", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.backBtn.setText("")
        self.nextPageBtn.setText("")
        self.prevPageBtn.setText("")
        self.dataCountLbl.setText(QCoreApplication.translate("MainWindow", u"1-5 de 11", None))
        self.graphBtn.setText("")
        self.deleteBtn.setText("")
    # retranslateUi

