from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from database import Base
import enum

class StatusEnum(str, enum.Enum):
    LAGER = "LAGER"
    RESERVIERT = "RESERVIERT"
    BETANKUNG = "BETANKUNG"
    VERSENDET = "VERSENDET"
    FEHLER = "FEHLER"
    ABGESCHLOSSEN = "ABGESCHLOSSEN"

class ModelEnum(str, enum.Enum):
    Notebook = "Notebook"
    MFF = "MFF"
    AllInOne = "AllInOne"
#    Scanner = "Scanner"
#    Drucker = "Drucker"
#    Multifunktionsdrucker = "Multifunktionsdrucker"
#    Zufuhrfach = "Zufuhrfach"
#    iPhone = "iPhone"
    Backpack = "Backpack"
    Dockingstation = "Dockingstation"
    Monitor = "Monitor"

class Hardware(Base):
    __tablename__ = "hardware"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(255))
    mac = Column(String(255), nullable=True)
    ip = Column(String(255), nullable=True)
    ticket = Column(String(255), nullable=True)
    uuid = Column(String(255), nullable=True)
    zentrum = Column(String(255), nullable=True)
    seriennumber = Column(String(255))

    model = Column(Enum(ModelEnum, native_enum=False))  # ✅ Das ist wichtig
    status = Column(Enum(StatusEnum, native_enum=False))  # ✅ Ebenfalls wichtig

    enduser = Column(String(255), nullable=True)
    admin = Column(String(255))
    comment = Column(String(1000), nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
