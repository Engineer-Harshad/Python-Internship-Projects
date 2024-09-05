import requests
import pandas as pd
from bs4 import BeautifulSoup
firsturl = "https://www.trustpilot.com/categories/energy_heating"
raw_data = requests.get(firsturl).text
#print(raw_data)
soup = BeautifulSoup(raw_data,'lxml')
#print(soup)
trustpilot = soup.find('section',class_="styles_feed__MNr87")
# print(trustpilot)
firstlist = trustpilot.find('div',class_="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2")
# print(firstlist)
abovecontent = firstlist.find('div',class_="styles_content__98tWf")
above_in_div1 = abovecontent.find('div',class_="styles_businessUnitMain__PuwB7")
p_tag = above_in_div1.find('p',class_="typography_heading-xs__jSwUz typography_appearance-default__AAY17 styles_displayName__GOhL2").get_text(strip = True)
print(p_tag) 

above_in_div1_div1 = above_in_div1.find('div',class_="styles_rating__pY5Pk")
p_in = above_in_div1_div1.find('p',class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_ratingText__yQ5S7")
## span1_inp = p_in.find('span',class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_trustScore__8emxJ").text
## print(span1_inp) 
spacing = p_in.split('|')
final= spacing[0] + "  " + spacing[1]
# print(final)
print(p_tag + " " + final)
# print(spacing)
# print(spacing[0] +"  "+ spacing[1])

# print(span1_inp)
# span2_inp = p_in.find('span',class_="styles_separator__TG_uV")
# print(span_in_span1_p)
#print(above_in_div1_div1)

# belowcontent = firstlist.find('div',class_="card_cardContent__sFUOe styles_footerWrapper__HMFrh")
# below_in_div1 = belowcontent.find('div',class_="styles_footer__DoJVj")
# button1 = below_in_div1.find('button',class_="styles_iconWrapper__Iy_ZV", aria-label="Contact")
# svg_web = button1.find('svg',class_="icon_icon__ECGRl")
# svg_mail = button1.find('svg',class_="icon_icon__ECGRl")


##below_div = soup.find('div',class_="modal_content__D8YoR")
## print(below_div)

# unordered = below_div.find('ul',class_="styles_list__4noUG")  
# li1 = unordered.find('li',class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_item__3AZ_v")
# anchor1 = li1.find('a href = "https://www.jedcosupply.com/?utm_medium=categories&utm_source=trustpilot&utm_campaign=domain_click/" rel="noreferrer nofollow noopener" target="_blank"  data-website-typography="true"',class_="link_internal__7XN06 typography_appearance-action__9NNRY link_link__IZzHN link_underlined__OXYVM")
# li2 = unordered.find('li',class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17 styles_item__3AZ_v")
# anchor2 = li2.find('a href = "mailto:%20sales@jedcosupply.com" rel="noreferrer nofollow noopener" target="_blank" data-email-typography="true"',class_="link_internal__7XN06 typography_appearance-action__9NNRY link_link__IZzHN link_underlined__OXYVM")
# print(anchor1)




# span_in_span1_p = span1_inp.find('span',class_="styles_desktop__U5iWw")



# above_in_div1_div1_div1 = above_in_div1_div1.find('div',class_="star-rating_starRating__4rrcf star-rating_responsive__C9oka")