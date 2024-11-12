from pydantic import BaseModel


class QixiangBase(BaseModel):
    port: int
    WindSpeed: str
    Direction: str
    AirPressure: str
    Humidity: str
    Lighting: str
    Temperature: str
    Rainfall: str
    time: str

class EntropyBase(BaseModel):
    port: int
    Water: str
    Temperature: str
    ElectricalConductivity: str
    PH: str
    time: str

class User(BaseModel):
    name: str
    password: str
