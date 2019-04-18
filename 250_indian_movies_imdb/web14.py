import json,pprint
with open("movies.json","r+") as file:
    movies=json.load(file)
all_5=[]
for movie in movies:
    url=(movie["Url"][28:]+".json")
    with open(url,"r+") as f:
        data=json.load(f)
        all_5.append(data["cast"][0:5])
movie_list=[]
# pprint.pprint(all_5)
for i in all_5:
    for j in i:
        # pprint.pprint(j)
        id= (j["imdb_id"])
        if id not in movie_list:
            movie_list.append(id)
# print(movie_list)
big_dict = {}
for p in movie_list:
    list_2 = []
    for r in movie_list:
        if r != p:
            khali_list = []
            khali_list.append(p)
            khali_list.append(r)
            # print(khali_list)
            count = 0
            for t in all_5:
                add = 0
                for k in t:
                    if k['imdb_id'] == p:
                        man_hero = k['Name']
                    if k['imdb_id'] == r:
                        s_hero = k['Name']
                    if k['imdb_id'] in khali_list:
                        add+=1
                if add == 2:
                    count+=1
                    add = 0
                else:
                    add = 0
            if count >= 1:
                # print(count)
                dict_1 = {"name":s_hero,"num":count}
                list_2.append(dict_1)
                # print(dict_1)
            else:
                count = 0
    big_dict[p]={'name':man_hero,"frequent_co_actors":list_2}
    pprint.pprint(big_dict)  
