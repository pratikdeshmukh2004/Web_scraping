import requests,pprint
from bs4 import BeautifulSoup
url=requests.get("https://www.giveindia.org/certified-indian-ngos")
soup=BeautifulSoup(url.text,"lxml")
table=soup.find("table",class_="jsx-697282504 certified-ngo-table")
trs=table.find_all("tr",class_="jsx-697282504")
list=[]
count=1
for tr in range(1,len(trs)):
    dic={}
    tds= (trs[tr].find_all("td"))
    dic["Name"]=(str(count)+" "+tds[0].text)
    dic["Cause"]=tds[1].text
    dic["City"]=tds[2].text
    list.append(dic)
    count+=1
pprint.pprint(list)
