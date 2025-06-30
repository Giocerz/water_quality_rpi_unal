from PySide2.QtCore import QThread, Signal
import time
import random

class FakeParametersMeasuredWorker(QThread):
    parameters_result = Signal(list)

    def __init__(self):
        super(FakeParametersMeasuredWorker, self).__init__()

    def run(self):
        self.running_state = True

        while self.running_state:
            try:
                # Valores aleatorios realistas
                temp = round(random.uniform(10.0, 35.0), 2)      # Temperatura en °C
                ph = round(random.uniform(6.0, 8.5), 2)           # pH
                do = round(random.uniform(5.0, 10.0), 2)          # Oxígeno disuelto (mg/L)
                tds = round(random.uniform(100, 1200), 2)         # TDS (ppm)
                turb = round(random.uniform(0.1, 5.0), 2)         # Turbidez (NTU)
                battery = round(random.uniform(20.0, 100.0), 2)   # Nivel batería (%)

                self.parameters_result.emit([temp, do, tds, ph, turb, battery])
                time.sleep(1)
            except Exception as e:
                print(e)

    def stop(self):
        self.running_state = False
        self.wait()
