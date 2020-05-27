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

from functools import reduce
# print(reduce(addnum,range(100)))

from collections.abc import Iterable

def addnumber( str):
    if isinstance(str,Iterable) is True:
        return reduce(lambda x,y:x+y,list(map(lambda x:int(x),str)))
    else:
        print(str+" 不是一个可迭代对象")

def addlist(str1):
    if isinstance(str1,Iterable) is True:
        listn = list()
        i = 0
        listz = list(map(lambda x:int(x),str1))
        while len(listz) != 1:
            listn.append(str(listz[i]+listz[i+1]))
            listz.pop(i)
        return "".join(listn)
print(addnumber("123456789"))
print(addlist("123456789"))

'''
filter
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
#用filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 注意这是一个生成器，并且是一个无限序列。
# 然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0
#最后，定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件
# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break


'''
sorted()函数
'''
from operator import itemgetter
# （1）对list排序
#和list的sort函数一样吧
#（2）sorted 这里面可以传一个参数 根据参数的规则排列
print(sorted([1,4,-1,-5,6,0,-9],key=abs)) #根据绝对值排序
print(sorted(['hello','My','Dad','gril'],key=str.upper)) #排序 自然是根据ASCLL排的 忽略大小写（都改成大写了）  规则的方法是根据列表里面的元素类型吧？
print(sorted(['hello','My','Dad','gril'],key=str.upper,reverse=True)) #反向排序

'''
python中的operator.itemgetter函数
operator.itemgetter函数
operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号。看下面的例子
a = [1,2,3]
b=operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值
b(a)
2
b=operator.itemgetter(1,0)  //定义函数b，获取对象的第1个域和第0个的值
b(a)
(2, 1)
要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。
sorted函数用来排序，sorted(iterable[, cmp[, key[, reverse]]])
其中key的参数为一个函数或者lambda函数。所以itemgetter可以用来当key的参数
a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
根据第二个域和第三个域进行排序
sorted(students, key=operator.itemgetter(1,2))
'''
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))

