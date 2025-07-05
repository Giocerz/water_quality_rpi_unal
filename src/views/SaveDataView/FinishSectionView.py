from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QPixmap
from .ui.ui_FinishSection import Ui_MainWindow
from src.package.Navigator import Navigator
from src.providers.SaveProvider import SaveProvider

class FinishSectionView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self._selected:str = None
        self.save_provider = SaveProvider()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.finishBtn.clicked.connect(self.on_next_clicked)

    def ui_components(self):
        pixmap = QPixmap('.src/resources/icons/check_circle_w.png')
        pixmap = pixmap.scaled(120, 120)
        self.ui.iconLbl.setPixmap(pixmap)

    def on_next_clicked(self):
        self.save_provider.clear()
        Navigator.pop(context=self.context, view=self)


