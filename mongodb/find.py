#!/usr/bin/python3
import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["runoobdb"]
my_cal = my_db["sites"]

x = my_cal.find_one()
print(x)
print("--------------------------------------------")

# 查找所有
my_cal = my_db["site2"]
lists = my_cal.find()
for list in lists:
    print(list)
print("--------------------------------------------")

# 筛选字段
lists = my_cal.find({}, { "_id": 0, "name": 1, "address": 1})
for list in lists:
    print(list)
print("--------------------------------------------")

# 条件查找
condition = {"name" : "Google"}
lists = my_cal.find(condition)
for list in lists:
    print(list)
print("--------------------------------------------")
