#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy



#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Students(object):
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self.name = name
        self.age = age


#的绑定属性
s=Students("xiaoming",92)
print(s.name+":  "+str(s.age))


#给实例绑一个方法
def stu(self,age):
    self.age = age

#from types import MethodType
#可以通过上面的包给实例绑一个方法 不过就绑定的实例可以调用  Students其他的实例访问不到  所以最好用下面的方法绑定一个该类的实例都可访问该方法的函数

Students.stu = stu   #这样 该类的实例都可访问   动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

'''
__slots__  :Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性  对子类不起作用哦
在创建类时(如果没有使用__slots__属性),python会为每个实例串讲一个__dict__属性,以字典的形式存放每个实例的属性
'''
#print(s.__dict__)   #类内加上__slots__ 就不存在__dict__这个属性了AttributeError: 'Students' object has no attribute '__dict__

# s.score = 95
# print(s.score)


