from playwright.sync_api import sync_playwright
import json
import time

def scrape_bigbasket(url):
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # keep visible for testing
        page = browser.new_page()

        # Spoof headers to look like a real user
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

        page.goto(url, timeout=60000)
        time.sleep(5)  # wait for content to load fully

        # scroll down gradually to trigger lazy loading
        for _ in range(5):
            page.mouse.wheel(0, 2000)
            time.sleep(2)

        # extract products
        products = page.locator('li.PaginateItems___StyledLi-sc-1yrbjdr-0')
        count = products.count()

        for i in range(count):
            name = products.nth(i).locator('h3').inner_text(timeout=5000)
            price = products.nth(i).locator('span.Tag___StyledTag-sc-15mnnkz-0').first.inner_text(timeout=5000)
            img = products.nth(i).locator('img').get_attribute('src')

            results.append({
                "name": name,
                "price": price,
                "image": img
            })

        browser.close()

    return results

# Example: fruits and vegetables page
url = "https://www.bigbasket.com/cl/fruits-vegetables/"
data = scrape_bigbasket(url)

with open("bigbasket_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Scraped {len(data)} products and saved in bigbasket_data.json")
