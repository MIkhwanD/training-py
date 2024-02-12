from pydantic import BaseModel
from enum import Enum
from typing import Optional

class OxymeterResult(BaseModel):
    spo:float
    bpm:float
    temperature:float

class StatusResult(Enum):
    success, failed, error, missing=range(4)

class Response(BaseModel):
    status:StatusResult
    message:Optional[str] = None

class OxymeterConfig(BaseModel):
    offsetSPO:float=0.0
    offsetBPM:float=0.0
    offsetTemperature:float=0.0