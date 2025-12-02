## Abu Dhabi Traffic and Air Quality Monitoring Platform

This project aims to integrate real-time traffic and air quality index data to provide a comprehensive overview of urban conditions in Abu Dhabi. It offers a simple yet effective solution for commuters, urban planners, and policymakers to make informed decisions.

### Features
- **Real-time Traffic Monitoring**: Fetches and displays live traffic data to assist with route planning.
- **Air Quality Index Alerts**: Provides updates on air quality levels, focusing on pollutants like PM2.5 and NO2.
- **Customizable Notifications**: Users can set preferences for route-specific traffic updates and air quality alerts.

### Getting Started

#### Prerequisites
- Python 3.x
- Internet connection
- Access to the Abu Dhabi Traffic API and AQI API

#### Installation
1. **Clone the Repository**:
   bash
   git clone https://github.com/your-repo/abu-dhabi-traffic-aqi.git
   cd abu-dhabi-traffic-aqi
   

2. **Install Dependencies**:
   Ensure you have `requests` library:
   bash
   pip install requests
   

#### Running the Application
Run the script using Python:
bash
python monitor.py


The application will continuously fetch and display traffic and AQI data every 5 minutes.

### Contributing
We welcome contributions from the community. Please ensure your code adheres to the project's coding standards and includes relevant tests.

### License
This project is licensed under the MIT License.
