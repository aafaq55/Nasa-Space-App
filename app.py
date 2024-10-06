import requests
from datetime import datetime

# Replace with your NASA API Key
API_KEY = "FmR2fL8mNtwGhHhgkCUUszdDVQRq9XT9VPHY2adm"

# Get today's date in the required format
today = datetime.today().strftime('%Y-%m-%d')

# NASA API URL for fetching asteroid data
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={today}&api_key={API_KEY}"

# Send a request to NASA's API
response = requests.get(url)
data = response.json()

# Loop through the data and print out asteroid details
for obj in data['near_earth_objects'][today]:
    name = obj['name']
    distance = obj['close_approach_data'][0]['miss_distance']['kilometers']
    velocity = obj['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
    hazardous = obj['is_potentially_hazardous_asteroid']
    
    print(f"Asteroid: {name}")
    print(f"Closest Distance: {distance} km")
    print(f"Speed: {velocity} km/h")
    print(f"Potentially Hazardous: {'Yes' if hazardous else 'No'}")
    print("-------------")
print(response.status_code)
