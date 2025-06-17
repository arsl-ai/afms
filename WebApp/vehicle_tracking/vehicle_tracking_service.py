from sqlalchemy import desc, select
from vehicle.models import Vehicle
from tracking.models import GPSTable
from typing import List, Final


from sqlalchemy.orm      import scoped_session, sessionmaker
from sqlalchemy          import create_engine
from sqlalchemy.engine.url import URL
from settings import config

import traceback



connection_url = URL.create(
	drivername=config["DB_DRIVERNAME"],
	username=config['DB_USERNAME'],
	password=config['DB_PASSWORD'],
	host=config['DB_HOST'],
	port=config['DB_PORT'],
	database=config['DB_NAME'],
	query={
		"driver": config['DB_DRIVER'],
		"TrustServerCertificate": "no"
	})
# print(connection_url.render_as_string())

# Database and database session init
Session = None
try:
     engine = create_engine(connection_url.render_as_string(hide_password=False), echo=bool(config['DEBUG_MODE']))
     # engine.execution_options(stream_results=True)
     Session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
    )
except Exception as e:
	traceback.print_exc()

db_session = scoped_session(Session)


def all_vehicles():
    vehicles = db_session.scalars(select(Vehicle).order_by(desc(Vehicle.ProcessingTime))).all()
    # for vehicle in vehicles:
    #     print(vehicle.VehicleID)
    #     print(vehicle.GPSID)
    return vehicles


def current_location(gpsId: str, vehicleId: str):
    latest_tracking = db_session.query(GPSTable).filter(GPSTable.GPSID == gpsId, GPSTable.VehicleID == vehicleId).order_by(desc(GPSTable.ProcessingTime)).first()
    # print(latest_tracking)
    return [latest_tracking.Latitude, latest_tracking.Longitude]


def vehicles_current_location() -> List[List[str]]:
    vehicles =  all_vehicles()
    vehicles_current_location: Final[List[List[str]]] = list()
    for vehicle in vehicles:
           curr_location = current_location(vehicle.GPSID, vehicle.VehicleID)
           vehicle_current_location: Final[List[str]] = list()
           vehicle_current_location.append(vehicle.VehicleName)
           vehicle_current_location.extend(curr_location)
           vehicles_current_location.append(vehicle_current_location)
    # print(vehicles_current_location)
    return vehicles_current_location
     
