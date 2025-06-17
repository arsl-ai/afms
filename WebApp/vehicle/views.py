from typing import List, Final, Sequence, Dict
from flask import render_template
from htmlmin.main import minify

from dto import Location, VehicleTracingDTO, VehicleDTO
from flask import Blueprint

from .models import Vehicle
from vehicle_tracking.vehicle_tracking_service import all_vehicles, current_location

vehicles_bp = Blueprint('vehicles', __name__, url_prefix='', static_folder="../static")

@vehicles_bp.route("/list_vehicles", methods=['GET'])
def list_vehicles():
    vehicles: Sequence[Vehicle] = all_vehicles()
    vehicle_tracking_ids: Final[List[str]] = list()
    vehicles_dict: Dict[str, VehicleDTO] = dict()

    for vehicle in vehicles:
        key: Final[str] = '||'.join([vehicle.VehicleID, vehicle.GPSID] )
        print(key)
        vehicle_tracking_ids.append(key)

        base_station = Location(
             latitude=vehicle.BaseLatitude,
             longitude=vehicle.BaseLongitude
        )
        vehicle_dto = VehicleDTO(
            baseStation=base_station
            ,make = vehicle.Make
            ,model = vehicle.Model
            ,vehicleId = vehicle.VehicleID
            ,gpsId = vehicle.GPSID
            ,name=vehicle.VehicleName
            ,vehicleRegistrationId=vehicle.VehicleRegistrationID    
        )
        
        curr_location = current_location(vehicle.GPSID, vehicle.VehicleID)
        locations: Dict[str, List[str]] = dict()
        locations[key] = curr_location

        vehicle_tracing_dto = VehicleTracingDTO(vehicle=vehicle_dto, locations=locations)
        vehicles_dict[key] = vehicle_tracing_dto

    return minify(
		render_template("list_vehicles.html", vehicle_tracking_ids = vehicle_tracking_ids , vehicles = vehicles_dict)
	)

@vehicles_bp.route("/add_vehicle", methods=['GET'])
def add_vehicle():
	return minify(render_template("add_vehicle.html"))