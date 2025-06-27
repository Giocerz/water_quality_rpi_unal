from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from .ui_ConnectionsMenu import Ui_MainWindow
from src.views.WifiView.WifiView import WifiView
from src.views.BluetoothView.BluetoothView import BluetoothView
from src.package.Navigator import Navigator

class ConnectionsMenuView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.wifiBtn.clicked.connect(self.on_wifi_clicked)
        self.ui.bluetoothBtn.clicked.connect(self.on_bluetooth_clicked)
        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/wifi_w.png')
        self.ui.wifiBtn.setIcon(icon)
        self.ui.wifiBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/bluetooth_w.png')
        self.ui.bluetoothBtn.setIcon(icon)
        self.ui.bluetoothBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(40, 40))

    def on_wifi_clicked(self):
        Navigator.push(context= self.context, view= WifiView(context= self.context))

    def on_bluetooth_clicked(self):
        Navigator.push(context= self.context, view= BluetoothView(context= self.context))
    
    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self)
