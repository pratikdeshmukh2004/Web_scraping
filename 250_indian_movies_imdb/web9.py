import os,json,time,random
from web1 import scrape_top_list
from web4 import scrape_movie_details
movies=scrape_top_list()
for i in movies:
	# time.sleep(random.randint(5,10))
	url=i["Url"][-9:]+".json"
	if not(os.path.exists(url)):
		all_movies=scrape_movie_details(i["Url"])
		with open(url,"w") as file:
			data=json.dumps(all_movies)
			file.write(data)
		print ("nahi thi")
	else:
		print("hai")
