
import requests
from bs4 import BeautifulSoup
import json
import pprint
all_pickels_details=[]
url1= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
page1=requests.get(url1)
soup1=BeautifulSoup(page1.text,"html.parser")
lenght1=soup1.find("span",class_="_3-is").get_text()
count=lenght1.split()
lenght=int(count[1])//32
k=1
position=1
while k<lenght:
    url = "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(k)
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    pickels_details={"position":"","name":"","price":"","url":""}
    new_post=soup.find("div",class_="_3RA-")
    post=new_post.find_all("div",class_="UGUy")
    price=new_post.find_all("div",class_="_1kMS")
    pick_url=new_post.find_all("div",class_="_3WhJ")
    i=0
    for i in (range(len(post))):
        name=post[i].get_text()
        pikels_price=price[i].get_text()
        url1=pick_url[i].a["href"]
        pickel_url="https://paytmmall.com"+url1
        pickels_details={"position":"","name":"","price":"","url":""}
        pickels_details["name"]=name
        pickels_details["position"]=position
        pickels_details["price"]=pikels_price
        pickels_details["url"]=pickel_url
        all_pickels_details.append(pickels_details)
        pprint.pprint(pickels_details)
        position+=1
        # j+=1
        i+=1  
    k+=1
# print(all_pickels_details)




