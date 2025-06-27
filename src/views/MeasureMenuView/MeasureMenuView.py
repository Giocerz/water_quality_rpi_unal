import os
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from .ui_MeasureMenu import Ui_MainWindow
from src.views.MonitoringView.MonitoringSelect import MonitoringSelectView
from src.views.CalibrationView.CalibrationView import CalibrationView
from src.views.FoldersView.FoldersView import FoldersView
from src.package.Navigator import Navigator

class MeasureMenuView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.monitoringBtn.clicked.connect(self.on_monitoring_clicked)
        self.ui.historyBtn.clicked.connect(self.on_datos_clicked)
        self.ui.calibrationBtn.clicked.connect(self.on_calibration_clicked)
        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/water_w.png')
        self.ui.monitoringBtn.setIcon(icon)
        self.ui.monitoringBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/analytics_w.png')
        self.ui.historyBtn.setIcon(icon)
        self.ui.historyBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/stacked_line_w.png')
        self.ui.calibrationBtn.setIcon(icon)
        self.ui.calibrationBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(40, 40))

    def on_monitoring_clicked(self):
        Navigator.push(context= self.context, view= MonitoringSelectView(context= self.context))

    def on_calibration_clicked(self):
        Navigator.push(context= self.context, view= CalibrationView(context= self.context))

    def on_datos_clicked(self):
        Navigator.push(context= self.context, view= FoldersView(context= self.context))
    
    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self)
