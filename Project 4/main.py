import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("weatherAPI_KEY")

details = []

KEYWORD = ["Paris", "Mumbai", "Delhi", "Bangalore", "New York"]

for city in KEYWORD:
    temp = []
    humidity = []
    wind = []
    condition = []

    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}"    

    response = requests.get(url)    

    if response.status_code == 200:
        print(f"Fetching {city}")
        data = response.json()
        temperature = data["current"]["temp_c"]
        hmdty = data["current"]["humidity"]
        wnd = data["current"]["wind_mph"]
        cndtn = data["current"]["condition"]["text"]    

        temp.append(temperature)
        humidity.append(hmdty)
        wind.append(wnd)
        condition.append(cndtn)

        details.append({"City": city,
                   "Temperature": temp,
                   "Humidity": humidity,
                   "Wind (in mph)": wind,
                   "Condition": condition})

    else:
        print(f"Error: {response.status_code} - {response.text}")

df = pd.DataFrame(details)

print(df)

