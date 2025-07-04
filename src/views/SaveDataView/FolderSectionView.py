from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt
from .ui.ui_FolderSection import Ui_MainWindow
from src.widgets.PopupWidget import PopupWidgetInfo
from src.package.Navigator import Navigator
from src.providers.SaveProvider import SaveProvider
from src.model.WaterQualityDB import WaterDataBase
from src.model.Models import LoteModel

class FolderSectionView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.save_provider = SaveProvider()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        
        self.set_list()

        #self.ui.nextBtn.clicked.connect(self.on_next_clicked)
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.folderList.clicked.connect(self.select_origin)
        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)
        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

    def ui_components(self):
        self.scrollBar = self.ui.folderList.verticalScrollBar()
        self.ui.verticalSlider.setRange(
            self.scrollBar.minimum(), self.scrollBar.maximum())
        self.ui.verticalSlider.hide()
    
    def on_back_clicked(self):
        prev_view = self.save_provider.get_prev_view()
        Navigator.pushReplacement(context=self.context, view=prev_view(context=self.context))

    def on_next_clicked(self):
        pass

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
        folder_name = self.folders_list[index].name
        self.ui.selectFolderLbl.setText(f'Carpeta: {folder_name}')


