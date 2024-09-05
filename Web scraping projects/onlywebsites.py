import requests
import pandas as pd
from bs4 import BeautifulSoup
# for i in range(1,9):
url = "https://www.trustpilot.com/categories/energy_heating?page="
# r = requests.get(url).text
# soup = BeautifulSoup(r,'lxml') 
# next_page = soup.find('a',class_="link_internal__7XN06 button_button__T34Lr button_l__mm_bi button_appearance-outline__vYcdF button_squared__21GoE link_button___108l pagination-link_next__SDNU4 pagination-link_rel__VElFy").get("href")
# complete_next_page = "https://www.trustpilot.com" + next_page
raw_data = requests.get(url).text
# WebSites = []
# Mail = []

soup = BeautifulSoup(raw_data,'lxml')
section = soup.find('section')
# websites = soup.find_all('div',class_="tooltip_tooltip-inner__KwHH_").ul.text

# for i in websites:
#     site = i
#     WebSites.append(site)
# print(WebSites)


divb1 = section.find('div',class_="section-theme-provider_theme-default__zZfHS")
divb2 = divb1.find('div',class_="tooltip_tooltip__9gA3F")

divb3 = divb2.find('div',class_="tooltip_tooltip-wrapper__K6y73")

divb4 = divb3.find('div',class_="tooltip_tooltip-inner__KwHH_")
divb5 = divb4.find('div')
span1 = divb5.find('span',class_="typography_body-s__aY15Q typography_appearance-default__AAY17")
ul1 = span1.find('ul',class_="styles_list__4noUG")
li1 = ul1.find('li', class_="typography_body-s__aY15Q typography_appearance-default__AAY17 styles_item__3AZ_v")
a1 = li1.find('a',class_="link_internal__7XN06 typography_appearance-action__9NNRY link_link__IZzHN link_underlined__OXYVM").get("href")
print(a1)

# # print(divb1)
# divb3 = body.find('div',class_="modal_dialog__zS3pe")
# # print(divb3)
# divb4 = body.find('div',class_="modal_content__D8YoR")
# print(divb4)


# ul1 = body.find('ul',class_="styles_list__4noUG").string
# print(ul1)
# li1 = body.find('li',class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_item__3AZ_v")
# print(li1)
# anchor1 = body.find('a',class_="link_internal__7XN06 typography_appearance-action__9NNRY link_link__IZzHN link_underlined__OXYVM")
# print(anchor1)
# li2 = ul1.find('li',class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_item__3AZ_v")
# anchor2 = li2.find('li',class_="link_internal__7XN06 typography_appearance-action__9NNRY link_link__IZzHN link_underlined__OXYVM").string.text


