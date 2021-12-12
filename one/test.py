from bs4 import BeautifulSoup

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
a = requests.get("https://www.baidu.com",headers = headers)
soup = BeautifulSoup(a.content,"html.parser")
b = soup.find("百度")
print(b)