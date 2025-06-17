const track_my_vehicles = function (locations, google_map_id) {
    var map = new google.maps.Map(document.getElementById(google_map_id), {
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapId: google_map_id,
    });
    var infowindow = new google.maps.InfoWindow();
    var bounds = new google.maps.LatLngBounds();
    var marker, i;
    for (i = 0; i < locations.length; i++) {
        marker = new google.maps.marker.AdvancedMarkerElement({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: map
        });

        bounds.extend(marker.position);

        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                infowindow.setContent(locations[i][0]);
                infowindow.open(map, marker);
            }
        })(marker, i));
    }
    map.fitBounds(bounds);
}


const set_track_modal_heading = function (vehicle_name,  vehicle_tracking_modal_div_id) {
    // console.log(vehicle_tracking_modal_div_id)
    // console.log(vehicle_name)
    document.getElementById(vehicle_tracking_modal_div_id).getElementsByTagName('h3')[0].textContent = ['Tracking Vehicle', vehicle_name].join(':');
}

const track_my_vehicle = function (vehicle, locations, div_id, vehicle_tracking_id) {
    // console.log(vehicle_tracking_id)
    // console.log(vehicle)
    // console.log(locations[vehicle_tracking_id])

    var locations = [
                        ['Current Location', locations[vehicle_tracking_id][0], locations[vehicle_tracking_id][1]],
                        ['Home / Parked Location', vehicle.baseStation.latitude, vehicle.baseStation.longitude]
                    ];

    var map = new google.maps.Map(document.getElementById(div_id), {
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapId: div_id,
    });

    var infowindow = new google.maps.InfoWindow();
    var bounds = new google.maps.LatLngBounds();
    var marker, i;
    for (i = 0; i < locations.length; i++) {
        marker = new google.maps.marker.AdvancedMarkerElement({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: map
        });

        bounds.extend(marker.position);

        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                infowindow.setContent(locations[i][0]);
                infowindow.open(map, marker);
            }
        })(marker, i));
    }
    map.fitBounds(bounds);
}



