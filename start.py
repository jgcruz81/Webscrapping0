import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# Fetch the page content
driver = webdriver.Chrome()  # Or webdriver.Firefox() if using Firefox
driver.get("https://www.leagueoflegends.com/en-us/champions/")
time.sleep(10)  # Wait for dynamic content to load


soup = BeautifulSoup(driver.page_source, "html.parser")
# Start from the specified div
start_div = soup.find('div', class_='sc-461cbba4-0 isUeVA')

# Ensure the starting div exists
if start_div:
    for a_tag in start_div.find_all('a', recursive=False):
        span_tag = a_tag.find('span')
        if not span_tag:
            continue

        first_div = span_tag.find('div')
        if not first_div:
            continue

        second_div = first_div.find('div')
        if not second_div:
            continue

        third_div = second_div.find('div')
        if not third_div:
            continue

        img_tag = third_div.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
            print(img_url)

driver.quit()