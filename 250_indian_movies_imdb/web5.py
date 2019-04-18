from pprint import pprint
import json
from web4 import scrape_movie_details
with open("movies.json","r") as file:
	top_movies=json.load(file)pprint(get_movie_list_details(top_movies[:10]))	
print ("loding....")
def get_movie_list_details(movies):
	list1=[]
	for movie in movies:
		url=(movie["Url"])
		list1.append(scrape_movie_details(url))
	return list1
# pprint(get_movie_list_details(top_movies[:10]))	