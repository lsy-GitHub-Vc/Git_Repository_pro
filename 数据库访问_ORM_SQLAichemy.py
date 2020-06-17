#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:SQLAlchemy
#@function:-----------

'''最有名的ORM框架是SQLAlchemy   ORM：Object-Relational Mapping'''

#https://blog.csdn.net/aimill/category_7732864.html   这里面挺详细的
'''
ORM方法论基于三个核心的原则：
    简单性：以最基本的形式建模数据。
    传达性：数据库结构被任何人都能理解的语言文档化。
    精确性：基于数据模型创建正确标准化结构。


ORM包括以下四部分：
    一个对持久类对象进行CRUD操作的API
    一个语言或API用来规定与类和类属性相关的查询；
    一个规定mapping metadata的工具；
    一种技术可以让ORM的实现同事务对象一起进行dirty checking, lazy association fetching以及其他的优化操作。
'''

#第一步，导入SQLAlchemy，并初始化DBSession：

from sqlalchemy import Column,String,Integer,Float,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationships
from sqlalchemy.ext.declarative import declarative_base
from collections.abc import Iterable,Iterator

#创建对象的基类
decl = declarative_base()

#定义stu表的对象
class Stu(decl):
    #表的名字
    __tablename__= 'stu'

    #表结构
    id = Column(Integer(),primary_key=True)
    class_id = Column(Integer())
    name = Column(String(50))
    age = Column(Integer())
    score = Column(Float())

    #如果有一对多的情况 例如：有多个个book
    # books =relationships('Book')

#初始化数据库连接
# sqlconn = create_engine('mysql+pymysql://root:root@localhost:3306/study')  #create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
                       #'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
'''使用pymysql这个驱动会有问题 插入数据时虽然能插入但是会抛出异常
E:\python37\Lib\site-packages\pymysql\cursors.py:170: Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 1")
  result = self._query(query)

所以最好安装mysql-connector-python驱动 将数据库驱动改为mysqlconnector
'''
sqlconn = create_engine('mysql+mysqlconnector://root:root@localhost:3306/study')  #创建一个引擎  engine(引擎)

#创建DBSession类型(其实就是创建一个会话对象)
DBSession = sessionmaker(bind=sqlconn)

#以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class
#由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：

#创建session对象  即实例化对象
session = DBSession()

'''插入数据'''
#创建stu对象
# new_stu = Stu(class_id = 2,name = '小卡',age = 20,score = 92.5)

#添加到session中
# session.add(new_stu)

#提交保存到数据库
# session.commit()



# 可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。

'''从数据库表中查询数据 有了ORM，查询出来的可以不再是tuple，而是我们刚才定义的Stu对象。SQLAlchemy提供的查询接口如下：'''

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# stu = session.query(Stu).filter(Stu.id == 5).one()
stu = session.query(Stu).all()
# stu = session.query(Stu).filter(Stu.name.like('%卡'))

#打印类型和属性 one()下
# print(type(stu))  # <class '__main__.Stu'>
# print(stu)       # <__main__.Stu object at 0x000001B7A0138630>
# print('id: %d,class_id: %d,name: %s,age: %d,score: %.1f' % (stu.id,stu.class_id,stu.name,stu.age,stu.score))

#打印类型和属性 all()下 （大于一条记录）
print(type(stu))  #<class 'list'>

if isinstance(stu,Iterable):
    #只能这样取多条数据吗
    for sqlobj in stu:
        print('id: %d,class_id: %d,name: %s,age: %d,score: %.1f' % (sqlobj.id,sqlobj.class_id,sqlobj.name,sqlobj.age,sqlobj.score))
else:
    print('id: %d,class_id: %d,name: %s,age: %d,score: %.1f' % (stu.id,stu.class_id,stu.name,stu.age,stu.score))

#关闭会话
session.close()

'''
可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。

由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。

例如，如果一个Stu拥有多个Book，就可以定义一对多关系如下
'''

# class Book(decl):
#     __tablename__ = 'book'
#
#     id = Column(Integer(),Primary_key = True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到stu表的:
#     stu_id = Column(Integer(),ForeignKey('stu.id'))

# 当我们查询一个Stu对象时，该对象的books属性将返回一个包含若干个Book对象的list。


'''
ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
正确使用ORM的前提是了解关系数据库的原理。
'''