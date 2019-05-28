#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

dblist = myclient.list_database_names()
# dblist = myclient.database_names()

print(dblist)

if "runoobdb" in dblist:
    print("数据库已存在！")
else:
    print("数据库不存在")