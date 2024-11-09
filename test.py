from bs4 import BeautifulSoup

# Load your HTML file
with open("/Users/juancruz/Downloads/Champions.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find the starting div with the specified class
start_div = soup.find('div', class_='sc-461cbba4-0 isUeVA')

# Ensure the starting div exists
if start_div:
    for a_tag in start_div.find_all('a', recursive=False):
        span_tag = a_tag.find('span')
        if not span_tag:
            continue
        
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
            img_url = img_tag['src']
            print(img_url)
