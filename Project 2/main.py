import requests
import json
from bs4 import BeautifulSoup

url = "https://www.bigbasket.com/cl/fruits-vegetables/?nc=nb&page=1"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")

# Find image urls
