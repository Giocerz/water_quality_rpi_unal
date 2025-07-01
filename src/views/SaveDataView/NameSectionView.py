from PySide2.QtWidgets import QMainWindow, QStackedLayout
from .ui.ui_NameSection import Ui_MainWindow
from src.widgets.KeyboardWidget import KeyboardWidget
from src.widgets.PopupWidget import PopupWidgetInfo
from .OriginSectionView import OriginSectionView
from src.model.SensorData import SensorData
from src.package.Navigator import Navigator

class NameSectionView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.nextBtn.clicked.connect(self.on_next_clicked)

    def ui_components(self):
        self.keyboard = KeyboardWidget(self.ui.inputPlace)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)
    
    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self)

    def on_next_clicked(self):
        if not self.validator():
            return
        Navigator.pushReplacement(
            context=self.context,
            view=OriginSectionView(context=self.context)
        )

    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()
    
    def validator(self) -> bool:
        """Validates the input data for the place name"""
        place = self.ui.inputPlace.text().strip()
        if (place == ''):
            self.show_dialog_error(error='Ingrese un nombre válido')
            return False
        if not place.replace(" ", "").isalnum():
            self.show_dialog_error(error='El nombre no puede tener<br>carácteres especiales')
            return False
        return True
