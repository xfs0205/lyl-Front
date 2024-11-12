from sqlalchemy import  Column,  Integer, String
from sql_app.database.database import engine, Base

class Qixiang(Base):
    __tablename__ = "Weather"

    id = Column(Integer, primary_key=True)
    port = Column(Integer)
    WindSpeed = Column(String(255))
    Direction = Column(String(255))
    AirPressure = Column(String(255))
    Humidity = Column(String(255))
    Lighting = Column(String(255))
    Temperature = Column(String(255))
    Rainfall = Column(String(255))
    time = Column(String(255))


class Entropy(Base):
    __tablename__ = "Entropy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    port = Column(Integer, nullable=False)
    Water = Column(String(255), nullable=False)
    Temperature = Column(String(255), nullable=False)
    ElectricalConductivity = Column(String(255), nullable=False)
    PH = Column(String(255), nullable=False)
    time = Column(String(255), nullable=False)


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    power = Column(String(255), nullable=False)
