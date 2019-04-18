import os,json,pprint,time,random
from web1 import scrape_top_list
from web12 import actores
def cach():
    movies=scrape_top_list()
    all_data=[]
    for i in movies:
        url=i["Url"][-9:]
        with open(url+".json","r") as file:
        		data=json.load(file)
        j_url=url+".json"
        if not(os.path.exists(j_url)):
            print ("hi")
            url2="https://www.imdb.com/title/"+url+"/fullcredits?ref_=tt_cl_sm#cast"
            data["cast"]=actores(url2)
            with open(j_url,"w+") as file:
                d_data=json.dumps(data)
                file.write(d_data)
        all_data.append(data)
    return all_data
# pprint.pprint(cach())
