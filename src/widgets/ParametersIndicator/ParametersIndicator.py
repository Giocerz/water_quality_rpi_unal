from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from .ui_ParameterIndicatorS import Ui_Form as Ui_S
from .ui_ParameterIndicatorM import Ui_Form as Ui_M


class ParametersIndicator(QWidget):
    def __init__(self, name: str, unit: str, min_value: float = None, max_value: float = None,
                 lower_limit: float = None, upper_limit: float = None, significant_figures:int = 2, widget_size: str = 'S'):
        super().__init__()
        self.name: str = name
        self.unit: str = unit
        self.min_value: float = min_value if min_value is not None else 0.0
        self.max_value: float = max_value if max_value is not None else 100.0
        self.lower_limit: float = lower_limit if lower_limit is not None else -20000.0
        self.upper_limit: float = upper_limit if upper_limit is not None else 20000.0
        self.significant_figures: int = significant_figures
        self.widget_size: str = widget_size
        self.__setup_size()
        self.__ui_components()

    def __setup_size(self):
        if self.widget_size == 'S' or self.widget_size == 's':
            self.ui = Ui_S()
        elif self.widget_size == 'M' or self.widget_size == 'm':
            self.ui = Ui_M()
        else:
            self.ui = Ui_M()
        self.ui.setupUi(self)

    def __ui_components(self):
        self.ui.stableLbl.hide()
        self.ui.nameLbl.setText(self.name)
        self.ui.valueLbl.setText(f'---- {self.unit}',)
        self.ui.valueLbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        stable_pixmap = QPixmap('./src/resources/icons/balance_w.png')
        stable_pixmap = stable_pixmap.scaled(40, 40)
        self.ui.stableLbl.setPixmap(stable_pixmap)

    def __acond_value(self, value: float) -> int:
        result = 100.0 / (self.max_value - self.min_value) * \
            (value - self.min_value)
        result = int(result)
        if result < 0:
            result = 0
        elif result > 100:
            result = 100
        return result

    """
    def __verify_limits(self, value:float):
        if value < self.lower_limit or value > self.upper_limit:
            self.ui.warningLbl.show()
        else:
            self.ui.warningLbl.hide()
    """

    def sizeHint(self):
        return self.size()

    def setValue(self, value: float):
        if self.significant_figures == 0:
            rounded_value = int(round(value))
        else:
            rounded_value = round(value, self.significant_figures)
        self.ui.valueLbl.setText(f'{rounded_value} {self.unit}',)
        self.ui.valueLbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.progressBar.setValue(self.__acond_value(value))
        #self.__verify_limits(value)

    def setStable(self, is_stable: float):
        if is_stable:
            self.ui.stableLbl.show()
        else:
            self.ui.stableLbl.hide()
