import requests
import os
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("google_KEY")
CX = "23b320d001037432a"
query = "blogging tips"
url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"

response = requests.get(url)
data = response.json()

for item in data["items"]:
    print(item["title"])
    print(item["link"])
    print("---")