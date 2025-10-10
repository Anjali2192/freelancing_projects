# PROJECT 1 :🌐 Search Engine URL Fetcher

### 📁 Project Overview
This project automates the process of fetching website URLs from **Google**, **Bing**, and **Yahoo** for a set of target keywords.  
It demonstrates the use of **web scraping, data extraction, and structured output handling** using Python.

The fetched URLs are stored in a CSV file (`link.csv`) along with the **search engine name** and the **date** of extraction.

---

### 🎯 Objective
To build a Python script that automatically:
1. Searches multiple queries across **different search engines**.
2. Extracts URLs from the search results.
3. Saves the data in a structured CSV format for further analysis or marketing research.

---

### 🧠 Keywords Used
The script fetches URLs for the following keywords:
 KEYWORDS = ["blogging tips", "marketing strategies", "content creation"]

Each keyword is searched on Google, Bing, and Yahoo — three times per search engine.

---

### 🧩 Tech Stack
1. Language: Python
2. Libraries Used: requests, BeautifulSoup, csv, datetime
3. Output Format: CSV

---

### 🧾 Summary
This project represents a real-world freelance-style task that involves:

*Multi-engine web scraping
*Keyword-based URL collection
*Organized CSV output
*Automation potential
*It serves as a foundational practice project for larger scraping and automation workflows.

---

### 🚀 Future Enhancements

-Add pagination support to fetch more results per search engine.

-Integrate proxy and user-agent rotation to handle rate limits.

-Automate weekly runs using Task Scheduler or cron jobs.

-Add logging and error handling for failed searches.

---