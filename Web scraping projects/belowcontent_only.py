import requests
import pandas as pd
from bs4 import BeautifulSoup
firsturl = "https://www.trustpilot.com/categories/energy_heating"
raw_data = requests.get(firsturl).text
#print(raw_data)
soup = BeautifulSoup(raw_data,'lxml')
#print(soup)
body = soup.find('body')
divb1 = body.find('div',class_="section-theme-provider_theme-default__zZfHS")
divb2 = divb1.find('div',class_="modal_modal__96QW2")
divb3 = divb2.find('div',class_="modal_dialog__zS3pe")
divb4 = divb3.find('div',class_="modal_content__D8YoR")
ul1 = divb4.find('ul',class_="styles_list__4noUG")  
li1 = ul1.find('li',class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_item__3AZ_v")
print(li1)