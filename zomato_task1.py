from selenium import webdriver
from bs4 import BeautifulSoup
def task1():
    driver=webdrivckkbsvhzbjkchjhhzbcacker.Chrome()
    driver.get("https://www.zomato.com/ncr")
    page=driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    soup=BeautifulSoup(page,"lxml")
    maindiv=soup.find("div",class_="ui segment row")
    divs=maindiv.find_all("a",class_="col-l-1by3 col-s-8 pbot0")
    s=1
    url_list=[]
    for i in divs:
        dic={}
        a=i.text.strip()
        url_list.append(i["href"])
        add=''
        for j in a:
            if j=="(":
                dic[s]=add.strip()
                add=""
                continue
            add+=j
        dic["Tota_restorents"]=add[:-1]
        # print (dic)
        s+=1
    return url_list
task1()
