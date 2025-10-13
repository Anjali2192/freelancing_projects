import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://www.bigbasket.com/basketService/get/"

headers = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

cookies_str = os.getenv("COOKIES")
cookies = dict(item.split("=", 1) for item in cookies_str.split("; ") if "=" in item)

# Make the GET request
response = requests.get(url, headers=headers, cookies=cookies)

# Check the response
print(response.status_code)
