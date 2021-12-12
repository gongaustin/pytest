import requests
from bs4 import BeautifulSoup
import time

def get_page(url):
    #设置浏览器代理
    #设置登录账号的cookie
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
               "Cookie":"csstype=2; access=pc; cfrom=tx; txuid=9641233; txEncodeUid=btAkbswIFS; tx.com.cn=1745070272.36895.0000; JSESSIONID=9FFC6FB7F752DACD13CF37E29CA25950; Hm_lvt_0807807898758df58fac1b03d3aece54=1596164588,1596173124,1596424255; Hm_lpvt_0807807898758df58fac1b03d3aece54=1596424255"}
    #获取页面
    r = requests.get(url,headers = headers)
    # print(r.text)
    return r.text





# n = soup.select(".seccontent2")[0].select(".a")

string = {'微博','帖子','日记','书籍','加好友','发消息','挠Ta','送礼物','>>下页','<<上页'}
def get_name(i):
    t = get_page("http://tx.com.cn/love/newpub/cs/pubIndex.do?sex=1&pn="+str(i))
    soup = BeautifulSoup(t, 'html.parser')
    for k in soup.find_all('div',class_= "seccontent2"):
        print(k.text.split("加好友.发消息.挠Ta.送礼物")[0])
        print(k.text.split("加好友.发消息.挠Ta.送礼物")[1])
        for n in k.find_all('a'):
            if(n.text not in string):
                print(n.text)

        print("-------------------")


# for i in range(1,1000):
#     get_name(i)
#     time.sleep(3)

import requests
r = requests.get('http://www.baidu.com')
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.content, 'html.parser')



print (soup.text)
