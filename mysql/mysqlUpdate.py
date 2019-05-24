#!/usr/bin/phtyon3
# 总结严格区别 字符 和 整形 ，用java不同，转换字符没那么随意
#

# 打开数据库连接
import pymysql

db = pymysql.connect("localhost","root","omt2018","t" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 编写sql语句
name = "邓志鹏"
id = 11
sql = "UPDATE t SET name = '" + name + "' WHERE id = " +  id.__str__()
print(sql)
try:
    print(cursor.execute(sql))
    # 提交到数据库执行
    db.commit()
except BaseException as e:
    # 发生错误时回滚
    db.rollback()
    print("update t table error" + e)
