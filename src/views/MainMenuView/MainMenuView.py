import os
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from .ui_MainMenu import Ui_MainWindow
from src.views.MeasureMenuView.MeasureMenuView import MeasureMenuView
from src.views.CalibrationView.CalibrationView import CalibrationView
from src.views.FoldersView.FoldersView import FoldersView
from src.views.BluetoothView.BluetoothView import BluetoothView
from src.views.HelpView.HelpView import HelpView
from src.views.WifiView.WifiView import WifiView
from src.views.UpdateView.UpdateView import UpdateView
from src.widgets.PopupWidget import PopupWidget
from src.package.Navigator import Navigator

class MainMenuView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.monitoringBtn.clicked.connect(self.on_monitoring_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/sensors_w.png')
        self.ui.monitoringBtn.setIcon(icon)
        self.ui.monitoringBtn.setIconSize(QSize(45, 45))
        icon = QIcon('./src/resources/icons/network_manage_w.png')
        self.ui.connectionsBtn.setIcon(icon)
        self.ui.connectionsBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/settings_w.png')
        self.ui.settingBtn.setIcon(icon)
        self.ui.settingBtn.setIconSize(QSize(40, 40))

    def on_monitoring_clicked(self):
        Navigator.push(context= self.context, view= MeasureMenuView(context= self.context))

    def on_calibration_clicked(self):
        Navigator.push(context= self.context, view= CalibrationView(context= self.context))

    def on_datos_clicked(self):
        Navigator.push(context= self.context, view= FoldersView(context= self.context))

    def on_bluetooth_clicked(self):
        Navigator.push(context= self.context, view= BluetoothView(context= self.context))
    
    def on_wifi_clicked(self):
        Navigator.push(context= self.context, view= WifiView(context= self.context))
    
    def on_help_clicked(self):
        Navigator.push(context= self.context, view= HelpView(context= self.context))

    def on_update_clicked(self):
        Navigator.push(context= self.context, view= UpdateView(context= self.context))

    def on_power_clicked(self):
        def yes_callback():
            os.system("sudo poweroff")
        def no_callback():
            pass
        popup = PopupWidget(context=self.context, text="¿Quieres apagar el dispositivo?", yes_callback=yes_callback, no_callback=no_callback)
        popup.show()