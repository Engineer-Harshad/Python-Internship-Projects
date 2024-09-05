import requests
import pandas as pd
from bs4 import BeautifulSoup
listing = [] 
for i in range(1,10):
    url = "https://github.com/topics/projects?l=java&page=" + str(i)
    r = requests.get(url).text
    soup = BeautifulSoup(r,'lxml') 
    div2 =soup.find_all('div',class_="col-md-8 col-lg-9")
    for projects in div2:
        article = projects.find('article',class_="border rounded color-shadow-small color-bg-subtle my-4")
        a1 = article.find('div',class_="px-3").div.div.h3.a.get_text(strip=True)
        a2 = article.find('a',class_="text-bold wb-break-word").get_text(strip=True)
        half1 = article.find('div',class_="px-3").div.div
        h3 = half1.find('h3',class_="f3 color-fg-muted text-normal lh-condensed")
        half2 = h3.find('a',class_="text-bold wb-break-word").get("href")
        # half_a3 = projects.find('a',class_="text-bold wb-break-word").get("href")
        full1 = "https://github.com" + half2
        rate1 = article.find('div',class_="px-3").div
        rate2 = rate1.find('div',class_="d-flex flex-items-center").div.a
        span1 = rate2.find('span',class_="Counter js-social-count").get_text(strip=True)
        # span1 = projects.find('span',class_="Counter js-social-count").get_text(strip=True)
        div2_new =soup.find('div',class_="col-md-8 col-lg-9")
        artic = div2_new.find_all('article',class_="border rounded color-shadow-small color-bg-subtle my-4")
        for tags_all in artic:
            tag1 = tags_all.find('div',class_="color-bg-default rounded-bottom-2")
            tag2 = tag1.find('div',class_="d-flex flex-wrap border-bottom color-border-muted px-3 pt-2 pb-2").text
        # tags = projects.find('div',class_="d-flex flex-wrap border-bottom color-border-muted px-3 pt-2 pb-2").text
        # date = projects.find('relative-time',class_="no-wrap").text
        date1 = article.find('div',class_="color-bg-default rounded-bottom-2")
        date2 = date1.find('div',class_="p-3").ul.li
        date3 = date2.find('relative-time',class_="no-wrap").get_text(strip=True)
        dictionary = {"username":a1, "Repo name":a2,"Repo_link": full1,"Reviews":span1,"Tags":tag2, "Date":date3}
        listing.append(dictionary)
data = pd.DataFrame(listing)
print(data)
data.to_excel("Project_java_2.xlsx")