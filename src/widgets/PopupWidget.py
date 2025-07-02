from PySide2.QtWidgets import QGraphicsOpacityEffect, QWidget
from PySide2.QtGui import QPixmap
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from .ui.ui_PopupWidget import Ui_Form as Ui_Popup
from src.views.ui_LoadingPopupWidget import Ui_Form as Ui_Loading
from src.views.ui_ProgressPopupWidget import Ui_Form as Ui_Progress
from .ui.ui_LoadingPopupFullpageLandscape import Ui_Form as Ui_FullpageLoadingLandS
from .ui.ui_LoadingPopupGPS import Ui_Form as Ui_LoadingGPS
from src.package.Timer import Timer


class PopupWidget(QWidget):
    def __init__(self, context, yes_callback, no_callback, text):
        super().__init__()
        self.context = context
        self.ui = Ui_Popup()
        self.ui.setupUi(self)

        self.yes_callback = yes_callback
        self.no_callback = no_callback

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.5)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)
        pixmap = QPixmap('./src/resources/icons/warning.png')
        pixmap = pixmap.scaled(61,61)
        self.ui.IconInfo.setPixmap(pixmap)

        self.ui.si.clicked.connect(self.yes_clicked)
        self.ui.no.clicked.connect(self.no_clicked)
        self.ui.lblOpacity.mousePressEvent = self.handle_click
        self.setParent(self.context)

    def yes_clicked(self):
        if self.yes_callback:
            self.yes_callback()
        self.close_and_delete()

    def no_clicked(self):
        if self.no_callback:
            self.no_callback()
        self.close_and_delete()
    
    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()
    
    def handle_click(self, event):
        self.close_and_delete()


class PopupWidgetInfo(QWidget):
    def __init__(self, context, text:str, button:bool = True, on_click:callable = None, is_warning:bool = True ):
        super().__init__()
        self.context = context
        self.on_click:callable = on_click
        self.__is_warning:bool = is_warning
        self.ui = Ui_Popup()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)
        if self.__is_warning:
            pixmap = QPixmap('./src/resources/icons/warning.png')
        else:
            pixmap = QPixmap('./src/resources/icons/check_circle.png')
        pixmap = pixmap.scaled(61,61)
        self.ui.IconInfo.setPixmap(pixmap)

        self.ui.si.hide()
        self.ui.no.hide()
        if(button):
            self.ui.no.show()
            self.ui.no.setText('OK')
            self.ui.lblOpacity.mousePressEvent = self.handle_click

        self.ui.no.clicked.connect(self.ok_clicked)
        self.setParent(self.context)


    def ok_clicked(self):
        if self.on_click:
            self.on_click()
        self.close_and_delete()
    
    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()
    
    def handle_click(self, event):
        self.close_and_delete()

class LoadingPopupWidget(QWidget):
    def __init__(self, context, text):
        super().__init__()
        self.context = context
        self.ui = Ui_Loading()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)

        self.rotation_step = 0
        self.timer = Timer.periodic(duration= 300, callback= self.update_border_style)
        self.timer.start()

        self.setParent(self.context)
    
    def update_border_style(self):
        border_styles = [
            "border-top: 5px solid #00007f;",  # Azul arriba
            "border-right: 5px solid #00007f;",  # Azul derecha
            "border-bottom: 6px solid #00007f;",  # Azul abajo
            "border-left: 6px solid #00007f;",  # Azul izquierda
        ]
        # Actualizar el estilo según el paso actual de la rotación
        current_border = border_styles[self.rotation_step % 4]
        # Estilo general del widget
        self.ui.IconInfo.setStyleSheet(f"""
                border: 6px solid #ced4da;
                border-radius: 30px;
                {current_border}
        """)
        self.rotation_step += 1
        

    def close_and_delete(self):
        self.timer.cancel()
        self.setParent(None)
        self.deleteLater()

class LoadingPopupGPS(QWidget):
    def __init__(self, context, text):
        super().__init__()
        self.context = context
        self.ui = Ui_LoadingGPS()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.LabelInfo.setText(text)

        self.toggle = True
        self.time_count = 0
        pixmap = QPixmap('./src/resources/icons/satellite_w.png')
        pixmap = pixmap.scaled(81,81)
        self.ui.satelliteLbl.setPixmap(pixmap)
        self.timer = Timer.periodic(duration= 300, callback= self.update_toggle)
        self.timer.start()

        self.setParent(self.context)
    
    def update_toggle(self):
        self.time_count += 1
        if self.time_count >= 50: 
            self.ui.LabelInfo.setText('Esto esta tomando mucho tiempo...')
        if self.toggle:
            pixmap = QPixmap('./src/resources/icons/satellite_w_nosignal.png')
            pixmap = pixmap.scaled(81,81)
            self.ui.satelliteLbl.setPixmap(pixmap)
            self.toggle = False
        else:
            pixmap = QPixmap('./src/resources/icons/satellite_w.png')
            pixmap = pixmap.scaled(81,81)
            self.ui.satelliteLbl.setPixmap(pixmap)
            self.toggle = True
        
    def close_and_delete(self):
        self.timer.cancel()
        self.setParent(None)
        self.deleteLater()

class FullpageLoadingPopup(QWidget):
    def __init__(self, context, text):
        super().__init__()
        self.context = context
        self.ui = Ui_FullpageLoadingLandS()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.LabelInfo.setText(text)
        self.setParent(self.context)

        # Guardar los círculos en una lista
        self.circles = [
            self.ui.firstCircle,
            self.ui.secondCircle,
            self.ui.thirdCircle
        ]

        # Guardar sus posiciones originales
        self.original_positions = [circle.pos() for circle in self.circles]

        # Crear la animación
        self.create_animation()

    def create_animation(self):
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.setLoopCount(-1)  # Infinita

        for circle, pos in zip(self.circles, self.original_positions):
            up = QPropertyAnimation(circle, b"pos")
            up.setDuration(300)
            up.setStartValue(pos)
            up.setEndValue(pos - QtCore.QPoint(0, 15))  # Subir 15px

            down = QPropertyAnimation(circle, b"pos")
            down.setDuration(300)
            down.setStartValue(pos - QtCore.QPoint(0, 15))
            down.setEndValue(pos)

            bounce = QSequentialAnimationGroup()
            bounce.addAnimation(up)
            bounce.addAnimation(down)

            self.anim_group.addAnimation(bounce)

        self.anim_group.start()

    def close_and_delete(self):
        self.anim_group.stop()
        self.setParent(None)
        self.deleteLater()

class ProgressPopupWidget(QWidget):
    def __init__(self, context, text):
        super().__init__()
        self.context = context
        self.ui = Ui_Progress()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.2)
        self.ui.lblOpacity.setGraphicsEffect(self.opacity)
        self.ui.LabelInfo.setText(text)
        self.ui.LabelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.progressBar.setValue(0)

        self.setParent(self.context)
    
    def set_value(self, value:int):
        self.ui.progressBar.setValue(value)
        
    def close_and_delete(self):
        self.setParent(None)
        self.deleteLater()