#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy


#基本类型我们可以用ttype()判断，那么一个对象属性我们怎么去判断呢我们用types
import types
def fn():
    pass

print(type(fn) == types.FunctionType) #True     判断方法
print(type(abs) == types.BuiltinFunctionType)   # True    属性方法
print(type(lambda x:x*x) == types.LambdaType)  #True
print(type(x for x in  range(2)) == types.GeneratorType)  #True

#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
#比如有一个类继承关系a-->b-->c
#创建实例a_1 = a(),b_1 = b(),c_1=c()

class a():
    def run(self):
        pass

class b(a):
    def run(self):
        pass

class c(b):
    def run(self):
        pass
a_1 = a()
b_1 = b()
c_1 = c()

print(isinstance(c_1,b))  #True  继承父类类型
print(isinstance(c_1,a))  #True  既有父类类型也有超父类类型   毕竟一脉相承  是不可逆的父类是没有子类类型的
#isinstance也可以做基本类型判断  如：
print(isinstance("123",str))
#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance(
    [1,2],(list,tuple)
))
''' 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽 '''

'''
dir() : 获取对象的所有属性和方法
'''
print(dir("ASD"))

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，
# 如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len("ASD") == "ASD".__len__())


#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

hasattr(obj, 'x') # 有属性'x'吗？  True
print(obj.x) #9
hasattr(obj, 'y') # 有属性'y'吗？ False
setattr(obj, 'y', 19) # 设置一个属性'y'
hasattr(obj, 'y') # 有属性'y'吗？ True
getattr(obj, 'y') # 获取属性'y' 19
print(obj.y) # 获取属性'y'  19

# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# getattr(obj, 'z') # 获取属性'z'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'MyObject' object has no attribute 'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值：
#getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

#获取对象的方法
print(hasattr(obj,"power"))  #判断是否有power函数  True
po = getattr(obj,"power")    #或取类obj中power的实例
print(po())

#一个正确的用法的例子如下：
# def readImage(fp):
#     if hasattr(fp, 'read'):  #传入一个数据流 request
#         return readData(fp)  #返回一个读后的数据流 response  （应该是吧）
#     return None

'''
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。
hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，
但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''


'''
实例属性和类属性
由于Python是动态语言，根据类创建的实例可以任意绑定属性。
给实例绑定属性的方法是通过实例变量，或者通过self变量：
'''
class Student(object):
    name = "Student"
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
print(s.name+": "+str(s.score))
#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
# class Student(object):
#     name = 'Student'
#当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：


# s = Student() # 创建实例s
print(s.name) #  Student     打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name) #  Student      打印类的name属性
s.name = 'Michael' # 给实例绑定name属性
print(s.name) #   Michael   由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name) #  Student     但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) #   Student   再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
