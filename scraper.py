# pip install requests beautifulsoup4 lxml

import json
import random
import requests
from bs4 import BeautifulSoup
from pprint import pprint

# TODO: Add ABS-CBN and GMA sitemaps
RAPPLER_SITEMAP_INDEX = "https://www.rappler.com/sitemap_index.xml"

# TODO: For now, this is focused on Rappler only
def get_article_urls(sitemap_url: str, max_urls=10000) -> list[str]:
    print(f"Fetching sitemap: {sitemap_url}")

    # this is to disguise the bot daw
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    response = requests.get(sitemap_url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml-xml")
    loc_tags = soup.find_all("loc")
    urls: list[str] = []
    for loc in loc_tags:
        if len(urls) >= max_urls:
            break
        url = loc.text
        if ("rappler-prod-01" not in url and
            ".jpg" not in url and
            ".png" not in url and
            "go.rappler" not in url):
            print(f"Found url: {url}")
            urls.append(url)

    print(f"Found {len(urls)} urls")
    return urls

def scrape_article_text(article_url: str) -> dict | None:
    print(f"Scraping: {article_url}")
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    response = requests.get(article_url, headers=headers)

    if response.status_code != 200:
        print(f"ERROR with url: status code is {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.content, "lxml")
    title_element = soup.find(class_="post-single__title")
    title = title_element.get_text(strip=True) if title_element else ''
    body_paragraphs = soup.select(".post-single__content p")

    # Have to add the replace because some \xa0 characters are left out
    body = " ".join([p.text.replace(u'\xa0', u' ').strip() for p in body_paragraphs])

    print(f"Done scraping: {url}")
    output = {"title": title, "body": body}
    return output

if __name__ == '__main__':
    urls = []
    urls.extend(get_article_urls("https://www.rappler.com/post-sitemap.xml"))
    # In Rappler, the sitemap goes up to post-sitemap380
    # for i in range(2, 381):
    for i in range(375, 381):
        urls.extend(get_article_urls(f"https://www.rappler.com/post-sitemap{i}.xml"))

    # Get 1,000 random URLs
    random_urls = random.sample(urls, 20)
    scraped = []
    for url in random_urls:
        output = scrape_article_text(url)
        if output is not None:
            scraped.append(output)
    pprint(scraped)

    with open("scraped.json", 'w', encoding='utf8') as output_file:
        output_file.write(json.dumps(scraped))
    
    print("Wrote output into scraped.json")