#顺序查找--线性查找(linear_search)

import pymysql as db


def linear_search(li,val):
    for index,value in enumerate(li):
        print(value)
        if value == val:
            return index



def linear_search_2(set,val):
    n = 0
    for i in range(0,len(set)):
        # print(set[i])
        if set[i] == val:
            n = n + 1
    return n

cars = ["轿车","suv","自行车"]

a = linear_search_2([2,2,2,3,3,6,2,8,9,22,2,12,11],2)

print(a)


def connect(sql):
    test = db.connect('localhost','root','123','test')
    cursor = test.cursor()   #创建游标
    cursor.execute(sql)      #执行
    data = cursor.fetchmany(10)  #设置行数
    for i in data:
        print(i[0])

connect('select * from student')

