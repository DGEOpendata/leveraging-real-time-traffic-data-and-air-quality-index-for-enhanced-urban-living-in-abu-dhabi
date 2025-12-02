python
import requests
import json
import time

# Define URLs for the real-time traffic data and air quality index API
TRAFFIC_API_URL = 'https://api.abudhabi.traffic/v1/realtime'
AQI_API_URL = 'https://api.abudhabi.env/v1/aqi'

# Function to fetch real-time traffic data
def fetch_traffic_data():
    response = requests.get(TRAFFIC_API_URL)
    if response.status_code == 200:
        traffic_data = response.json()
        return traffic_data
    else:
        return None

# Function to fetch air quality index data
def fetch_aqi_data():
    response = requests.get(AQI_API_URL)
    if response.status_code == 200:
        aqi_data = response.json()
        return aqi_data
    else:
        return None

# Main function
if __name__ == '__main__':
    while True:
        # Fetch data
        traffic_data = fetch_traffic_data()
        aqi_data = fetch_aqi_data()

        # Process and display data
        if traffic_data and aqi_data:
            print('Traffic Data:', json.dumps(traffic_data, indent=4))
            print('AQI Data:', json.dumps(aqi_data, indent=4))
        else:
            print('Error fetching data')

        # Wait for 5 minutes before the next call
        time.sleep(300)
