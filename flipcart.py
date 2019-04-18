import requests,webbrowser,pprint
from bs4 import BeautifulSoup
def function(url):
    url=requests.get(url)
    soup=BeautifulSoup(url.text,"lxml")
    main_div=soup.find_all("div",class_="_1UoZlX")
    main_a_tag=soup.find_all("a",class_="_31qSD5")
    list1=[]
    for div in main_div:
        dic={}
        mobi_name= (div.find("div",class_="_3wU53n").text)
        mobi_price=(div.find("div",class_="_1vC4OE _2rQ-NK").text)
        mobi_rating=(div.find("div",class_="hGSR34"))
        details=div.find_all("li",class_="tVe95H")
        dic["Memory"]=details[0].text
        dic["Display"]=details[1].text
        dic["Camera"]=details[2].text
        dic["Battry"]=details[3].text
        dic["Prosser"]=details[4].text
        if len(details)>5:
            dic["Warranty"]=details[5].text
        dic["Name"]=mobi_name
        dic["Price"]=mobi_price
        if not(mobi_rating == None):
            dic["Ratting"]=mobi_rating.text
        list1.append(dic)
    pprint.pprint(list1)
user=input("aapako kaunsa page chaiye : ")
function("https://www.flipkart.com/search?q=Redmi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+user)
