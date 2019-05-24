import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","omt2018","t" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 编写sql语句
sql = "SELECT * FROM t"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        var = row[1]
        print( "id = ",id,"var = " + var )
except:
    print("selelct t table error")


sex = "kk"
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = " + sex

print(str)
print(sql)

