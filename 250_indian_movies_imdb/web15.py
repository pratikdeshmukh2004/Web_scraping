from web13 import cach
import json,os,pprint
list_movie=cach()
def analyse_actors(movie_list):
    dic={}
    dic2={}
    for movie in movie_list:
        cast= (movie["cast"])
        for i in cast:
            name=(i["imdb_id"])
            if name in dic:
                dic[name]+=1

            else:
                dic[name]=1
    for i in dic:
        for movie in movie_list:
            cast=movie["cast"]
            for j in cast:
                if i== (j["imdb_id"]) and i not in dic2:
                    dic2[i]={
                    "Name":j["Name"],
                    "num_movies":dic[i]
                    }
    print (dic2)
analyse_actors(list_movie)
