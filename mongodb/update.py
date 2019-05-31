#!/usr/bin/python3

import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["runoobdb"]
my_col = my_db["sites"]

my_query = {"alexa" : "10000"}
new_values = { "$set": { "alexa": "12345" } }
my_col.update_one(my_query, new_values)

results = my_col.find()
for reslut in results:
    print(reslut)
print("--------------------------------------------------")

# 正则匹配修改
my_query = {"name": {"$regex": "^F"}}
new_values = {"$set": {"alexa": "123"}}
x = my_col.update_many(my_query, new_values)
print(x.modified_count, "文档已修改")