import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, "xml")
year = input("Enter year : ")
for item in bs.find_all("item"):
    pub_date = item.find("pubDate").text
    if year in pub_date:
        print(item.find('title').text.strip())
