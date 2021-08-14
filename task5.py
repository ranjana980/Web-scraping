from task1 import scrap_top
#from task4 import scrape_movie_details
import requests
import json
from bs4 import BeautifulSoup 
movie=scrap_top()
movie_url=[]
i=0
while i<10:
    url=(movie[i]["url"])
    movie_url.append(url)
    i+=1
def get_movie_list_details(movies_list):
    movie_list=scrap_top()
    ten_movie=[]
    directer=[]
    lanuage=[]
    country=[]
    genre=[]
    def scrape_movie_details(movie_url):
        for j in movies_list:
            move_api= j
            movie_url2=requests.get(move_api)
            soup1=BeautifulSoup(movie_url2.text,"html.parser")
            directer_name=soup1.find("div",class_="credit_summary_item").a.get_text()
            directer.append(directer_name)
            details = soup1.find("div",attrs={"class":"article","id":"titleDetails"})
            div_list = details.find_all("div")
            for i in div_list:
                run=i.find_all("h4")
                for j in run:
                    if "Language:" in j:
                        lan=i.find_all("a")
                        for lang_uage in lan:
                            movie_language=lang_uage.get_text()
                            lanuage.append(movie_language)
                    elif "Country:" in j:
                        con=i.find_all("a")
                        for con_try in con:
                            movie_country=con_try.get_text()
                            country.append(movie_country)
            post_img_url=soup1.find("div",class_="poster").img["src"]
            bio=soup1.find("div",class_="summary_text").get_text()
            new_bio=bio.split()
            m_bio=""
            for i in new_bio:
                m_bio+=" "
                m_bio+=i
            movie=soup1.find("h1",class_="").get_text()
            movie_split=str(movie[0:len(movie)-7])
            movie=movie_split.split()
            m_movie=""
            for i in movie:
                m_movie+=" "
                m_movie+=i
            co=soup1.find('div',class_="subtext")
            genre=co.find_all("a")
            genre.pop()
            movie_genre=[i.get_text() for i in genre]
            runtime=co.find('time').get_text().strip()
            main_time=runtime[0:len(runtime)-(len(runtime)-1)]
            main_time1=runtime[2:len(runtime)-3]
            time=int(main_time)*60+int(main_time1)
            movie_details={"name":" ","director":" ","country":" ","language":" ","poster_image_url":" ","bio":" ","runtime":" ","genre":" "}
            movie_details["name"]=m_movie
            movie_details["director"]=directer
            movie_details["country"]=country
            movie_details["language"]=lanuage
            movie_details["poster_image_url"]=post_img_url
            movie_details["bio"]=m_bio
            movie_details["runtime"]=time
            movie_details["genre"]=movie_genre
            ten_movie.append(movie_details)
        return ten_movie
    print(scrape_movie_details(movie_list))
get_movie_list_details(movie_url)

   
