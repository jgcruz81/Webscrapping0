from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

# Read URLs from file
with open("all.txt", "r") as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    driver.get(url)
    time.sleep(5)  # Adjust if necessary

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Locate the image tag (adjust selector as needed)
    img_tag = soup.find('img')
    if img_tag and 'src' in img_tag.attrs:
        img_url = img_tag['src']
        
        # Download the image
        img_data = requests.get(img_url).content
        file_name = os.path.join("images", f"{url.split('//')[1].replace('/', '_')}.jpg")
        with open(file_name, 'wb') as handler:
            handler.write(img_data)

driver.quit()
