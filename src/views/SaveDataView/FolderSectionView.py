from PySide2.QtWidgets import QMainWindow, QStackedLayout, QVBoxLayout, QWidget, QGridLayout, QSizePolicy
from PySide2.QtCore import Qt
from .ui.ui_FolderSection import Ui_MainWindow
from src.widgets.KeyboardWidget import KeyboardWidget
from src.widgets.PopupWidget import PopupWidgetInfo, PopupWidget
from src.widgets.FolderWidget import FolderWidget
from .OriginSectionView import OriginSectionView
from src.model.SensorData import SensorData
from src.package.Navigator import Navigator
from src.providers.SaveProvider import SaveProvider
from src.model.Models import LoteModel, WaterQualityParams
from src.model.WaterQualityDB import WaterDataBase
from src.config import Constants
from datetime import datetime

class FolderSectionView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.folder_name: str = None
        self.folder_id: int = None
        self.folders_list: list[LoteModel] = []
        self.save_provider = SaveProvider()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.setup_list()
        self.current_index = 0
        self.folder_list_empty = False

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.backBtn_2.clicked.connect(self.on_back_clicked)

        self.ui.createBtn.clicked.connect()


        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)
        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

    def ui_components(self):
        self.keyboard = KeyboardWidget(self.ui.inputPlace)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)

        self.scrollBar = self.ui.scrollArea.verticalScrollBar()
        self.ui.verticalSlider.setRange(
            self.scrollBar.minimum(), self.scrollBar.maximum())
        self.ui.verticalSlider.hide()

        self.ui.stackedWidget.setCurrentIndex(self.current_index)
    
    def on_back_clicked(self):
        if self.current_index == 1 and not self.folder_list_empty:
            self.current_index = 0
            self.ui.stackedWidget.setCurrentIndex(self.current_index)
        else:
            prev_view = self.save_provider.get_prev_view()
            Navigator.pushReplacement(context=self.context, view=prev_view(context=self.context))
        
    def on_create_folder_clicked(self):
        if self.current_index == 0:
            self.current_index = 1
            self.ui.stackedWidget.setCurrentIndex(self.current_index)

    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()

    def load_data(self):
        self.folders_list = WaterDataBase.get_lotes()

    def on_push_folder_widget(self, id: int, name: str):
        self.folder_id = id
        self.folder_name = name

    def setup_list(self):
        self.load_data()

        if len(self.folders_list) == 0:
            self.current_index = 1
            self.ui.stackedWidget.setCurrentIndex(self.current_index)
            self.ui.verticalSlider.hide()
            self.folder_list_empty = True
            return

        # Crear el contenedor principal y el layout vertical
        container_widget = QWidget()
        main_layout = QVBoxLayout(container_widget)
        # Alinear contenido en la parte superior
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(10)

        # Crear el layout en cuadrícula
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        num_cols = 3  # Número de columnas
        for i, product in enumerate(self.folders_list):
            # Crear y configurar el widget
            product_widget = FolderWidget(
                id=product.id, name=product.name, description=product.description, on_push=self.on_push_folder_widget)
            product_widget.setFixedSize(133, 100)  # Fijar tamaño del widget
            product_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

            # Calcular la fila y columna
            row = i // num_cols
            col = i % num_cols

            # Establecer tamaño mínimo para filas y columnas
            grid_layout.setRowMinimumHeight(row, 100)
            grid_layout.setColumnMinimumWidth(col, 133)

            # Agregar el widget al layout
            grid_layout.addWidget(product_widget, row, col)

        self.total_rows = (len(self.folders_list) + num_cols - 1) // num_cols
        # Agregar el layout en cuadrícula al layout principal
        main_layout.addLayout(grid_layout)

        # Ajustar el contenedor dentro del ScrollArea
        self.ui.scrollArea.setWidget(container_widget)
        self.ui.scrollArea.setWidgetResizable(True)

    def slider_value_changed(self, value):
        self.scrollBar.setValue(value)

    def adjust_slider_range(self, minValue, maxValue): 
        if maxValue > minValue:  # Solo mostramos el slider si hay algo que desplazar
            self.ui.verticalSlider.show()
            self.ui.verticalSlider.setRange(minValue, maxValue)
            
            # Definir filas visibles en la UI
            visible_rows = 3.5  # Ajusta esto según la visibilidad real en la UI
            total_rows = self.total_rows

            if total_rows > visible_rows:
                step_size = max(1, round((maxValue - minValue) / (total_rows - visible_rows)))
            else:
                step_size = max(1, round((maxValue - minValue) / 3))  # Si hay pocas filas, usar un paso más grande
            
            self.ui.verticalSlider.setSingleStep(step_size)
            self.ui.verticalSlider.setPageStep(step_size * 2)  # Ajustar el desplazamiento por página
        else:
            self.ui.verticalSlider.hide()


    def scroll_value_changed(self, value):
        self.ui.verticalSlider.setValue(value)

    def validator(self) -> bool:
        if (not self.folder_name):
            self.show_dialog_error(error='Seleccione una carpeta')
            return False

    #Verify if a lote exist
    def verify_repeated_lote_name(self, name:str):
        name_lw = name.strip().lower()
        is_repeated = False
        for i in range(len(self.folders_list)):
            is_repeated = name_lw == self.folders_list[i].name.lower()
            if is_repeated:
                break
        return is_repeated
    """
    def on_save_clicked(self):        
        place = self.ui.inputPlace.text().strip()

        dtatetime_now = datetime.now()
        format_date = dtatetime_now.strftime("%Y-%m-%d")
        hour = dtatetime_now.strftime("%H:%M:%S")

        if self.folder_id:
            lote_id = self.folder_id
        else:
            lote = LoteModel(
                name=self.folder_name,
                creation_date=format_date,
                creation_hour=str(hour),
                last_add_date=format_date,
                last_add_hour=str(hour),
            )
            lote_id = WaterDataBase.insert_lote(lote)

        counter = 0
        for sample in self.capture_samples:
            sample_name = place if counter == 0 else f"{place} {counter}"
            params = WaterQualityParams(
                name=sample_name,
                device_id=Constants.DEVICE_ID,
                latitude=self.latitude,
                longitude=self.longitude,
                date=format_date,
                hour=str(hour),
                sample_origin=self.origin,
                it_rained=self.it_rained,
                upload_state=0,
                lote_id=lote_id,
                conductivity=sample.conductivity,
                oxygen=sample.oxygen,
                ph=sample.ph,
                temperature=sample.temperature,
                tds=sample.tds,
                turbidity=sample.turbidity,
                battery=sample.battery
            )
            WaterDataBase.insert_water_param(params)
            counter += 1

        message = "La muestra se guardó exitosamente" if len(self.capture_samples) == 1 else "Las muestras se guardaron exitosamente"
        self.close_monitoring_callback()
        finish_popup = PopupWidgetInfo(
            context=self.context, text=message, on_click=self.close_view, is_warning=False)
        finish_popup.show()
        """