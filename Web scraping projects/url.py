import requests
import pandas as pd
from bs4 import BeautifulSoup
list_1 = []
for item in range(1,8):
    base_url  = "https://www.trustpilot.com/categories/energy_heating?page=" 
    list_1.append(base_url + str(item))

# firsturl = "https://www.trustpilot.com/categories/energy_heating"
raw_data = requests.get(list_1[0]).text
#print(raw_data)
soup = BeautifulSoup(raw_data,'lxml')
#print(soup)
body = soup.find('div',class_="modal_content__D8YoR")
print(body)
# divb1 = body.find('div',class_="section-theme-provider_theme-default__zZfHS").text
# print(divb1)
# divb2 = divb1.find('div',class_="modal_modal__96QW2")

# divb3 = body.find('div',class_="modal_dialog__zS3pe").text 
# print(divb3)

# divb4 = divb3.find('div',class_="modal_content__D8YoR")
# ul1 = body.find('ul',class_="styles_list__4noUG")  
# li1 = body.find('li',class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_item__3AZ_v")
# anchor1 = body.find('a',class_="link_internal__7XN06 typography_appearance-action__9NNRY link_link__IZzHN link_underlined__OXYVM")
# li2 = ul1.find('li',class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_item__3AZ_v")
# anchor2 = li2.find('li',class_="link_internal__7XN06 typography_appearance-action__9NNRY link_link__IZzHN link_underlined__OXYVM")




# for item in range(1,8):
#     base_url  = "https://www.trustpilot.com/categories/energy_heating?page=" 
#     new_url.append(base_url + item)

#     new_url = "https://www.trustpilot.com/categories/energy_heating?page=1" 



url = " "
# item = 1 to 8 no's 
list = []
for item in range(1,8):
    list.append("url" + str(item))

list = [" ", " ", " "]
list[0]
list[1]
list[2]
for i in range(0,8):
    var = (list[i]) 