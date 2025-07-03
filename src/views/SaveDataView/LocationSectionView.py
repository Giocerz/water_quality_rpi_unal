from PySide2.QtWidgets import QMainWindow
from PySide2 import QtCore
from .ui.ui_LocationSection import Ui_MainWindow
from src.widgets.PopupWidget import PopupWidgetInfo
from src.package.Navigator import Navigator
from .LocationWorker import LocationdWorker
from src.widgets.PopupWidget import PopupWidgetInfo, LoadingPopupGPS
from .ManualGPSPopup import SetManualLocationWidget
from src.providers.SaveProvider import SaveProvider

class LocationSectionView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.save_provider = SaveProvider()

        self.location_worker = LocationdWorker()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.location_state()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.nextBtn.clicked.connect(self.on_next_clicked)
        self.ui.gpsBtn.clicked.connect(self.on_gps_clicked)
        self.ui.setManualLocationBtn.clicked.connect(self.on_set_manual_location_clicked)
        self.location_worker.location_result.connect(
            self.handle_location_result)
    
    def location_state(self):
        if self.save_provider.get_location() is not None:
            self.latitude = self.save_provider.get_location()['latitude']
            self.longitude = self.save_provider.get_location()['longitude']
            self.ui.label_4.setText(f'{self.latitude} , {self.longitude}')
            self.ui.label_4.setAlignment(QtCore.Qt.AlignCenter)

    def on_back_clicked(self):
        prev_view = self.save_provider.get_prev_view()
        Navigator.pushReplacement(context=self.context, view=prev_view(context=self.context))

    def on_next_clicked(self):
        pass

    def on_set_manual_location_clicked(self):
        manual_location_widget = SetManualLocationWidget(
            context=self.context, set_location=self.set_location)
        manual_location_widget.show()
        manual_location_widget.raise_()
        manual_location_widget.activateWindow()
    
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
        self.save_provider.set_location(latitude, longitude)

    def on_gps_clicked(self):
        self.loading_popup = LoadingPopupGPS(
            context=self.context, text='Localizando...', on_cancel=self.on_cancel_clicked)
        self.loading_popup.show()
        if not self.location_worker.isRunning():
            self.location_worker.start()
