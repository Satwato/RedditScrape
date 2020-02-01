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

# for domain in soup.find_all("span", class_="domain"):
#     if domain.text != "(self.SuicideWatch)":
#        #print(domain.text)
#         continue
    
#     parent_div = domain.parent
#     print(parent_div.text)

attrs = {'class': 'thing', 'data-domain': 'self.SuicideWatch'}


    
counter = 1
words=[]
try:
  for i in tqdm(range(100)):
      for post in soup.find_all('div', attrs=attrs):
          f= open("titles.txt","a+")
          f2= open("posts.txt","a+")
          link = post.find('a', class_="title").get('href')
          #print(link)
          title = post.find('a', class_="title").text
          f.write("# "+title+"\n")
          
          p1 = requests.get("https://old.reddit.com"+link,headers=headers)
          s1=BeautifulSoup(p1.text, 'html.parser')

          if s1.find('div', attrs=attrs).find('div', class_="usertext-body") != None:
              post=s1.find('div', attrs=attrs).find('div', class_="usertext-body").text
              f2.write("# "+title+"\n")
              f2.write("@ "+post+"\n")
          else:
              f2.write("# "+title+"\n")
          words.extend(list(title.split(" ")))
          
          f.close()
          f2.close()

          #print(title)
          #print(post)
      #print(next_page_link[:-16])
      if soup.find("span", class_="next-button") != None:
        next_button = soup.find("span", class_="next-button")
        next_page_link = next_button.find("a").attrs['href']
      else:
        #print("ASSSSSS")
        page = requests.get(next_page_link[:-16], headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        next_button = soup.find("span", class_="next-button")
        next_page_link = next_button.find("a").attrs['href']
      time.sleep(2)
      page = requests.get(next_page_link, headers=headers)
      soup = BeautifulSoup(page.text, 'html.parser')
except AttributeError:
  print(page.text)
  print(soup)

print(words)