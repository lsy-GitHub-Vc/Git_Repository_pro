#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:MySQL
#@function:-----------
'''MySQL'''

'''
在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。

在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。
MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：
[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci
'''
#注：如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4，utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。


import pymysql

#链接数据库
#数据库地址  用户 密码 库名
db = pymysql.connect("localhost","root","root","study")

#创建一个链接对象
cursor = db.cursor()

#  例： 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.rowcount
# 1
# # 提交事务:
# db.commit()
# cursor.close()
#这些和sqllit一样的

#插入多条数据 例：
# sql = "INSERT INTO userinfo(username,passwd) VALUES(%s,%s)"
# cursor.executemany(sql,[("tom","123"),("alex",'321')])

#获取返回的信息
#返回一个结果集
#data = cursor.fetchone()
#返回所有结果集
#data = cursor.fetchall()
data = cursor.execute('SELECT * FROM stu')  #返回的为受影响的行数
values = cursor.fetchall()  #返回数据

print(data,values)

#断开
cursor.close()
db.close()