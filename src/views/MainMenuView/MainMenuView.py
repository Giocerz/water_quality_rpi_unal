from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from .ui_MainMenu import Ui_MainWindow
from src.views.MeasureMenuView.MeasureMenuView import MeasureMenuView
from src.views.ConnectionsMenuView.ConnectionsMenuView import ConnectionsMenuView
from src.views.SettingsMenuView.SettingsMenuView import SettingsMenuView
from src.package.Navigator import Navigator

class MainMenuView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.monitoringBtn.clicked.connect(self.on_monitoring_clicked)
        self.ui.connectionsBtn.clicked.connect(self.on_connections_clicked)
        self.ui.settingBtn.clicked.connect(self.on_settings_clicked)

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

    def on_connections_clicked(self):
        Navigator.push(context= self.context, view= ConnectionsMenuView(context= self.context))

    def on_settings_clicked(self):
        Navigator.push(context= self.context, view= SettingsMenuView(context= self.context))