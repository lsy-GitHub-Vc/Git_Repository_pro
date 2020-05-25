import pymysql

#链接数据库
#数据库地址  用户 密码 库名
db = pymysql.connect("localhost","root","root","lsy")

#创建一个链接对象
cursor = db.cursor()

sql = "select * from figures"

cursor.execute(sql)

#获取返回的信息
#返回一个结果集
#data = cursor.fetchone()
#返回所有结果集
data = cursor.fetchall()
print(data)


#断开
cursor.close()
db.close()