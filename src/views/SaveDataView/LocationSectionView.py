from PySide2.QtWidgets import QMainWindow, QStackedLayout
from PySide2 import QtCore
from .ui.ui_LocationSection import Ui_MainWindow
from src.widgets.KeyboardWidget import KeyboardWidget
from src.widgets.PopupWidget import PopupWidgetInfo
from src.package.Navigator import Navigator
from .LocationWorker import LocationdWorker
from src.widgets.PopupWidget import PopupWidgetInfo, LoadingPopupGPS

class LocationSectionView(QMainWindow):
    def __init__(self, context, previous_view):
        QMainWindow.__init__(self)
        self.context = context
        self.previous_view = previous_view

        self.location_worker = LocationdWorker()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.nextBtn.clicked.connect(self.on_next_clicked)
        self.ui.gpsBtn.clicked.connect(self.on_gps_clicked)
        self.location_worker.location_result.connect(
            self.handle_location_result)
    
    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self.previous_view(context=self.context))

    def on_next_clicked(self):
        pass
    
    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()

    def on_cancel_clicked(self):
        self.location_worker.stop()
        self.loading_popup.close_and_delete()
        self.show_dialog_error('Localización cancelada.')

    def handle_location_result(self, location):
        self.location_worker.stop()
        self.loading_popup.close_and_delete()
        if (len(location) == 1):
            if (location[0] == 'error'):
                self.show_dialog_error('Error al intentar localizar.')
                return
            elif (location[0] == 'time'):
                self.show_dialog_error(
                    'Tiempo de espera de<br>localización expirado.')
                return
        self.set_location(location[0], location[1])
        self.show_dialog_error('Localización completada.')
    
    def set_location(self, latitude:float, longitude:float):
        self.latitude = latitude
        self.longitude = longitude
        self.ui.label_4.setText(f'{self.latitude} , {self.longitude}')
        self.ui.label_4.setAlignment(QtCore.Qt.AlignCenter)

    def on_gps_clicked(self):
        self.loading_popup = LoadingPopupGPS(
            context=self.context, text='Localizando...', on_cancel=self.on_cancel_clicked)
        self.loading_popup.show()
        if not self.location_worker.isRunning():
            self.location_worker.start()
