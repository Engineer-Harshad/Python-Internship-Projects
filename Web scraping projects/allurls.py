# import requests
# from bs4 import BeautifulSoup

# for i in range(1,9):
#     url = "https://www.trustpilot.com/categories/energy_heating?page=" + str(i)
#     r = requests.get(url).text
#     soup = BeautifulSoup(r,'lxml') 
#     next_page = soup.find('a',class_="link_internal__7XN06 button_button__T34Lr button_l__mm_bi button_appearance-outline__vYcdF button_squared__21GoE link_button___108l pagination-link_next__SDNU4 pagination-link_rel__VElFy").get("href")
#     complete_next_page = "https://www.trustpilot.com" + next_page
#     print(complete_next_page)

#         # url = complete_next_page
#         # r = requests.get(url)
#         # soup = BeautifulSoup(r.text,"lxml")



import requests
import pandas as pd
from bs4 import BeautifulSoup
mylist = [] 
for i in range(1,9):
    url = "https://www.trustpilot.com/categories/energy_heating?page=" + str(i)
    r = requests.get(url).text
    soup = BeautifulSoup(r,'lxml') 
    section = soup.find('section',class_="styles_feed__MNr87") 
    div7 = section.find_all('div',class_="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2")
    for com in div7:
        div8 = com.find('div',class_="styles_content__98tWf")
        div9 = com.find('div',class_="styles_businessUnitMain__PuwB7")
        p_tag = com.find('p',class_="typography_heading-xs__jSwUz typography_appearance-default__AAY17 styles_displayName__GOhL2").get_text(strip = True)
        div10 = com.find('div',class_="styles_rating__pY5Pk")
        try:
            p_in = com.find('p',class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_ratingText__yQ5S7").text 
            spacing = p_in.split('|')
            rate_list = spacing[0]
            rate = rate_list[11:14]
            reviews = spacing[1].replace("reviews", "")
            Dict = {"Name" : p_tag, "Ratings": rate, "Reviews" : reviews}
            mylist.append(Dict)
        except:
            rate = "None"
            reviews = "None"
            Dict = {"Name" : p_tag, "Ratings": rate, "Reviews" : reviews}
            mylist.append(Dict)
data = pd.DataFrame(mylist)
data.to_excel("final.xlsx")



 # next_page = soup.find('a',class_="link_internal__7XN06 button_button__T34Lr button_l__mm_bi button_appearance-outline__vYcdF button_squared__21GoE link_button___108l pagination-link_next__SDNU4 pagination-link_rel__VElFy").get("href")
    # complete_next_page = "https://www.trustpilot.com" + next_page
    # raw_data = requests.get(complete_next_page).text
    # soup = BeautifulSoup(raw_data,'lxml')

# body = soup.find('body')
    # div1 = body.find('div')
    # div2 = div1.find('div',class_= "theme-provider_themeProvider__MkYcR theme-provider_theme-default__IISCt")
    # div3 = div2.find('div',class_= "layout_wrapper__s2pss")
    # main = div3.find('main',class_="layout_content__o0ojo")
    # div4 = main.find('div',class_="styles_wrapper__2vU7q")
    # div5 = div4.find('div',class_="styles_body__WGdpu")
    # div6 = div5.find('div',class_="styles_main__XgQiu")