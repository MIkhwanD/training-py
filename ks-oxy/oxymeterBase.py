from oxymeterModel import OxymeterResult,Response, OxymeterConfig
from abc import ABC, abstractmethod
from typing import Optional, Tuple

class OxymeterSensorBase(ABC):
    @abstractmethod
    def begin(self, config:OxymeterConfig = OxymeterConfig())->Response:
        pass

    @abstractmethod
    def getDataRaw(self)->Tuple[Response,Optional[OxymeterResult]]:
        pass

    @abstractmethod
    def getData(self)->Tuple[Response,Optional[OxymeterResult]]:
        pass