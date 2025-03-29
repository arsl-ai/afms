// Initialize the map
const map = L.map('map').setView([17.6868, 83.2185], 10);

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let vehicleData = [];

// Function to read Excel file and populate data
function readExcel(file) {
    const reader = new FileReader();
    reader.onload = function(event) {
        const data = new Uint8Array(event.target.result);
        const workbook = XLSX.read(data, { type: 'array' });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        vehicleData = XLSX.utils.sheet_to_json(worksheet);
        populateVehicleSelect(vehicleData);
    };
    reader.readAsArrayBuffer(file);
}

// Function to populate vehicle dropdown
function populateVehicleSelect(data) {
    const vehicleSelect = document.getElementById('vehicle-select');
    vehicleSelect.innerHTML = '<option value="">Select a vehicle</option>'; // Clear existing options
    const vehicleIDs = [...new Set(data.map(vehicle => vehicle.Vehicle_ID))];
    vehicleIDs.forEach(id => {
        const option = document.createElement('option');
        option.value = id;
        option.textContent = id;
        vehicleSelect.appendChild(option);
    });
}

// Function to update map with selected vehicle's location and path
function updateMap(vehicleID) {
    map.eachLayer(layer => {
        if (layer instanceof L.Marker || layer instanceof L.Polyline) {
            map.removeLayer(layer);
        }
    });

    const selectedVehicleData = vehicleData.filter(vehicle => vehicle.Vehicle_ID === vehicleID);
    const color = 'blue';
    const latLngs = selectedVehicleData.map(vehicle => [vehicle.Latitude, vehicle.Longitude]);

    selectedVehicleData.forEach(vehicle => {
        L.marker([vehicle.Latitude, vehicle.Longitude], { icon: L.divIcon({ className: 'custom-icon', html: `<div style="background-color: ${color}; width: 10px; height: 10px; border-radius: 50%;"></div>` }) })
            .addTo(map)
            .bindPopup(`<b>${vehicle.Vehicle_ID}</b><br>Speed: ${vehicle.Speed_kmh} km/h`);
    });

    L.polyline(latLngs, { color: color, dashArray: '5, 5' }).addTo(map);
}

// Event listeners
document.getElementById('file-input').addEventListener('change', event => {
    const file = event.target.files[0];
    readExcel(file);
});

document.getElementById('vehicle-select').addEventListener('change', event => {
    const vehicleID = event.target.value;
    if (vehicleID) {
        updateMap(vehicleID);
    }
});
