#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect('localhost','root','123','test')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select * from students")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchmany(10)
for i in data:
    print(i)
    print(i[0])
#插入语句
sql = "insert into students (id,name,sex,class,age) values (replace(uuid(),'-',''),%s,%s,%s,%s)"
#print ("Database version : %s " % data)
import random
value = ('龚均','男','2008级电子商务2班',random.randint(18,22))
print(cursor.execute(sql,value))
#提交，使得修改数据生效
db.commit()
# 关闭数据库连接
db.close()
print('----------------------------------------------')
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != j) and (j != k) and (i != k):
                print (i,j,k)
print('----------------------------------------------')
#打印9*9乘法表
print('\n'.join(['\t'.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))
print('----------------------------------------------')
print('李小红')
print('龚均')
print(1+1)
print('----------------------------------------------')
a=7
b=1
a=b
print(a!=b)
print('----------------------------------------------')
for i in range(1,101):


    print(i)

print(i)
print('----------------------------------------------')

#打印Python之禅
#import this
print('----------------------------------------------')
print("hello'world")
print('----------------------------------------------')
# 计算1到100中不能被3整除的数的和
sum = 0
for i in range(1,101):
    if(i%3!=0):
        sum+=i
print(sum)

#计算1到100的质数的和

print('----------------------------------------------')


import math
list=[]
for i in range (2,10):
    a = math.ceil(i/2)
    if a <=2:
        a = i
    for j in range(2,a):
        if(i%j==0):
            break
    else:
        list.append(i)
print(list)


print('----------------------------------------------')

def ReturnInfo(self,avalue,akey):
    connection = pymysql.connect("localhost","root","123","test" )
    cursor = connection.cursor()
    sql = 'select * from %s where %s=%s' % (self.table,akey,avalue)
    print(sql)
    cursor.execute(sql)
    domain_name = cursor.description
    domain_num = len(domain_name)
    sql_domain_name = [None]*domain_num
    for i in range(domain_num):
        sql_domain_name = domain_name[i][0]
    cursor.close()
    return sql_domain_name

import sqlalchemy

gongjun = [123,345]
gongjun.append("abc")
print(gongjun)

#定义一个函数
def sum(a,b,c):
    return a+b+c

#调用函数
print(sum(1,2,3))


Lee = 123

Lee = int(str(Lee))+int('456')

print(Lee)


#操作表格数据
import xlrd

data = xlrd.open_workbook('D:\香门第装修费用及材料统计.xls')

print(data.sheet_names())

table = data.sheet_by_name('装修表格')

print(table.row_values(1))


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


#读取excel的方法
def read_xlrd(excelFile):
     data = xlrd.open_workbook(excelFile)
     table = data.sheet_by_index(0)

     for rowNum in range(table.nrows):
        rowVale = table.row_values(rowNum)
        for colNum in range(table.ncols):
            if rowNum > 0 and colNum == 0:
                if(is_number(rowVale[0])):
                    print(int(rowVale[0]))
                    print('---------')
                else:
                    print(print(rowVale[0]))
                    print('---------')
            else:
                print(rowVale[colNum])
print('----------------------------------------------')

read_xlrd('D:\香门第装修费用及材料统计.xls')


gg = isinstance(11,float)

print(gg)


class A:
    pass
class B(A):
    pass

print(isinstance(B,A))

print(type(B())==A)




