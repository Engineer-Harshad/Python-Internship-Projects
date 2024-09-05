import requests
import pandas as pd
from bs4 import BeautifulSoup
list_2 = [] 
for i in range(1,9):
    url = "https://www.trustpilot.com/categories/energy_heating?page=" + str(i)
    r = requests.get(url).text
    soup = BeautifulSoup(r,'lxml') 
    section_1 = soup.find('section',class_="styles_feed__MNr87") 
    div7 = section_1.find_all('div',class_="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2")
    for com in div7:
        div8 = com.find('div',class_="styles_content__98tWf")
        div9 = com.find('div',class_="styles_businessUnitMain__PuwB7")
        name = com.find('p',class_="typography_heading-xs__jSwUz typography_appearance-default__AAY17 styles_displayName__GOhL2").get_text(strip = True)
        div10 = com.find('div',class_="styles_rating__pY5Pk")
        try:
            p_in = com.find('p',class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_ratingText__yQ5S7").text 
            spacing = p_in.split('|')
            rate_list = spacing[0]
            rate = rate_list[11:14]
            reviews = spacing[1].replace("reviews", "")
            Dict1 = {"Name" : name, "Ratings": rate, "Reviews" : reviews}
            list_2.append(Dict1)
        except:
            rate = "None"
            reviews = "None"
            Dict1 = {"Name" : name, "Ratings": rate, "Reviews" : reviews}
            list_2.append(Dict1)
data = pd.DataFrame(list_2)
print(data)
data.to_excel("Best companies in Energy & Heating.xlsx")