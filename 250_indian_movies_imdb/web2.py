import json,pprint
with open("movies.json","r") as file:
	movies=json.load(file)
def group_by_year(movies):
	years=[]
	for movie in movies:
		if movie["year"]  not in years:
			years.append(movie["year"] )
	dic={}
	for year in years:
		year_list=[]
		for movie in movies:
			if year==movie["year"]:
				year_list.append(movie)
		dic[year]=year_list
	return(dic)
	with open("movies1.json","w") as file:
			data=json.dumps(dic)
			file.write(data)
# pprint.pprint(group_by_year(movies))
# ********************************************3 task 3***************************************************
