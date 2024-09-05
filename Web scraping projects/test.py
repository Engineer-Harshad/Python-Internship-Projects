import requests
import pandas as pd
from bs4 import BeautifulSoup
mylist = [] 
for i in range(1,9):
    url = "https://www.trustpilot.com/categories/energy_heating?page=" + str(i)
    r = requests.get(url).text
    soup = BeautifulSoup(r,'lxml') 
    section_1 = soup.find('section',class_="styles_feed__MNr87") 
    div7 = section_1.find_all('div',class_="paper_paper_1PY90 paper_outlinelwsUX card_cardlQWDv card_noPaddingD8PcU styles_wrapper_2JOo2")
    for com in div7:
        div8 = com.find('div',class_="styles_content__98tWf")
        div9 = com.find('div',class_="styles_businessUnitMain__PuwB7")
        s = com.find('p',class_="typography_heading-xs_jSwUz typography_appearance-defaultAAY17 styles_displayName_GOhL2").get_text(strip = True)
        div10 = com.find('div',class_="styles_rating__pY5Pk")
        try:
            p_in = com.find('p',class_="typography_body-m_xgxZ typography_appearance-subtle_8_H2l styles_ratingText_yQ5S7").text 
            spacing = p_in.split('|')
            rate_list = spacing[0]
            rate = rate_list[11:14]
            reviews = spacing[1].replace("reviews", "")
            Dict = {"Name" : s, "Ratings": rate, "Reviews" : reviews}
            mylist.append(Dict)
        except:
            rate = "None"
            reviews = "None"
            Dict = {"Name" : s, "Ratings": rate, "Reviews" : reviews}
            mylist.append(Dict)
data = pd.DataFrame(mylist)
data.to_excel("Best companies in Energy.xlsx")