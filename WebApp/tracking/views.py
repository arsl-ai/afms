from flask import render_template, Blueprint
from htmlmin.main import minify
from typing import Final, List

from vehicle_tracking.vehicle_tracking_service import vehicles_current_location


tracking_bp = Blueprint('tracking', __name__, url_prefix='', static_folder="../static")

@tracking_bp.route("/track_vehicles", methods=['GET'])
def track_vehicles():
    vehicles_current_locations: Final[List[List[str]]] = vehicles_current_location()
    print(vehicles_current_locations)
    return minify(
			render_template(
				"track_vehicles.html"
				, locations= vehicles_current_locations
		)
	)