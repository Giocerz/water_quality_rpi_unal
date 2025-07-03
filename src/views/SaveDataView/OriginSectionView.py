from PySide2.QtWidgets import QMainWindow, QStackedLayout
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt
from .ui.ui_OriginSection import Ui_MainWindow
from src.widgets.PopupWidget import PopupWidgetInfo
from src.package.Navigator import Navigator
from src.logic.AppConstans import AppConstants
from .LocationSectionView import LocationSectionView
from src.providers.SaveProvider import SaveProvider

class OriginSectionView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.save_provider = SaveProvider()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.set_list()

        self.ui.nextBtn.clicked.connect(self.on_next_clicked)
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.originList.clicked.connect(self.select_origin)
        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)
        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

    def ui_components(self):
        self.scrollBar = self.ui.originList.verticalScrollBar()
        self.ui.verticalSlider.setRange(
            self.scrollBar.minimum(), self.scrollBar.maximum())
        self.ui.verticalSlider.hide()
        if self.save_provider.get_origin() is not None:
            self.ui.originList.setCurrentIndex(
                self.model.index(self.save_provider.get_origin(), 0))

    def get_origin_state(self):
        if self.save_provider.get_origin() is not None:
            self.ui.selectOriginLbl.setText(
                f'Origen: {self.save_provider.get_origin()}')
    
    def on_back_clicked(self):
        print('on_back_clicked')
        # If the previous view is a NameSectionView
        prev_view = self.save_provider.get_prev_view()
        Navigator.pushReplacement(context=self.context, view=prev_view(context=self.context))

    def on_next_clicked(self):
        self.save_provider.set_prev_view(OriginSectionView)
        Navigator.pushReplacement(
            context=self.context, view=LocationSectionView(context=self.context))

    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()    
    
    def set_list(self):
        self.model = QStandardItemModel()
        for origin in AppConstants.WATER_SOURCES:
            standard_item = QStandardItem(origin)
            standard_item.setFlags(standard_item.flags() & ~Qt.ItemIsEditable)
            self.model.appendRow(standard_item)
        self.ui.originList.setModel(self.model)

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

    #FUNCIONES PARA SELECCIONAR ORIGEN
    def select_origin(self):
        indexes = self.ui.originList.selectedIndexes()
        index = indexes[0].row()
        origin = AppConstants.WATER_SOURCES[index]
        if origin != 'Otro':
            pass
        self.save_provider.set_origin(origin)
        self.ui.selectOriginLbl.setText(f'Origen: {origin}')


