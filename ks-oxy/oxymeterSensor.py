from typing import Optional, Tuple
from oxymeterBase import OxymeterSensorBase
from oxymeterModel import Response, OxymeterResult, StatusResult, OxymeterConfig
from DFRobot_BloodOxygen_S import *
import time

class OxymeterSensor(OxymeterSensorBase):
    def begin(self, config: OxymeterConfig = OxymeterConfig()) -> Response:
        self.oxy = DFRobot_BloodOxygen_S_i2c(0x01, 0x57)
        self.config: OxymeterConfig = config
        return Response(status=StatusResult.success)

    def getDataRaw(self) -> Tuple[Response, Optional[OxymeterResult]]:
        self.oxy.get_heartbeat_SPO2()
        self.temp = self.oxy.get_temperature_c()
        self.spo = self.oxy.SPO2
        self.hr = self.oxy.heartbeat
        hasil = OxymeterResult(spo=self.spo, bpm=self.hr, temperature=self.temp)
        resp = Response(status=StatusResult.success)
        return resp, hasil

    def getData(self) -> Tuple[Response, Optional[OxymeterResult]]:
        resdata = self.getDataRaw()
        return resdata

hasilbang = OxymeterSensor()
hasilbang.begin()
oxy = DFRobot_BloodOxygen_S_i2c(0x01, 0x57)

while True:
    try:
        oxy.sensor_start_collect()
        response, resdata = hasilbang.getData()
        print("SPO:", resdata.spo, "BPM:", resdata.bpm, "Temp:", resdata.temperature)
        time.sleep(0.25)
        
    except KeyboardInterrupt:
        oxy.sensor_end_collect()
        print("Measurement Fisished !")
        break