import requests
import pandas as pd
from bs4 import BeautifulSoup
listing = [] 
for i in range(1,10):
    url = "https://github.com/topics/projects?l=java&page=" + str(i)
    r = requests.get(url).text
    soup = BeautifulSoup(r,'lxml') 
    div2 =soup.find('div',class_="col-md-8 col-lg-9")
    articles = div2.find('article',class_="border rounded color-shadow-small color-bg-subtle my-4")
    # a1 = projects.find('div',class_="px-3").div.div.h3.a.get_text(strip=True)
    # a2 = projects.find('a',class_="text-bold wb-break-word").get_text(strip=True)
    # half_a3 = projects.find('a',class_="text-bold wb-break-word").get("href")
    # full_a3 = "https://github.com" + half_a3 
    # span1 = projects.find('span',class_="Counter js-social-count").get_text(strip=True)
    # tags = projects.find('div',class_="color-bg-default rounded-bottom-2").text
    tags= articles.find('div',class_="d-flex flex-wrap border-bottom color-border-muted px-3 pt-2 pb-2").text
    # date = projects.find('relative-time',class_="no-wrap").text
    dictionary = {"Tags":tags}
    listing.append(dictionary)
data = pd.DataFrame(listing)
print(data)
data.to_excel("Project_java.xlsx")