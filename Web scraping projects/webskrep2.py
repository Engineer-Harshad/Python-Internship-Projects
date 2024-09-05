import requests
import pandas as pd
from bs4 import BeautifulSoup
base_url  = "https://www.trustpilot.com/categories/energy_heating?page=" 
list = []
mylist = []
for item in range(1,8):
    new_url = base_url + str(item)
    list.append(new_url)
    for i in range(0,9):
        var = (list[i]) 
        raw_data = requests.get(var).text
        soup = BeautifulSoup(raw_data,'lxml')
        body = soup.find('body')
        div1 = body.find('div')
        div2 = div1.find('div',class_= "theme-provider_themeProvider__MkYcR theme-provider_theme-default__IISCt")
        div3 = div2.find('div',class_= "layout_wrapper__s2pss")
        main = div3.find('main',class_="layout_content__o0ojo")
        div4 = main.find('div',class_="styles_wrapper__2vU7q")
        div5 = div4.find('div',class_="styles_body__WGdpu")
        div6 = div5.find('div',class_="styles_main__XgQiu")
        section = div6.find('section',class_="styles_feed__MNr87") 
        div7 = section.find_all('div',class_="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2")
        
        for com in div7:
            a1 = com.find('a',class_="link_internal__7XN06 link_wrapper__5ZJEx styles_linkWrapper__UWs5j")
            div8 = com.find('div',class_="styles_content__98tWf")
            div9 = com.find('div',class_="styles_businessUnitMain__PuwB7")
            p_tag = com.find('p',class_="typography_heading-xs__jSwUz typography_appearance-default__AAY17 styles_displayName__GOhL2").get_text(strip = True)
            print(p_tag)
            # div10 = com.find('div',class_="styles_rating__pY5Pk")
            # p_in = com.find('p',class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_ratingText__yQ5S7").text.split('|')
            # rate_list = p_in[0]
            # rate = rate_list[11:14]
            # reviews = p_in[1].replace("reviews", "")

            # Dict = {"Name" : p_tag, "Ratings": rate, "Reviews" : reviews}
            # mylist.append(Dict)
            # data = pd.DataFrame(mylist)
            # print(data)
# data.to_excel("Pyintern.xlsx")
    


# divb1 = body.find('div',class_="section-theme-provider_theme-default__zZfHS").string.text
# print(divb1)
# divb1 = body.find('div',class_="modal_modal__96QW2")
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






# anchor1 = li1.find('a',class_="link_internal__7XN06 typography_appearance-action__9NNRY link_link__IZzHN link_underlined__OXYVM").text
# li2 = unordered.find('li',class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_item__3AZ_v")
# anchor2 = li2.find('a href = "mailto:%20sales@jedcosupply.com" rel="noreferrer nofollow noopener" target="_blank" data-email-typography="true"',class_="link_internal__7XN06 typography_appearance-action__9NNRY link_link__IZzHN link_underlined__OXYVM")
# print(anchor1)
















# # span1 = p_in.find('span',class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_trustScore__8emxJ").get_text()
# print(span1_inp)
# span2_inp = p_in.find('span',class_="styles_separator__TG_uV")
# print(span_in_span1_p)
#print(above_in_div1_div1)

# below_div = soup.find('div',class_="modal_content__D8YoR")
# print(below_div)

# belowcontent = firstlist.find('div',class_="card_cardContent__sFUOe styles_footerWrapper__HMFrh")
# below_in_div1 = belowcontent.find('div',class_="styles_footer__DoJVj")
# button1 = below_in_div1.find('button',class_="styles_iconWrapper__Iy_ZV", aria-label="Contact")
# svg_web = button1.find('svg',class_="icon_icon__ECGRl")
# svg_mail = button1.find('svg',class_="icon_icon__ECGRl")

# span_in_span1_p = span1_inp.find('span',class_="styles_desktop__U5iWw")



# above_in_div1_div1_div1 = above_in_div1_div1.find('div',class_="star-rating_starRating__4rrcf star-rating_responsive__C9oka")