from bs4 import BeautifulSoup

# Load your HTML file
with open("/Users/juancruz/Downloads/Champions.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find the starting div with the specified class
start_div = soup.find('div', class_='sc-461cbba4-0 isUeVA')

# Open the file in append mode

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
        
        # Drill down through the next three div layers
        first_div = span_tag.find('div')
        if not first_div:
            continue
        
        second_div = first_div.find('div')
        if not second_div:
            continue
        
        third_div = second_div.find('div')
        if not third_div:
            continue
        
        # Look for an img within the third div
        img_tag = third_div.find('img')
        if img_tag and 'src' in img_tag.attrs:
            with open("all.txt", "a") as file:
                img_url = img_tag['src']
                file.write(img_url + "\n")
