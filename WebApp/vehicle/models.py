from settings import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import  String, DateTime, Float
from datetime import datetime
from typing import Optional

class Vehicle(Base):
    __tablename__ = "Vehicle"
    VehicleID: Mapped[str] = mapped_column(String(50), primary_key=True)
    GPSID: Mapped[str] = mapped_column(String(50))
    BaseLatitude: Mapped[float] = mapped_column(Float)
    BaseLongitude: Mapped[float] = mapped_column(Float)
    VehicleRegistrationID:  Mapped[str] = mapped_column(String(50))
    Make:Mapped[str] = mapped_column(String(50))
    Model: Mapped[str] = mapped_column(String(50))
    VehicleName: Mapped[str] = mapped_column(String(50))
    ProcessingTime:  Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False))
   
    # def __repr__(self) -> str:
    #     return self.VehicleName+' '+self.VehicleRegistrationID+ ' '+self.Make+' '+self.Model
