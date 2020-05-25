'''
1、lambda 只是一个表达式
2、lambda有自己的命名空间  不能访问列表之外的或全局命名的参数变量
3、他和c的内联函数不同 c是为了效率而存在的

'''

s1 = lambda num1,num2:num1+num2

print(s1(1,2))

'''
Python 中 map和reduce 的用法

首先是map：接受两个参数，第一个是函数，第二个是一个可迭代的的参数（Iterable）

如下例子，我们定义一个函数f(x)=x^2
'''
#map的用法
def func(x):
    return x*x
m=map(func,range(1,8))
print(list(m))
#输出 [1, 4, 9, 16, 25, 36, 49]
'''
这段代码的意思就是将1到7一次传入到函数func，返回值存在迭代器（Iterator）中，再转化为list输出。

我们再来看看传入多个（Iterable）参数
'''
def func(x,y):
    return x+y
m=map(func,range(1,8),range(3,6))
print(list(m))            #返回的是一个内存地址 加list后变为一个列表

#输出结果：4(1+3),6(2+4),8(3+5)
'''
可见，如果传入的是多个Iterator，则按照元素最少的为准

再来看看reduce的用法。

reduce接受两个参数，第一个参数是一个函数，第二个参数是一个可以迭代的类型（Iterable）
第一个参数的函数也必须接受两个参数，reduce会把函数的返回值与序列的写一个元素继续传入函数做计算。

如下例子，求从1加到100的值

reduce 将函数的到的结果继续当做参数传入到函数中去
'''
from functools import reduce

def add(x,y):
    return x+y
print(reduce(add,range(100)))
#输出结果：4950

'''
接下来设计一个场景将map和reduce这两个函数都综合的用上

现在给定一个str类型的数，例如’1234’，我们要求出其对应的每个元素相加后的和

首先定义个函数将字符串转化为数字列表：如’1234’->[1,2,3,4]
'''
def charToNum(str):
    return int(str)
#接下来写一个函数计算这个数字列表里面所有值的和

def numToNumber(x,y):
    return x+y

#接下来使用map和reduce完成这个场景

def charToNumber(s):
    def charToNum(str):
        return int(str)
    def numToNumber(x,y):
        return x+y
    return reduce(numToNumber,list(map(charToNum,s)))

print(charToNumber('345789'))

#sdsds