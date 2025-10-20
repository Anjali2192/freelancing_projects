from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()

driver.get("https://www.sunglasshut.com/us/mens-sunglasses")
time.sleep(3)

is_saved = driver.save_screenshot("C:/Users/hp/OneDrive/Pictures/Screenshots/full.png")
if is_saved:
    print("Screenshot saved successfully!")
else:
    print("Failed to save screenshot!")

input("Press Enter to close the Browser...")