from web5 import get_movie_list_details
import json
with open("movies.json","r") as file:
	top_movies=json.load(file)
movie_list=get_movie_list_details(top_movies[:10])
def analyse_movies_directors(movie_list):
	list_=[]
	for movies in movie_list:
		lan=movies["Director"]
		list_.append(lan)
	data=[]
	dic={}
	for i in list_:
		for j in i:
			if j not in data:
				data.append(j)
	for h in data:
		dic[h]=0
	for d in data:
		for i in list_:
			for j in i:
				if d==j:
					a=dic[d]
					dic[d]=a+1
	return dic
pprint.pprint(analyse_movies_directors(movie_list))
