#!/usr/bin/python3

import pymongo

print("升序排列")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydoc = mycol.find().sort("alexa")
for x in mydoc:
    print(x)
print("--------------------------------------")

print("降序排列")
mydoc = mycol.find().sort("alexa", -1)
for x in mydoc:
    print(x)