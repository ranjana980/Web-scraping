
from task1 import scrap_top
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint
new_data=scrap_top()
year_of_movies={}
def group_by_decade(movies):
    new_year=[]
    for i in movies:
        new=i["year"]
        new_year.append(new)
    new_year.sort()
    d_year=[]
    for i in new_year:
        a=str(i)
        year=a[0:2]+str(i%100-i%10)
        if i%100-i%10==0:
            year+='0'
        if year not in d_year:
            d_year.append(year) 
    for i in d_year:
        decade_of_year = []
        for j in movies:
           if j["year"]>int(i) and j["year"]<int(i)+10:
            decade_of_year.append(j)
            year_of_movies[i] = decade_of_year
    return  year_of_movies
pprint(group_by_decade(new_data))