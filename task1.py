
import requests
from bs4 import BeautifulSoup
import json
def scrap_top():
    movie_name=[]
    movie_year=[]
    movie_position=[]
    movie_rating=[]
    movie_url=[]
    url ="https://www.imdb.com/chart/top/"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    main_div=soup.find('div',class_='lister')
    trs=soup.find_all('td',class_="titleColumn")
    link="https://www.imdb.com"
    i=1
    for positoin in trs:
        correct_name=(positoin).a.get_text()
        movie_name.append(correct_name)
        correct_year=(positoin).span.get_text()
        year=correct_year[1:5]
        correct_url=link+(positoin).a['href']
        movie_url.append(correct_url)
        movie_year.append(year)
        movie_position.append(i)
        i+=1
    rate_all=soup.find_all('td',class_="ratingColumn imdbRating")
    for rate in rate_all:
        correct_rate=(rate).strong.get_text()
        movie_rating.append(correct_rate)
    total=[]
    top_movies={"name":'',"year":'',"position":'',"rating":'',"url":''}
    index=0
    while index<len(trs):
        top_movies["name"]=str(movie_name[index])
        top_movies["year"]=int(movie_year[index])
        top_movies["position"]=int(movie_position[index])
        top_movies["rating"]=float(movie_rating[index])
        top_movies["url"]=movie_url[index]
        total.append(top_movies.copy())
        top_movies={"name":'',"year":'',"position":'',"rating":'',"url":''}
        index+=1
    return total

print(scrap_top())