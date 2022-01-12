import pymysql as db
import requests as req
import json


conn = db.connect(host='127.0.0.1', user='root', passwd='123', db='test', charset='utf8')
cursor = conn.cursor()

sql = "select * from abc where area is null";
cursor.execute(sql)

data = cursor.fetchmany(199)
for i in data:
    # res = req.get(" https://www.baifubao.com/callback?cmd=1059&callback=phone&phone="+i[2])
    res = req.get("http://api.k780.com/?app=phone.get&phone="+ i[2] +"&appkey=63833&sign=bcda3f5460d3129c0fd03461c86bcd0e&format=json")
    res.encoding = "utf-8"
    # str_res = str(res.text).replace("/*fgg_again*/phone(","").replace("}})","}}")
    str_res = str(res.text)

    print(str_res)


    js = json.loads(str_res)
    area = js.get('result').get('att')
    print(area)
    update_sql = "update abc set area = " +"'"+ area + "'"+" where cellphone = " +"'"+ i[2] + "'"
    print(update_sql)

    cursor.execute(update_sql)
    conn.commit()


