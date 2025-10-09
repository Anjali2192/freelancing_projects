import requests
import os
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

KEYWORDS = ["blogging tips", "marketing strategies", "content creation"]

website_urls = []

API_KEY = os.getenv("google_KEY")
CX = "23b320d001037432a"

for keyword in KEYWORDS:
    print(f"{keyword} is being searched")    

    url = f"https://www.googleapis.com/customsearch/v1?q={keyword}&key={API_KEY}&cx={CX}" 
    
    response = requests.get(url)
    data = response.json()

    urls = []
    for item in data["items"]:
        urls.append(item["link"])  

    # Store data
    for link in urls:
        website_urls.append({
            "URL": link,
            "Search Engine": "Bing",
            "Keyword": keyword,
            "Date": pd.Timestamp.today().strftime("%Y-%m-%d")
        })    

    print(f"✅ Found {len(urls)} links for '{keyword}'")    

print(website_urls)