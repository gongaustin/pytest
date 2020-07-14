#!C:\Users\12550\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
#爬取全国信息

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import urllib.request
import re
from urllib.error import URLError, HTTPError


conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123', db='test', charset='utf8')
db = conn.cursor()

curr_url = ''

# 请求网页
def get_html(url):
    global curr_url
    user_agent = 'Mozilla/6.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.6796.99 Safari/537.36'
    response = urllib.request.Request(url)
    response.add_header('User-Agent', user_agent)
    response = urllib.request.urlopen(response)

    html = BeautifulSoup(response.read(), "html.parser", from_encoding='gbk')
    return html

#get_level:爬取深度
def get_list(url, level=1,  pid=0, get_level=5):
    data = [];
    level_arr = {'1': 'provincetr', '2': 'citytr', '3': 'countytr', '4': 'towntr', '5': 'villagetr'}

    try:
        print(url)
        html = get_html(url)
        c_url = url

        tr_list = html.findAll('tr', {'class': level_arr[str(level)]})
        for tr in tr_list:
            region_name, static_code, href, page = '','000000000000', '', ''
            td_list = tr.findAll('td')
            for td in td_list:
                region_name = td.get_text()
                # 判断是否存在该省份
                if (level == 1):
                    sql = "select * from region where region_name='" + region_name + "'"
                    db.execute(sql)
                    exist = db.fetchone()
                    if(exist):
                        continue

                # 判断是否全数字-非法则跳过
                if (region_name.isdigit()):
                    if(len(region_name)==12):
                        static_code = region_name
                    continue

                if (region_name):
                    sql = "insert into region(static_code,region_name,pid,level,url) value('"+static_code+"','" + region_name + "','" + str(
                        pid) + "','" + str(level) + "','" + url + "')"
                    db.execute(sql)
                    db.execute('SELECT LAST_INSERT_ID();')
                    last_id = db.fetchone()[0]

                if (td.a):
                    page = td.a.attrs['href']
                    pattern = re.compile(r'\w*.html')
                    url = re.sub(pattern, page, c_url)

                    if (level <= get_level):
                        get_list(url, level + 1, last_id)

            # 每个省份执行完成，则提交
            if (level == get_level):
                conn.commit()
        return data;
    except HTTPError as e:
        # 如果有出错，则回滚
        conn.rollback()
        print(e) # HTTP Error 502: Proxy Error


url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html'
get_list(url)
print('执行完成')