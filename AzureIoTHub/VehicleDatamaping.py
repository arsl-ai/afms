import pandas as pd
import folium

# 1. Load the CSV data into a Pandas DataFrame
csv_data = """VehicleID,Timestamp,Latitude,Longitude,Speed,Heading,Altitude,Odometer,FuelLevel
V001,2023-10-27 10:00:00,34.0522,-118.2437,65,270,150,123456,80
V001,2023-10-27 10:01:00,34.0530,-118.2445,68,272,152,123457,79
V001,2023-10-27 10:02:00,34.0538,-118.2453,70,275,155,123458,78
V002,2023-10-27 10:00:00,40.7128,-74.0060,30,90,20,54321,90
V002,2023-10-27 10:01:00,40.7135,-74.0055,32,92,22,54322,89
V002,2023-10-27 10:02:00,40.7142,-74.0050,35,95,25,54323,88
V003,2023-10-27 10:00:00,47.6062,-122.3321,45,180,50,98765,70
V003,2023-10-27 10:01:00,47.6068,-122.3328,48,182,52,98766,69
V003,2023-10-27 10:02:00,47.6074,-122.3335,50,185,55,98767,68
V001,2023-10-27 10:03:00,34.0546,-118.2461,72,278,158,123459,77
V001,2023-10-27 10:04:00,34.0554,-118.2469,75,280,160,123460,76
V002,2023-10-27 10:03:00,40.7149,-74.0045,38,98,28,54324,87
V002,2023-10-27 10:04:00,40.7156,-74.0040,40,100,30,54325,86
V003,2023-10-27 10:03:00,47.6080,-122.3342,52,188,58,98768,67
V003,2023-10-27 10:04:00,47.6086,-122.3349,55,190,60,98769,66"""

import io

df = pd.read_csv(io.StringIO(csv_data))

# 2. Visualize on a map using Folium
# Create a base map centered on the first location
if not df.empty:
    map_center = [df['Latitude'].iloc[0], df['Longitude'].iloc[0]]
    m = folium.Map(location=map_center, zoom_start=10)

    # Add markers for each location
    for index, row in df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"Vehicle: {row['VehicleID']}<br>Time: {row['Timestamp']}<br>Speed: {row['Speed']}",
            icon=folium.Icon(color='blue')
        ).add_to(m)

    # Save the map to an HTML file or display in a notebook
    m.save("vehicle_tracking_map.html")
    # m # Uncomment to display in a Jupyter Notebook

# 3. Analyze movement (example: calculate distance)
# (This requires more complex calculations and is beyond the scope of a simple example)
# For example, you would use haversine formula, or other distance calculations.

# 4. Store in a database (example using SQLite)
import sqlite3

conn = sqlite3.connect('vehicle_tracking.db')
df.to_sql('vehicle_locations', conn, if_exists='replace', index=False)
conn.close()

# 5. Simulate GPS data (example: generate more data)
# (This is a simplified example, real simulation is more complex)
import random
import datetime

def generate_gps_data(num_points=10):
    data = []
    vehicle_ids = ['V004', 'V005']
    start_time = datetime.datetime.now()
    for _ in range(num_points):
        vehicle_id = random.choice(vehicle_ids)
        timestamp = start_time + datetime.timedelta(minutes=_)
        lat = random.uniform(33, 48)  # Example range
        lon = random.uniform(-123, -73) # Example range
        speed = random.randint(20, 80)
        heading = random.randint(0, 360)
        altitude = random.randint(10, 200)
        odometer = random.randint(10000, 200000)
        fuel_level = random.randint(10, 100)
        data.append([vehicle_id, timestamp, lat, lon, speed, heading, altitude, odometer, fuel_level])
    return pd.DataFrame(data, columns=['VehicleID', 'Timestamp', 'Latitude', 'Longitude', 'Speed', 'Heading', 'Altitude', 'Odometer', 'FuelLevel'])

new_data = generate_gps_data(20)
print(new_data.head()) # prints the first few rows of the generated data.