import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# Fetch the page content
driver = webdriver.Chrome()  # Or webdriver.Firefox() if using Firefox
driver.get("https://www.leagueoflegends.com/en-us/champions/")
time.sleep(7)  # Wait for dynamic content to load


soup = BeautifulSoup(driver.page_source, "html.parser")
# Start from the specified div
start_div = soup.find('div', class_='sc-461cbba4-0 isUeVA')

# Ensure the starting div exists
if start_div:
    for a_tag in start_div.find_all('a', recursive=False):
        span_tag = a_tag.find('span')
        if not span_tag:
            continue
        
        with open("all.txt", "a") as file:
            aria_label = a_tag.get('aria-label')
            if aria_label:
                file.write(aria_label + "\n")

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
            with open("all.txt", "a") as file:
                img_url = img_tag['src']
                file.write(img_url + "\n")

driver.quit()