#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy

'''SQLlte'''

'''
SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，
甚至在iOS和Android的App中都可以集成。

在使用SQLite前，我们先要搞清楚几个概念：

表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。

要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；

连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。

由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。
'''

#我们在Python交互式命令行实践一下：

import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:

conn = sqlite3.connect('test.db',timeout=5,) #创建连接

cursor = conn.cursor() #创建一个游标对象

#来条sql执行下
# cursor.execute('CREATE table user(id varchar(10) primary key,name varchar(5))')

#插入一条数据
# cursor.execute('INSERT INTO user(id,name) VALUES (\'1\',\'lsy\')' ) #<sqlite3.Cursor object at 0x00000204A99F4D50>
# cursor.execute('INSERT INTO user(id,name)VALUES (\'2\',\'ting\')')

#查询 获取表内数据
print(cursor.execute('SELECT id,name FROM user').fetchall())  #在sqllit中这个返回的是结果对象 而在mysql中返回的是受影响的行数 所以在sqllit中可以这么写

cursor.close()   #关闭游标

#提交事务
conn.commit()

print(cursor.rowcount)  #通过rowcount获得插入的行数

#关闭连接
conn.close()

'''
使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。

使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
'''

# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

'''
小结
在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。

要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。

'''