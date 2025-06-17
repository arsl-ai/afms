from settings import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import  String, Double, DateTime
from datetime import datetime
from typing import Optional


class GPSTable(Base):
    __tablename__ = "GPSTable"
    GPSID: Mapped[str] = mapped_column(String(50), primary_key=True)
    VehicleID: Mapped[str] = mapped_column(String(50))
    Latitude: Mapped[float] = mapped_column(Double)
    Longitude: Mapped[float] 
    Timestamp: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False))
    ProcessingTime:  Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False))
   
    # def __repr__(self) -> str:
    #     return GPSTable.
