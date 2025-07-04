from PySide2.QtWidgets import QMainWindow,QStackedLayout
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt
from .ui.ui_FolderSection import Ui_MainWindow
from src.widgets.PopupWidget import PopupWidgetInfo
from .FinishSectionView import FinishSectionView
from src.package.Navigator import Navigator
from src.providers.SaveProvider import SaveProvider, SaveProviderParamsModel
from src.model.WaterQualityDB import WaterDataBase, WaterQualityParams
from src.model.Models import LoteModel
from src.widgets.KeyboardWidget import KeyboardWidget
from src.config.Constants import Constants
from datetime import datetime as Datetime

class FolderSectionView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.current_index = 0
        self.selected_folder:LoteModel = None
        self.save_provider = SaveProvider()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        
        self.set_list()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.backBtn_2.clicked.connect(self.on_back_clicked)
        self.ui.saveBtn.clicked.connect(self.on_push_save)
        self.ui.saveBtn_2.clicked.connect(self.on_push_save)
        self.ui.createBtn.clicked.connect(self.on_create_folder_clicked)
        self.ui.folderList.clicked.connect(self.select_folder)
        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)
        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

    def ui_components(self):
        self.scrollBar = self.ui.folderList.verticalScrollBar()
        self.ui.verticalSlider.setRange(
            self.scrollBar.minimum(), self.scrollBar.maximum())
        self.ui.verticalSlider.hide()
        self.keyboard = KeyboardWidget(self.ui.inputPlace)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)
    
    def on_back_clicked(self):
        if self.current_index == 1 and len(self.folders_list) > 0:
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
        self.folders_list:list[LoteModel] = WaterDataBase.get_lotes()

    def set_list(self):
        self.load_data()
        if len(self.folders_list) == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        self.model = QStandardItemModel()
        for folder in self.folders_list:
            standard_item = QStandardItem(folder.name)
            standard_item.setFlags(standard_item.flags() & ~Qt.ItemIsEditable)
            self.model.appendRow(standard_item)
        self.ui.folderList.setModel(self.model)

    def slider_value_changed(self, value):
        self.scrollBar.setValue(value)

    def adjust_slider_range(self, min, max):
        self.ui.verticalSlider.show()
        self.ui.verticalSlider.setRange(min, max)

    def scroll_value_changed(self, value):
        self.ui.verticalSlider.setValue(value)
    
    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()

    def select_folder(self):
        "Selects the folder from the list and updates the save provider with the selected origin."
        indexes = self.ui.folderList.selectedIndexes()
        index = indexes[0].row()
        self.selected_folder = self.folders_list[index]
        folder_name = self.selected_folder.name
        self.ui.selectFolderLbl.setText(f'Carpeta: {folder_name}')

    #Validators
    def verify_repeated_lote_name(self, name:str):
        name_lw = name.strip().lower()
        is_repeated = False
        for i in range(len(self.folders_list)):
            is_repeated = name_lw == self.folders_list[i].name.lower()
            if is_repeated:
                break
        return is_repeated
    
    def validator(self) -> bool:
        if self.current_index == 1:
            if not self.ui.inputPlace.text().strip:
                self.show_dialog_error(error='Seleccione una carpeta')
                return False
            if self.verify_repeated_lote_name(self.ui.inputPlace.text()):
                self.show_dialog_error(error='Ya existe una carpeta con ese nombre')
                return False
        else:
            if self.selected_folder is None:
                self.show_dialog_error(error='Seleccione una carpeta')
                return False
        return True
    
    def on_push_save(self):
        if not self.validator():
            return
        if self.current_index == 0:
            self.folder_id = self.selected_folder.id
        else:
            dtatetime_now = Datetime.now()
            format_date = dtatetime_now.strftime("%Y-%m-%d")
            hour = dtatetime_now.strftime("%H:%M:%S")

            lote = LoteModel(
                    name=self.ui.inputPlace.text().strip(),
                    creation_date=format_date,
                    creation_hour=str(hour),
                    last_add_date=format_date,
                    last_add_hour=str(hour),
                )
            self.folder_id = WaterDataBase.insert_lote(lote)

    def save_data(self):
        try:
            parameters:SaveProviderParamsModel = self.save_provider.get_parameters_lists()
            sample_name = self.save_provider.get_sample_name()
            origin = self.save_provider.get_origin()
            location = self.save_provider.get_location()
            it_rained = self.save_provider.get_it_rained()
            latitude = location['latitude']
            longitude = location['longitude']

            for index in range(len(parameters.timestamp_list)):
                name = sample_name if index == 0 else f"{sample_name} {index + 1}"
                date = parameters.timestamp_list[index].split(" ")[0]
                hour = parameters.timestamp_list[index].split(" ")[1]
                params = WaterQualityParams(
                    name=name,
                    device_id=Constants.DEVICE_ID,
                    latitude=latitude,
                    longitude=longitude,
                    date=date,
                    hour=hour,
                    sample_origin=origin,
                    it_rained=it_rained,
                    upload_state=0,
                    lote_id=self.folder_id,
                    conductivity=parameters.conductivity_list[index],
                    oxygen=parameters.oxygen_list[index],
                    ph=parameters.ph_list[index],
                    temperature=parameters.temperature_list[index],
                    tds=parameters.tds_list[index],
                    turbidity=-1000,
                    battery=parameters.battery_list[index],
                )
                WaterDataBase.insert_water_param(params)
                counter += 1
        except:
            self.show_dialog_error('Error al guardar los datos')
            return
        Navigator.pushReplacement(
            context=self.context,
            view=FinishSectionView(context=self.context)
        )
        
    
