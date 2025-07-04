from PySide2.QtWidgets import QMainWindow
from .ui.ui_ItRainedSection import Ui_MainWindow
from src.widgets.PopupWidget import PopupWidgetInfo
from src.package.Navigator import Navigator
from .LocationSectionView import FolderSectionView
from src.providers.SaveProvider import SaveProvider

class ItRainedSectionView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self._selected:str = None
        self.save_provider = SaveProvider()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.get_state()

        self.ui.nextBtn.clicked.connect(self.on_next_clicked)
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.yesCheckBox.clicked.connect(self._on_yes_clicked)
        self.ui.noCheckBox.clicked.connect(self._on_no_clicked)
        self.ui.idkCheckBox.clicked.connect(self._on_idk_clicked)

    def get_state(self):
        self._selected = self.save_provider.get_it_rained()
        if self._selected == 'Si':
            self.ui.yesCheckBox.setChecked(True)
            self.ui.noCheckBox.setChecked(False)
            self.ui.idkCheckBox.setChecked(False)
        elif self._selected == 'No':
            self.ui.yesCheckBox.setChecked(False)
            self.ui.noCheckBox.setChecked(True)
            self.ui.idkCheckBox.setChecked(False)
        elif self._selected == 'No lo sé':
            self.ui.yesCheckBox.setChecked(False)
            self.ui.noCheckBox.setChecked(False)
            self.ui.idkCheckBox.setChecked(True)
        else:
            self.ui.yesCheckBox.setChecked(False)
            self.ui.noCheckBox.setChecked(False)
            self.ui.idkCheckBox.setChecked(False)

    def _on_yes_clicked(self):
        self.ui.yesCheckBox.setChecked(True)
        self.ui.noCheckBox.setChecked(False)
        self.ui.idkCheckBox.setChecked(False)

    def _on_no_clicked(self):
        self.ui.yesCheckBox.setChecked(False)
        self.ui.noCheckBox.setChecked(True)
        self.ui.idkCheckBox.setChecked(False)

    def _on_idk_clicked(self):
        self.ui.yesCheckBox.setChecked(False)
        self.ui.noCheckBox.setChecked(False)
        self.ui.idkCheckBox.setChecked(True)

    def save_state(self):
        yes_state = self.ui.yesCheckBox.isChecked()
        no_state = self.ui.noCheckBox.isChecked()
        idk_state = self.ui.idkCheckBox.isChecked()
        if yes_state:
            text = 'Si'
        elif no_state:
            text = 'No'
        else:
            text = 'No lo sé'
        self._selected = text
        self.save_provider.set_it_rained(text)
    
    def on_back_clicked(self):
        prev_view = self.save_provider.get_prev_view()
        Navigator.pushReplacement(context=self.context, view=prev_view(context=self.context))

    def on_next_clicked(self):
        if self._selected is None:
            self.show_dialog_error('Marque una opción')
            return
        self.save_provider.set_prev_view(ItRainedSectionView)
        Navigator.pushReplacement(
            context=self.context, view=FolderSectionView(context=self.context))

    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()    


