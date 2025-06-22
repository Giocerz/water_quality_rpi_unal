from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon
from src.views.ui_SaveSelect import Ui_MainWindow
from src.views.SaveDataView.SaveDataView import SaveDataView
from src.views.GraphView.GraphView import GraphPreviewView
from src.package.Navigator import Navigator
from src.model.SensorData import SensorData
from src.logic.AppConstans import AppConstants
from typing import Optional

class SaveSelectView(QMainWindow):
    def __init__(self, context, capture_samples: list[SensorData], close_monitoring_callback:callable):
        super().__init__()
        self.context = context
        self.capture_samples : list[SensorData] = capture_samples
        self.close_monitoring_callback:callable = close_monitoring_callback

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.allCheckBox.mousePressEvent = self.on_press_all_checkbox
        self.ui.meanCheckBox.mousePressEvent = self.on_pres_mean_checkbox
        self.ui.continueBtn.clicked.connect(self.on_continue_clicked)
        self.ui.openGraphBtn.clicked.connect(self.on_open_graph_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.ui.continueBtn.hide()
        self.averaged_samples: SensorData = self.calculate_average()

        text = f"Temp: {self.averaged_samples.temperature}"

        if self.averaged_samples.oxygen is not None and self.averaged_samples.oxygen != AppConstants.MEASURE_OFF_VALUE:
            text += f", OD: {self.averaged_samples.oxygen}"

        if self.averaged_samples.tds is not None and self.averaged_samples.tds != AppConstants.MEASURE_OFF_VALUE:
            text += f", TDS: {self.averaged_samples.tds}"

        if self.averaged_samples.conductivity is not None and self.averaged_samples.conductivity != AppConstants.MEASURE_OFF_VALUE:
            text += f", CE: {self.averaged_samples.conductivity}"

        if self.averaged_samples.ph is not None and self.averaged_samples.ph != AppConstants.MEASURE_OFF_VALUE:
            text += f", pH: {self.averaged_samples.ph}"

        if self.averaged_samples.turbidity is not None and self.averaged_samples.turbidity != AppConstants.MEASURE_OFF_VALUE:
            text += f", Turb: {self.averaged_samples.turbidity}"

        self.ui.meanLbl.setText(text)
        self.ui.meanLbl.setAlignment(Qt.AlignCenter)
        self.ui.allLbl.setText(F'Total de muestras: {len(self.capture_samples)}')
        self.ui.allCheckBox.setChecked(True)
        self.ui.meanCheckBox.setChecked(False)
        self.ui.continueBtn.show()
    
    def on_back_clicked(self):
        Navigator.pop(context=self.context, view=self)

    def on_open_graph_clicked(self):
        Navigator.push(context=self.context, view=GraphPreviewView(context=self.context, sensor_data_list=self.capture_samples))

    def on_press_all_checkbox(self, event):
        """ Maneja el evento de clic en allCheckBox, desmarcando meanCheckBox si es necesario. """
        if self.ui.allCheckBox.isChecked():
            self.ui.allCheckBox.setChecked(False)
        else:
            self.ui.allCheckBox.setChecked(True)
            self.ui.meanCheckBox.setChecked(False)  # Desmarca el otro checkbox

    def on_pres_mean_checkbox(self, event):
        """ Maneja el evento de clic en meanCheckBox, desmarcando allCheckBox si es necesario. """
        if self.ui.meanCheckBox.isChecked():
            self.ui.meanCheckBox.setChecked(False)
        else:
            self.ui.meanCheckBox.setChecked(True)
            self.ui.allCheckBox.setChecked(False)  # Desmarca el otro checkbox

    def on_continue_clicked(self):
        if self.ui.allCheckBox.isChecked():
            view =  SaveDataView(context= self.context, capture_samples=self.capture_samples, close_monitoring_callback=self.close_monitoring_callback)
        else:
            view =  SaveDataView(context= self.context, capture_samples=[self.averaged_samples], close_monitoring_callback=self.close_monitoring_callback)
        Navigator.pushReplacement(context=self.context, view=view)

    def calculate_average(self) -> SensorData:
        """ Calcula el promedio de cada parámetro en capture_samples, ignorando valores None """
        def average(values: list[Optional[float]]) -> Optional[float]:
            if values[0] is None:  # Solo verifica el primer elemento
                return None
            valid_values = [v for v in values if v is not None]
            return round(sum(valid_values) / len(valid_values) , 2) if valid_values else None

        return SensorData(
            temperature=average([sample.temperature for sample in self.capture_samples]),
            ph=average([sample.ph for sample in self.capture_samples]),
            tds=average([sample.tds for sample in self.capture_samples]),
            conductivity=average([sample.conductivity for sample in self.capture_samples]),
            oxygen=average([sample.oxygen for sample in self.capture_samples]),
            turbidity=average([sample.turbidity for sample in self.capture_samples]),
            battery=average([sample.battery for sample in self.capture_samples])
        )
