from collections import defaultdict
from dataclasses import dataclass, field
from dataclass_wizard import JSONSerializable

json_dict = {
    "vehicle": {
        "vehicleRegistrationId": "",
        "make": "Toyota",
        "model": "2007 Cororlla",
        "baseStation": {
            "latitude": 7878.2323,
            "longitude": 2322.23232
        }
    },
    "tracking": {
        "devices":[
            "gpsDevice001"
        ]
    },
    "locations": {
        "gpsDevice001": [
            {
            "latitude": 7878.2323,
            "longitude": 2322.23232
            }
        ]
    }
}

json_str = """
{
    "vehicle": {
        "vehicleRegistrationId": "",
        "make": "Toyota",
        "model": "2007 Cororlla",
        "baseStation": {
            "latitude": 7878.2323,
            "longitude": 2322.23232
        }
    },
    "tracking": {
        "devices":[
            "gpsDevice001"
        ]
    },
    "locations": {
        "gpsDevice001": [
            {
            "latitude": 7878.2323,
            "longitude": 2322.23232
            }
        ]
    }
}
"""

@dataclass
class Location:
    latitude: float
    longitude: float


@dataclass
class VehicleDTO(JSONSerializable):
    vehicleId: str
    gpsId: str
    vehicleRegistrationId: str
    name: str
    make: str
    model: str
    baseStation:  Location

    # def to_json(self):
    #     return self.to_json()


@dataclass
class VehicleTracingDTO(JSONSerializable):
    vehicle: VehicleDTO
    locations: defaultdict[str, list[str]] = field(
        default_factory=lambda: defaultdict(list)
    )






