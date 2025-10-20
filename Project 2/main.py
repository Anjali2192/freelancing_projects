import requests
import json

url = "https://www.bigbasket.com/listing-svc/v2/products?type=mem.sb&slug=all&page=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://www.bigbasket.com/cl/fruits-vegetables/"
}

response = requests.get(url, headers=headers)

if response.status_code==200:
    print("getting data")
    data = response.json()
    with open ("keys.json", "w") as f:
        json.dump(data, f, indent=4) 
    print(F"Saved data in keys.json")

else:
    print(f"Error: {response.status_code} - {response.text}")