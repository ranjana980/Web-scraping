
import requests
from bs4 import BeautifulSoup
import json
url = "https://webscraper.io/test-sites"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
e_commarce2=soup.find_all("h2")
seriol_no=1
for i in e_commarce2:
    commarce=i.find("a")["href"]
    name=i.find("a").get_text().strip()
    print(seriol_no,name)
    print("   https://webscraper.io"+commarce)
    seriol_no+=1
