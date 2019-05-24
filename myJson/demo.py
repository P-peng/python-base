#!/usr/bin/python3

import json

data = {
    'no' : 1,
    "name" : "志鹏",
    'url' : "http://www.baidu.com"
}

json_str = json.dumps(data)
print("python 原始信息", repr(data))
print("json 信息", json_str)

import time;  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks)