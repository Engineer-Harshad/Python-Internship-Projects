import requests
import pandas as pd
from bs4 import BeautifulSoup
all_list = ["?l=html", "?l=javascript", "?l=python","?l=css", "?l=jupyter+notebook","?l=java","?l=c%2B%2B","?l=typescript","?l=c","?lphp"]
listing = [] 
ind = all_list.index
for ind in all_list:
    url = "https://github.com/topics/projects" + ind
    r = requests.get(url).text
    soup = BeautifulSoup(r,'lxml') 
# div1 = soup.find('div',class_="d-md-flex gutter-md").div.details
# details_menu =div1.find('details-menu',class_="select-menu-modal position-absolute")
# div3 = details_menu.find_all('div',class_="select-menu-list")
# links = div3.find_all('a',class_="select-menu-item").get("href")
    div2 =soup.find('div',class_="col-md-8 col-lg-9")
    articles = div2.find_all('article',class_="border rounded color-shadow-small color-bg-subtle my-4")
    for projects in articles:
        a1 = projects.find('div',class_="px-3").div.div.h3.a.get_text(strip=True)
        a2 = projects.find('a',class_="text-bold wb-break-word").get_text(strip=True)
        half_a3 = projects.find('a',class_="text-bold wb-break-word").get("href")
        full_a3 = "https://github.com" + half_a3 
        span1 = projects.find('span',class_="Counter js-social-count").get_text(strip=True)
        div3 = projects.find('div',class_="color-bg-default rounded-bottom-2")
        tags = div3.find('div',class_="d-flex flex-wrap border-bottom color-border-muted px-3 pt-2 pb-2").text 
        print(tags)

        
#         date = projects.find('relative-time',class_="no-wrap").text
#         dictionary = {"username":a1, "Repo name":a2,"Repo_link": full_a3,"Reviews":span1,"Tags":tags,"Date":date}
#         listing.append(dictionary)
# print(listing)
    # data = pd.DataFrame(listing)
    # print(data)
    # data.to_excel("Proj2og.xlsx")



# https://github.com/Python-World/python-mini-projects
# https://github.com
# https://github.com/topics/projects
# https://github.com/topics/projects?l=html
# https://github.com/topics/projects?l=javascript
# https://github.com/topics/projects?l=php
