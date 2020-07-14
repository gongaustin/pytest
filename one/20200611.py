from bs4 import BeautifulSoup
import requests

class tx(object):
    def __init__(self,headers):
        self.session = requests.Session
        self.header = headers
    def func(self):
        headers = {
            'Host': '172.28.14.165',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'cookie': 'JSESSIONID=' + '7BEFD3FAE8568645B4AA2ABC54719123'
        }
        response = self.session.get(url='http://tx.com.cn/love/newpub/cs/pubIndex.do?sex=1&pn=1',headers=headers, allow_redirects=False)
        sourse = BeautifulSoup(response.text, 'html.parser')
        text = sourse.find('span', {'class': 'seccontent2'})
        if not text:
            text = sourse.find('span',{'class','red'})
        tq = text.string
        print(tq)

        status = tx(headers=headers)
        status.func()
