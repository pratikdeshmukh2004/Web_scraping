import requests
from bs4 import BeautifulSoup
url=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
soup=BeautifulSoup(url.text,"lxml")
tbody= soup.find("tbody",class_="lister-list")
trs=tbody.find_all("tr")
list_name=[]
url_list=[]
for tr in trs:
    td = tr.find('td',class_="titleColumn").a.text
    url="https://www.imdb.com/"+(tr.find('td',class_="titleColumn").a["href"][:16])
    list_name.append(td)
    url_list.append(url)
for i in range(len(list_name)):
    print (i+1,list_name[i])
user=int(input("Enter movie number : "))
for i in range(user):
    a=url_list[i]
url2=requests.get(a).text
soup2=BeautifulSoup(url2,"lxml")
div=soup2.find("div",class_="slate").a["href"]
link =("https://www.imdb.com/"+div)
import webbrowser
webbrowser.open_new_tab(link)
