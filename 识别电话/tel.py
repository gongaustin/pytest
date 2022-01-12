import pymysql as db
import requests as req
import json

conn = db.connect(host='127.0.0.1', user='root', passwd='123', db='test', charset='utf8')
cursor = conn.cursor()

sql = "select * from abc where area is null"
cursor.execute(sql)

data = cursor.fetchmany(1000)
for i in data:
    res = req.get("http://cx.shouji.360.cn/phonearea.php?number=" + i[2])
    res.encoding = "utf-8"
    str_res = str(res.text)
    js = json.loads(str_res)
    province = js.get('data').get('province')
    city = js.get('data').get('city')
    area = province+city
    update_sql = "update abc set area = " + "'" + area + "'" + " where cellphone = " + "'" + i[2] + "'"
    cursor.execute(update_sql)
    conn.commit()
    print("号码:%s的地区为:%s,数据库更新成功!" % (i[2], area))
