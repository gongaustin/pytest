# -*- coding: utf-8 -*-

import pymysql
import random
import pandas as pd
import matplotlib.pylab as mtp
import numpy as np

# 数据库连接
db_conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="123",
    database="test",
    port=3306,
    charset="utf8"
)

# 插入数据库
# cursor = db_conn.cursor()
# sql_cmd = "INSERT INTO kimbo_test (id,order_id,valid_amt,coll_amt,product_type,one_dept) VALUES (REPLACE(UUID(),'-',''),REPLACE(UUID(),'-',''),%s,%s,%s,%s);"
# for i in range(1,1000):
#     value = (random.randint(0,5000),random.randint(100,50000),random.randint(0,10),random.randint(1,100))
#     cursor.execute(sql_cmd,value)
# db_conn.commit()

sql_cmd = "select id,order_id,valid_amt,coll_amt,product_type,one_dept from kimbo_test;"


# 执行sql语句
sql_cmd = "select id,order_id,valid_amt,coll_amt,product_type,one_dept from kimbo_test;"

# 导入数据
data1 = pd.read_sql(sql_cmd, db_conn)

# 数据清洗，发现缺失值
c = 0

data2 = data1.values  # 转换成DateFrame模式
rows = len(data2)  # 行数
cols = len(data2[0])  # 列数
# print(data2)
print(rows, cols)

for i in range(rows):
    for j in range(cols):
        if (data2[i][j] == "NULL"):
            data2[i][j] = None
        if (data2[i][2] >= 1000):
            data2[i][2] -= 100
            c += 1
print("总共修改数值：%d" % c)

data3 = data2.T  # 行列转换
price = data3[2]  # 价格
amt = data3[3]  # 金额
pricemax = data3[2].max()
pricemin = data3[2].min()
amtmax = data3[3].max()
amtmin = data3[3].min()

# 极差 最大值-最小值
pricediff = pricemax - pricemin
amtdiff = amtmax - amtmin
# 组距 极差/组数
pricedst = pricediff / 7
amtdst = amtdiff / 7
# 根据组距 切分
pricesty = np.arange(pricemin, pricemax, pricedst)
amtsty = np.arange(amtmin, amtmax, amtdst)

# 散点图
mtp.subplot(2, 1, 1)
mtp.plot(price, amt, 'o')
mtp.title("ctp")

# # 画价格的直方图
# mtp.subplot(2, 2, 3)
# mtp.hist(data3[2], pricesty, color='y')
# mtp.title("pri")
#
# 画金额的直方图
# mtp.subplot(2, 2, 4)
# mtp.hist(data3[3], amtsty, color='b')
# mtp.title("amt")
mtp.show()


path="D:\香门第装修费用及材料统计.xls"

df = pd.read_excel(path,dtype=object)
df.info()

# df.序号