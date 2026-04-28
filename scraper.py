# pip install requests beautifulsoup4 lxml selenium webdriver_manager
# Also need Chrome driver https://developer.chrome.com/docs/chromedriver

import requests
import time
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# TODO: Add ABS-CBN and GMA sitemaps
RAPPLER_SITEMAP_INDEX = "https://www.rappler.com/sitemap_index.xml"

def setup_chrome():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-images")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# TODO: For now, this is focused on Rappler only
def get_article_urls(sitemap_url: str, target_amount=1000) -> list[str]:
    print(f"Fetching sitemap: {sitemap_url}")

    # this is to disguise the bot daw
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    response = requests.get(sitemap_url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml-xml")
    loc_tags = soup.find_all("loc")
    urls = []
    for loc in loc_tags:
        if len(urls) >= target_amount:
            break
        if "rappler-prod-01" not in (url := loc.text):
            urls.append(url)

    pprint(urls)
    print(f"Found {len(urls)} urls")
    return urls

def scrape_article_text(driver: webdriver.Chrome, url: str) -> dict:
    ...

get_article_urls("https://www.rappler.com/post-sitemap380.xml")