from PySide2.QtWidgets import QMainWindow, QStackedLayout, QVBoxLayout, QWidget, QGridLayout, QSizePolicy
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon
from .ui.ui_FolderSection import Ui_MainWindow
from src.widgets.KeyboardWidget import KeyboardWidget
from src.widgets.PopupWidget import PopupWidgetInfo
from src.widgets.FolderWidget import FolderWidget
from src.package.Navigator import Navigator
from src.providers.SaveProvider import SaveProvider
from src.model.Models import LoteModel
from src.model.WaterQualityDB import WaterDataBase


class FolderSectionView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.current_index = 0
        self.selected_folder_widget: FolderWidget = None
        self.folder_list_empty = False
        self.folder_name: str = None
        self.folder_id: int = None
        self.folders_list: list[LoteModel] = []
        self.save_provider = SaveProvider()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.setup_list()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.backBtn_2.clicked.connect(self.on_back_clicked)
        
        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)

        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.scrollBar = self.ui.scrollArea.verticalScrollBar()
        self.ui.verticalSlider.setRange(self.scrollBar.minimum(), self.scrollBar.maximum())
        self.ui.verticalSlider.hide()

    def load_data(self):
        self.folders_list = WaterDataBase.get_lotes()
    
    def setup_list(self):
        self.load_data()

        if len(self.folders_list) == 0:
            self.current_index = 1
            self.ui.stackedWidget.setCurrentIndex(self.current_index)
            self.folder_list_empty = True
            self.ui.verticalSlider.hide()
            self.ui.scrollArea.hide()
            return

        # Crear el contenedor principal y el layout vertical
        container_widget = QWidget()
        main_layout = QVBoxLayout(container_widget)
        main_layout.setAlignment(Qt.AlignTop)  # Alinear contenido en la parte superior
        main_layout.setSpacing(10)

        # Crear el layout en cuadrícula
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        num_cols = 3  # Número de columnas
        for i, folder in enumerate(self.folders_list):
            # Crear y configurar el widget
            product_widget = FolderWidget(id=folder.id, name=folder.name, description=folder.description, on_push=self.on_push_folder_widget)
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
        self.ui.uploadBtn.show()


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
    

    def on_push_folder_widget(self, folder_widget: FolderWidget):
        pass
    
    
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

    """
    def on_push_folder_widget(self, folder_widget: FolderWidget):
        self.folder_id = folder_widget.id
        self.folder_name = folder_widget.name

        # Oculta el "label de selección" del anterior si existe
        if self.selected_folder_widget and self.selected_folder_widget != folder_widget:
            self.selected_folder_widget.set_selected(False)

        folder_widget.set_selected(True)

        # Guardar el nuevo seleccionado
        self.selected_folder_widget = folder_widget
    """
    

    """
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