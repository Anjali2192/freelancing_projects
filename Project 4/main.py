import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import smtplib
from email.message import EmailMessage

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

filename = f"details{today}.csv"
df = pd.DataFrame(details)
df.to_csv(filename, index=False)

print(f"All fetched data saved to details{today}.csv")

SENDER_EMAIL = os.getenv("sender_email")
SENDER_PASSWORD = os.getenv("sender_password")
RECEIVER_EMAIL = os.getenv("receiver_email")

msg = EmailMessage()
msg["Subject"] = f"Weather Report : {today}"
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg.set_content("Hi,\n\nHere is your daily weather report.\n\nRegards,\nYour Automation Bot")

with open(filename, "rb") as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=filename)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
    smtp.send_message(msg)

print("Email sent successfully!")