from task1 import scrap_top
import requests
import json
from bs4 import BeautifulSoup
import pprint 
scrapped=scrap_top()
def group_by_year(movies):
    year_of_movie=[]
    for year in movies:
        top_year=year["year"]
        if top_year not in year_of_movie:
            year_of_movie.append(top_year)
    year_of_movie.sort()
    movie_dict={i:[] for i in year_of_movie}
    for i in movies:
        year=i['year']
        for j in movie_dict:
            if str(j)==str(year):
                movie_dict[j].append(i)
    with open("task.json","w") as task1:
        json.dump(movie_dict,task1,indent=4)
    return movie_dict
print(group_by_year(scrapped))

