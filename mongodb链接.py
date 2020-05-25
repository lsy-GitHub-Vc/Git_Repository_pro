from pymongo import MongoClient


#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库  conn.库名
db = conn.mydb

#获取集合对象db.集合名
coll = db.clas

#添加文档
coll.insert({"name":"tom","age":12,"gender":1,"address":"北京","isDelete":0})

#查询部分文档
'''
res = coll.find() #全部查询
res = coll.find().count() #统计查询
print(res)
res = coll.find({"age":{"$gt":18}})
for row in res:
    print(row)
'''
#断开
coll.colse()