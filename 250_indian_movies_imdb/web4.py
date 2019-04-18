import requests
from bs4 import BeautifulSoup
from pprint import pprint
def scrape_movie_details(url):
	dic={}
	url=requests.get(url)
	soup=BeautifulSoup(url.text,"html.parser")
	nam=(soup.title.text)[0:-14]
	director=soup.find("div",class_="credit_summary_item").find_all("a")
	def jugad(director):
		list2=[]
		for i in director:
			d=""
			d+=i.text
			list2.append(d)
			return list2
	bio=soup.find("div",class_="summary_text").text
	url=soup.find("div",class_="poster")
	url1=url.find("img").get("src")
	dic["Name"]=nam.strip()
	dic["Director"]=jugad(director)
	dic["Bio"]=bio.strip()
	dic["Poster_image_url"]=url1.strip()
	main_div=soup.find("div",attrs={"class":'article','id':'titleDetails'})
	time=soup.find("div",class_="title_block").find("time").text.strip()
	if time[1]=="h" and time[-3:]=="min":
		dic["Runtime"]=int(time[0])*60+int(time[3:-3])
	else:
		dic["Runtime"]=int(time[0])*60
	some_div = main_div.find_all('div',class_='txt-block')
	for i in some_div:
		if i != None:
			a = i.find('h4').text
			if a=="Language:":
				alll=(i.find_all('a'))
				list2=[]
				for i in alll:
					d=""
					d+=i.text
					list2.append(d)
				dic["Language"]=list2
				break
			if a == 'Country:':
				dic["Country"]=(i.find('a').get_text())
	main_div=soup.find("div",attrs={"class":'article','id':'titleStoryLine'})
	some_div = main_div.find_all('div',class_='see-more inline canwrap')
	for i in some_div:
		if i != None:
			a = i.find('h4').text
			if a=="Genres:":
				my=(i.find_all('a'))
				list2=[]
				for i in my:
					d=""
					d+=i.text
					list2.append(d)
				break
	dic["Genres"]=list2
	return(dic)
# pprint(scrape_movie_details("https://www.imdb.com/title/tt0079221/"))