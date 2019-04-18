import requests,pprint
from bs4 import BeautifulSoup
def get_gana_list_details(url):
    url=requests.get(url)
    soup=BeautifulSoup(url.text,"lxml")
    main_div=soup.find_all("div",class_="playlist_thumb_det")
    list=[]
    for div in main_div:
        dic={}
        name=(div.find("a").text)
        href=(div.find("a")["href"])
        dic["Name"]=name
        dic["Url"]=href
        list.append(dic)
    return(list)
print ("*********Welcom to Gana.com*********")
print ("\nWe have only two types of songs\n\n1. bollywood-top-50\n2. international-top-50\n")
user=input("which type of songs you want (enter 1,2) : ")
if user=="1":
    list=get_gana_list_details("https://gaana.com/playlist/gaana-dj-bollywood-top-50-1")
    a=1
    for name in list:
        print (a,name["Name"])
        a+=1
else:
    list=get_gana_list_details("https://gaana.com/playlist/gaana-dj-gaana-international-top-50")
    a=1
    for name in list:
        print (a,name["Name"])
        a+=1
user1=input("enter song num and play the song : ")
for i in range(int(user1)):
    a=list[i]["Url"]
import webbrowser
webbrowser.open_new_tab(a)