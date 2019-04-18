import requests,pprint
from bs4 import BeautifulSoup
url=("https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast")
def actores(url):
    url=requests.get(url)
    soup=BeautifulSoup(url.text,"lxml")
    table=soup.find("table",class_="cast_list")
    a_tags=table.find_all("td",class_="primary_photo")
    img_tags=table.find_all("img")
    loop=0
    list=[]
    for img in img_tags:
        dic={}
        dic["Name"]=(img.get("title"))
        dic["imdb_id"]=(a_tags[loop].find("a")["href"][6:15])
        loop+=1
        list.append(dic)
        if loop==16:
            break
    return(list)
