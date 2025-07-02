import time
import subprocess
from PySide2.QtCore import QThread, Signal

class LocationdWorker(QThread):
    location_result = Signal(list)

    def __init__(self):
        super(LocationdWorker, self).__init__()

    def run(self):
        self.running_state = True
        try:
            subprocess.run("sudo systemctl stop gpsd.socket", shell=True)
            time.sleep(0.5)
            subprocess.run(
                "sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock", shell=True)
            time.sleep(0.5)
            import gps
            session = gps.gps(mode=gps.WATCH_ENABLE)
        except:
            self.location_result.emit(['error'])
            self.running_state = False
        latitude: float = None
        longitude: float = None
        time_count = 0
        time_period = 2
        while self.running_state:
            try:
                if (time_count * time_period >= 60):
                    self.location_result.emit(['time'])
                report = session.next()

                if report['class'] == 'TPV':
                    if hasattr(report, 'lat') and hasattr(report, 'lon'):
                        latitude = float(report.lat)
                        longitude = float(report.lon)
                        self.location_result.emit([latitude, longitude])
                time.sleep(time_period)
                time_count += 1
            except Exception as e:
                self.location_result.emit(['error'])

    def stop(self):
        self.running_state = False
        self.wait()