import os
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from .ui_SettingsMenu import Ui_MainWindow
from src.widgets.PopupWidget import PopupWidget
from src.package.Navigator import Navigator

class SettingsMenuView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.powerBtn.clicked.connect(self.on_power_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/mode_off_on_w.png')
        self.ui.powerBtn.setIcon(icon)
        self.ui.powerBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/question_mark_w.png')
        self.ui.helpBtn.setIcon(icon)
        self.ui.helpBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/description_w.png')
        self.ui.aboutBtn.setIcon(icon)
        self.ui.aboutBtn.setIconSize(QSize(40, 40))
        icon = QIcon('./src/resources/icons/settings_w.png')
        self.ui.settingsBtn.setIcon(icon)
        self.ui.settingsBtn.setIconSize(QSize(40, 40))

    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self)

    def on_power_clicked(self):
        def yes_callback():
            os.system("sudo poweroff")
        def no_callback():
            pass
        popup = PopupWidget(context=self.context, text="¿Quieres apagar el dispositivo?", yes_callback=yes_callback, no_callback=no_callback)
        popup.show()