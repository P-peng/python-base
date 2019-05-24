#!/usr/bin/phtyon3
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","omt2018","t" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 编写sql语句
sql = "INSERT INTO t VALUES(null,'686')"

try:
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()


# 关闭数据库连接
db.close()


