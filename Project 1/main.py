import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
]

KEYWORDS = ["blogging tips", "marketing strategies", "content creation"]

website_urls = []

def search_bing():
    print("Searching Bing")
    for keyword in KEYWORDS:
        print(f"{keyword} is being searched")    

        headers = {"User-Agent": random.choice(USER_AGENTS)}
        url = "https://www.bing.com/search?q={keyword.replace(' ', '+')}"
        print(f"Using header: {headers['User-Agent']}")    

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")    

        #Extract URLs
        urls = []
        for result in soup.find_all("li", class_="b_algo"):
            a_tag = result.find("a")
            if a_tag and a_tag.get("href"):
                urls.append(a_tag["href"])    

        # Store data
        for link in urls:
            website_urls.append({
                "URL": link,
                "Search Engine": "Bing",
                "Keyword": keyword,
                "Date": pd.Timestamp.today().strftime("%Y-%m-%d")
            })    

        print(f"✅ Found {len(urls)} links for '{keyword}'")    

        # Random delay to act human-like
        time.sleep(random.uniform(2, 5))

def search_yahoo():
    print("Searching Yahoo")
    for keyword in KEYWORDS:
        print(f"{keyword} is being searched")

        headers = {"User-Agent": random.choice(USER_AGENTS)}
        url = "https://in.search.yahoo.com/search?q={keyword.replace(' ', '+')}"
        print(f"Using header: {headers['User-Agent']}")    

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")    

        #Extract URLs
        urls = []
        for result in soup.find_all("li", class_="last"):
            a_tag = result.find("a")
            if a_tag and a_tag.get("href"):
                urls.append(a_tag["href"])    

        # Store data
        for link in urls:
            website_urls.append({
                "URL": link,
                "Search Engine": "Yahoo",
                "Keyword": keyword,
                "Date": pd.Timestamp.today().strftime("%Y-%m-%d")
            })    

        print(f"✅ Found {len(urls)} links for '{keyword}'")    

        # Random delay to act human-like
        time.sleep(random.uniform(2, 5))

search_bing()
search_yahoo()

#Export all data
df = pd.DataFrame(website_urls)
df.to_csv("link.csv", index=False)
print("\n📁 Saved all results to link.csv")