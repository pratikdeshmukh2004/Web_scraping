import urllib.request
import pprint,webbrowser
from bs4 import BeautifulSoup
url=urllib.request.urlopen("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
soup=BeautifulSoup(url,"lxml")
maindiv=soup.find("div",class_="cb-col cb-col-100 cb-padding-left0")
all_names=maindiv.find_all("a",class_="text-hvr-underline text-bold cb-font-16")
position=maindiv.find_all("div",class_="cb-col cb-col-16 cb-rank-tbl cb-font-16")
citys=maindiv.find_all("div",class_="cb-font-12 text-gray")
rating=maindiv.find_all("div",class_="cb-col cb-col-17 cb-rank-tbl pull-right")
list=[]
all_list=[]
for i in range(len(all_names)):
    dic={}
    dic["Name"]= (all_names[i].text)
    dic["position"]=(position[i].text)
    dic["Country"]=citys[i].text
    dic["Rating"]=rating[i].text
    all_list.append(dic)
    list.append(all_names[i]["href"])
pprint.pprint(all_list)
user=int(input("enter the position of player which you want : "))
webbrowser.open_new_tab("https://www.cricbuzz.com/"+list[user-1])
