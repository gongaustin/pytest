import pymysql as db
import requests as req
import json


conn = db.connect(host='127.0.0.1', user='root', passwd='123', db='test', charset='utf8')
cursor = conn.cursor()

sql = "select * from abc";
cursor.execute(sql)

data = cursor.fetchmany(1500)
for i in data:
    res = req.get(" https://www.baifubao.com/callback?cmd=1059&callback=phone&phone="+i[2])
    res.encoding = "utf-8"
    str_res = str(res.text).replace("/*fgg_again*/phone(","").replace("}})","}}")


    js = json.loads(str_res)
    area = js.get('data').get('area')
    print(area)
    update_sql = "update abc set area = " +"'"+ area + "'"+" where cellphone = " +"'"+ i[2] + "'"
    print(update_sql)

    cursor.execute(update_sql)
    cursor.commit()



