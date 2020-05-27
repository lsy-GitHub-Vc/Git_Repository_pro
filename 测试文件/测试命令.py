from copy import deepcopy
import copy
import sys

dic = {"a":"A","b":"B"}
new_dict = {y:x for x,y in dic.items()}
print(new_dict)


a=100
b=100
print(a is b)
print(a == b)

c=257
d=257
print(c is d)
print(c == d)


e=["h"]
f=["h"]
print(e is f)
print(e == f)


lis = [0,1,2,3,4,5,["a","b","c"]]
lis1 = lis
lis2 = lis.copy()
lis3 = copy.deepcopy(lis)


lis.append(6)
lis[6].append("d")

print(lis1)
print(lis2)
print(lis3)

import math
import random

print(abs(-100))

print(
    math.floor(3.1),math.fabs(-100),math.ceil(3.1),math.fmod(40.4,4),math.modf(10.2),math.sqrt(16),
        random.choices(['1','2','3','4']),random.choice(['1','2','3','4']),int(random.random()*10),random.randint(1,10),random.randrange(11,30,2)
)

import time
import calendar

# for x in range(10):
#     print(time.perf_counter())
#     print(time.perf_counter_ns())
#     print('@@@@@@@@@')

# print(calendar.calendar(2020))
print(calendar.month(2020,5))
print(time.perf_counter())
print(time.process_time())
print(time.ctime())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.localtime())
print(time.strftime('%y-%m-%d %H-%M-%S',time.localtime()))

import collections
listp = ['1','2','3','4','5']
que = collections.deque()
listd = ['6','7','8','9','10']
while len(listd) != 0 :
    for qus in listd:
        que.appendleft(qus)
        listd.remove(qus)
print(que)

import os

# fileread = open(r"E:\PyCharm\project_1\文档\git.txt","r",encoding="utf-8")
# filewrith = open(r"E:\PyCharm\project_1\文档\ceshifile.txt","w+",encoding="utf-8")
# filestr = fileread.read()
# filestr = fileread.readlines()
# print(filestr)
# for f in range(5):
#     filewri = fileread.readline().strip()
#     filewrith.write(filewri+"\n")
# fileread.close()
# filewrith.close()

# with (open(r"E:\PyCharm\project_1\文档\git.txt","r",encoding="utf-8")) as filecs:
#     with (open(r"E:\PyCharm\project_1\文档\git_1.txt","w+",encoding="utf-8")) as filewi:
#         for i in range(5):
#             filewi.write(filecs.readline())

import contextlib

# @contextlib.contextmanager
#
# def context (path):
#     filek = open(path,"w+",encoding="utf-8")
#     try:
#         yield filek
#     finally:
#         filek.close()
#
# with (context("E:\PyCharm\project_1\文档\ceshifile.txt")) as filefr:
#     filefr.write("1111111111111111111")


import pickle

# listlo = ['a','b','4','g']
# dictlo = {"a":"d","f":"g"}
# tuplelo = ("1","g","4","jj")
# setlo = set("strmg")
# # with (open(r"E:\PyCharm\project_1\文档\pickda.txt","ab+")) as filepi:
# #     pickle.dump(setlo,filepi)
#
# with (open(r"E:\PyCharm\project_1\文档\pickda.txt","rb+")) as filepk:
#     for i in range(5):
#         print(pickle.load(filepk))

# listisin = ["a","s","d"]
# listlirt = iter(listisin) #转换为一个可迭代对象
# for i in range(len(listisin)):
#     print(next(listlirt))


# 将方法属性化
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
#
# pr = Student()
# pr.score = 10
# print(pr.score)


# def decorate(func):
#     def inner(*args,**kwargs):
#         print(args)
#         if int(args[0]) >18 :
#             print("*********************")
#         else:
#             print("______________________")
#         func(*args,**kwargs)
#     return inner
#
# @decorate
# def nier(age):
#     print("**************%s" % (age))
#
# nier(20)
#
# class Student(object):
#
#     @property
#     def birth(self):
#         print(2)
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         print("1*****"+str(value))
#         self._birth = value
#
#     @property
#     def age(self):  #这个只存在只读属性
#         print(3)
#         return 2014 - self._birth
#
# Stu = Student()
# # Stu.birth = 10
# # print(Stu.age)
# Stu.birth = 20
# print(Stu.age )

import functools

# def pfunc(str,base=2):
#     return int(str,base=2)
# print(pfunc("101010"))

# bas = functools.partial(int,base=2)
# print(bas("1010"))

# def mapr(x,y):  #可以是一个参数
#     return math.pow(x,y)
#
# print(list(map(mapr,range(1,5),range(3,8))))       #返回的是一个内存地址 加list后变为一个列表

#
# def addnum(x,y):
#     return x+y
#




import os
print(os.name)#获取操作系统类型
# print(os.environ) #获取环境变量
# print(os.environ.get("ALLUSERSPROFILE")) #获取某一环境变量的详细信息
# print(os.curdir) #获取当前路径
print(os.getcwd()) #当前运行路径
print(os.listdir(r"E:\PyCharm\project\文档")) #路径下的所有文件
# print(os.mkdir(r"E:\PyCharm\project\文档\qw.txt"))#创建文件夹
# print(os.rmdir(r"E:\PyCharm\project\文档\qw.txt")) #删除文件夹
print(os.stat(r"E:\PyCharm\project\文档\git.txt")) #文件类型
# print(os.system("msconfig")) #打开某应用
# print(os.system("ps -ef | grep PyCharm")) #执行系统路径
print(os.path.abspath('.')) #当前绝对路径
# print(os.path.join("E:\PyCharm\project_1\文档","qw.txt") #拼接路径
print(os.path.split(r"E:\PyCharm\project\文档\git.txt")) #分割路径
print(os.path.splitext(r"E:\PyCharm\project\文档\git.txt")) #获取文件扩展名
print(os.path.dirname(r"E:\PyCharm\project\文档\git.txt"))
print(os.path.basename(r"E:\PyCharm\project\文档\git.txt"))
print(os.path.isdir(r"E:\PyCharm\project\文档")) #判断是否为文件
print(os.path.isfile(r"E:\PyCharm\project\文档")) #判断文件是否存在
print(os.path.isabs(r"E:\PyCharm\project\文档\git.txt")) #感觉是 是否为文件最底层的绝对路径
print(os.path.exists(r"E:\PyCharm\project\文档")) #判断目录是否存在
print(os.path.getsize(r"E:\PyCharm\project\文档\git.txt"))#文件字节
