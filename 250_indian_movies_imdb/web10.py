import json,pprint
with open("movies.json","r") as file:
    data_data=json.load(file)
    data=data_data
    movie_list=[]
    lan_list=[]
def jugad(list):
    director_list=[]
    for i in list:
        for j in i:
            if j not in director_list:
                director_list.append(j)
    return director_list
for movie in data:
    url=movie["Url"][-9:]+".json"
    with open(url,"r") as file:
        data=json.load(file)
    director=data["Director"]
    language=data["Language"]
    movie_list.append(director)
    lan_list.append(language)
    director_list=jugad(movie_list)
    lang_list=jugad(lan_list)
# print (director_list)
# print (lang_list)

mainDic={}
# print(data)
sameLanguage=[]

for i in director_list:
    dic={}
    for j in lang_list:
        # print (j)
        count = 0
        for movie in data_data:
            url=movie["Url"][-9:]+".json"
            with open(url,"r") as file:
                data=json.load(file)
                directorList=data["Director"]
                langaugeList=data["Language"]
                if i in directorList:
                    if j in langaugeList:
                        count+=1
        if count>0:
            dic[j]=count
    mainDic[i]=dic
pprint.pprint(mainDic)








    # dic[  director]=language
# pprint.pprint(dic)
