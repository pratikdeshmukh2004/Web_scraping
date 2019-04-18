import json
with open("movies.json") as file:
    data=json.load(file)
    data1=data
genre_list=[]
for movie in data:
    url=movie["Url"][-9:]+".json"
    with open(url,"r") as file:
        data=json.load(file)
        genre_list.append(data["Genres"])
genreList=[]
for i in genre_list:
    for j in i:
        if j not in genreList:
            genreList.append(j)
dic={}
for i in genreList:
    dic[i]=0
for gen in genreList:
    for movie in data1:
        url=movie["Url"][-9:]+".json"
        with open(url,"r") as file:
            data=json.load(file)
        if gen in (data["Genres"]):
            a=dic[gen]
            dic[gen]=a+1
print (dic)
