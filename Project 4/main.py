import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd

load_dotenv()

API_KEY = os.getenv("weatherAPI_KEY")

details = []

KEYWORD = ["Paris", "Mumbai", "Delhi", "Bangalore", "New York"]

for city in KEYWORD:
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}"    

    response = requests.get(url)    

    if response.status_code == 200:
        print(f"Fetching {city}")
        data = response.json()
        temperature = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_mph"]
        condition = data["current"]["condition"]["text"]    

        details.append({"City": city,
                   "Temperature": temperature,
                   "Humidity": humidity,
                   "Wind (in mph)": wind,
                   "Condition": condition,
                   "Date": pd.Timestamp.today().strftime("%Y-%m-%d"),
                   "Time": pd.Timestamp.now().strftime("%H:%M:%S")})

    else:
        print(f"Error: {response.status_code} - {response.text}")

today = datetime.now().strftime("%d-%m-%y")

df = pd.DataFrame(details)
df.to_csv(f"details{today}.csv", index=False)

print(f"All fetched data saved to details{today}.csv")