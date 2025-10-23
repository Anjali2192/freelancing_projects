import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("weatherAPI_KEY")

url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q=Paris"

response = requests.get(url)

if response.status_code == 200:
    print("Fetching data !")
    data = response.json()
    print(data)

else:
    print(f"Error: {response.status_code} - {response.text}")

with open("keys.json", "w") as f:
    json.dump(data, f, indent=4)

print("It's done")