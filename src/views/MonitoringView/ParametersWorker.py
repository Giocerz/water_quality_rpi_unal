
from PySide2.QtCore import QThread, Signal
import time
from w1thermsensor import W1ThermSensor
from src.logic.adcModule import ParametersVoltages
from src.logic.parametersCalc import ParametersCalculate
from src.logic.batteryLevel import BatteryProvider
from src.logic.filters import MovingAverageFilter

class ParametersMeasuredWorker(QThread):
    parameters_result = Signal(list)

    def __init__(self):
        super(ParametersMeasuredWorker, self).__init__()

    def run(self):
        self.running_state = True

        temperature_sensor = W1ThermSensor()
        parameters = ParametersVoltages()
        parameters_calc = ParametersCalculate()
        battery_provider = BatteryProvider()
        turb_filter = MovingAverageFilter(10)

        while self.running_state:
            try:
                temp = round(temperature_sensor.get_temperature(), 2)
                ph = round(parameters_calc.calculatePh(
                    parameters.ph_volt()), 2)
                do = round(parameters_calc.calculateDo(
                    parameters.oxygen_volt(), temp), 2)
                tds = round(parameters_calc.calculateTds(
                    temp, parameters.tds_volt()), 2)
                turb_voltage = turb_filter.add_value(parameters.turbidity_volt())
                turb = round(parameters_calc.calculateTurb(turb_voltage), 2)
                battery = battery_provider.getBatteryLevel()
                

                self.parameters_result.emit([temp, do, tds, ph, turb, battery])
                time.sleep(1)
            except Exception as e:
                print(e)

    def stop(self):
        self.running_state = False
        self.wait()
    