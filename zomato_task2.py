from zomato_task1 import task1

from selenium import webdriver
from bs4 import BeautifulSoup
import time,random,json
h_list=task1()
list=[]
for i in h_list:
    dic12={}
    driver=webdriver.Chrome()
    driver.get(i)
    page=driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    soup=BeautifulSoup(page,"lxml")
    time.sleep(random.randint(0,5))
    a_tag=soup.find_all("a",class_="zred")
    for j in a_tag:
        driver2=webdriver.Chrome()
        driver2.get(j["href"])
        page2=driver2.execute_script("return document.documentElement.outerHTML")
        driver2.quit()
        soup2=BeautifulSoup(page2,"lxml")
        maindiv=soup2.find_all("div",class_="col-s-12")
        ids=(soup2.find_all("div",class_="ta-right floating search_result_rating col-s-4 clearfix"))
        md=(soup2.find_all("div",class_="search-page-text clearfix row"))
        votes=(soup2.find_all("div",class_="ta-right floating search_result_rating col-s-4 clearfix"))
        for d in range(len(votes)):
            a1=(maindiv[d].text.strip().split("\n"))
            vote= (votes[d].text.strip().split("\n"))
            if len(a1)==5:
                dic12["Name"]=a1[1]
            else:
                dic12["Name"]=a1[0]
            dic12["place"]=a1[-1]
            dic12["Ratting"]=vote[0]
            dic12["Votes"]=vote[-1]
            dic12["Id"]=ids[d].find("div").get("data-res-id")
            dic12["price"]= (md[d].find("span",class_="col-s-11 col-m-12 pl0").text[1:])
            list.append(dic12)
with open ("zomatodata.json","w+") as file:
    dara=json.dumps(list)
    file.write(dara)
print (list)
