import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("weatherAPI_KEY")

city = "Paris"

url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}"

response = requests.get(url)

if response.status_code == 200:
    print("Fetching data !")
    data = response.json()
    temp = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    wind = data["current"]["wind_mph"]
    condition = data["current"]["condition"]["text"]

else:
    print(f"Error: {response.status_code} - {response.text}")

#with open("keys.json", "w") as f:
#    json.dump(data, f, indent=4)

df = pd.DataFrame([{"City": city,
                   "Temperature": temp,
                   "Humidity": humidity,
                   "Wind (in mph)": wind,
                   "Condition": condition}])

print(df)

