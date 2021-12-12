#!/usr/bin/python3
import pymongo
#面向文档存储MongoDB

#连接
client = pymongo.MongoClient(host='127.0.0.1',port=27017)

#指定数据库
db = client.test

#指定集合
connection = db.pymongo

#数据对象
student={
    "name":"MissLee",
    "age":29
}
#插入对象
result = connection.insert(student)

#打印结果，返回id
print(result)

#查询大于($eq))或者小于($lt)的数据
find = connection.find({"age": {"$lt":30}})

# result = connection.aggregate({"$group":{"count":{"$sum":1}}})

print(find)

for item in find:
    print(item)