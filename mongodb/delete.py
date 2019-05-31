#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

myquery = {"name": "Taobao"}

mycol.delete_one(myquery)

# 删除后输出
for x in mycol.find():
    print(x)
print("--------------------------------------------")

# 正则匹配删除
myquery = {"name": {"$regex": "^F"}}
x = mycol.delete_many(myquery)
print(x.deleted_count, "个文档已删除")