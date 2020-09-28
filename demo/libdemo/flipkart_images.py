import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.flipkart.com")
bs = BeautifulSoup(resp.text, "html.parser")

for tag in bs.find_all("img"):
    if 'src' in tag.attrs:
        print(tag['src'])


