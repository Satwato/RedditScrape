import requests
import csv
import time
from bs4 import BeautifulSoup

url="https://old.reddit.com/r/SuicideWatch/"
headers = {'User-Agent': 'Mozilla/5.0'}

page = requests.get(url,headers=headers)


soup=BeautifulSoup(page.text, 'html.parser')
# domains = soup.find_all("span", class_="domain")

# soup.find_all("span", {"class": "domain", "height": "100px"})

# for domain in domains:
#     if domain != "(self.SuicideWatch)":
#         continue

#     print(domain.text)

for domain in soup.find_all("span", class_="domain"):
    if domain.text != "(self.SuicideWatch)":
       #print(domain.text)
        continue
    
    parent_div = domain.parent
    print(parent_div.text)