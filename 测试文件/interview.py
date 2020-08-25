#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file: interview
#@function:-----------

from __future__ import division   #在python2.x中要使用精确算法需要导入这个函数（就导入就行不用操作它  python3是不需要这个东西的）
from copy import deepcopy
import copy
import sys

dic = {"a":"A","b":"B"}
new_dict = {y:x for x,y in dic.items()}
print(new_dict)


#拷贝
#赋值变量
list3 = [0,1,2,3,4,5,["a","b","c"]]  #外围的list 和内部的list是有不同的内存地址的
list4 = list3
list4.append(6)
list4[6].append("f")
print(
      list3,list4,list3[6],list4[6],id(list3),id(list4),id(list3[6]),id(list4[6])
      )  #list4去拷贝list3时只是拷贝的list3的指针(在栈区(存的变量)  就是在栈取开辟了一个list3相同的空间)并没有开辟新的内存(堆区(存的数据))
         #[0, 1, 2, 3, 4, 5, ['a', 'b', 'c', 'f'], 6] [0, 1, 2, 3, 4, 5, ['a', 'b', 'c', 'f'], 6]
         # ['a', 'b', 'c', 'f'] ['a', 'b', 'c', 'f']
         # 2171639552072 2171639552072 2171639473672 2171639473672
#浅拷贝
list_3 = [0,1,2,3,4,5,["a","b","c"]]
list5 = list_3.copy()   #浅拷贝 只为外围list开辟了新空间 内部的list还是拷贝的内存地址 这里说下内部的list是独立的内存 外围的list存的是地址
list5.append(7)
list_3[6].append("f")
print(
        list_3,list5,list_3[6],list5[6],id(list_3),id(list5),id(list_3[6]),id(list5[6])
     )#[0, 1, 2, 3, 4, 5, ['a', 'b', 'c', 'f']] [0, 1, 2, 3, 4, 5, ['a', 'b', 'c', 'f'], 7]
      # ['a', 'b', 'c', 'f'] ['a', 'b', 'c', 'f']  #内部的list是相同的 因为是浅拷贝 所以内部拷贝的仍是内存地址 所以两个list的内部list指向仍相同
      # 2841459641800 2841459641864 2841459610312 2841459610312

#深拷贝
list_3d = [0,1,2,3,4,5,["a","b","c"]]
list6 = copy.deepcopy(list_3d)   #内部的list也会开辟一个新的内存 外部 内部的list都拷贝了 都开辟了栈新空间
list6.append(8)
list6[6].append("f")
print(
        list_3d,list6,list_3d[6],list6[6],id(list_3d),id(list6),id(list_3d[6]),id(list6[6])
     )#[0, 1, 2, 3, 4, 5, ['a', 'b', 'c']] [0, 1, 2, 3, 4, 5, ['a', 'b', 'c', 'f'], 8]
      # ['a', 'b', 'c'] ['a', 'b', 'c', 'f']
      # 1779299666696 1779299666824 1779299666760 1779299666888  #id都是不同  开了新的栈空间


'''
内存管理：
    python中万物皆对象 所以python的存储问题就是对象的存储问题
    管理机制：引用计数 垃圾回收 内存池机制
'''
'''引用计数
                             引用      数据类型，ref count(计数)
1、变量通过引用指向对象  变量-------->(每个对象都会有一个头部信息)对象

'''

a=100
b=100
print(a is b)  #True      #is------------------>是用来判断两个值得引用对象是否相同
print(a == b)  #True


c='hello'
d='hello'
print(c is d)  #True
print(c == d)  #True

#以上结果证明：
    #Python缓存了整数和短字符串，因此每个对象在内存中只存有一份，引用所指对象就是相同的，即使使用赋值语句，也只是创造新的引用，而不是对象本身；

print("*************************  分割线____1  **************************")

g = 'hello my beauties word'
h = 'hello my beauties word'
print(g is h)  #False
print(g == h)  #True


e=["h"]
f=["h"]
print(e is f)  #False    每一个list对象会单独开辟空间 字典也是这样的
print(e == f)  #True

#以上的运行结果为IDE的运行结果 和pycharm的运行结果可能有出入 以IDE的为准  是不是pycharm在内存中缓存了一部分数据类型 就长字符串而言
#上面的 g is h 这个应该是 False的  下面这段话是没有问题的 ：
    #   Python没有缓存长字符串、列表及其他对象，可以由多个相同的对象，可以使用赋值语句创建出新的对象。
    #  对于字符串来说，如果不包含空格的字符串，则不会重新分配对象空间 对于包含空格的字符串则会重新分配
print("*************************  分割线____2  **************************")

m = 257
n = 257
print(m is n)  # False
print(m == n)  # True
# python中对大于256的整数，会重新分配对象空间地址保存对象；以上结果也是IDE的结果 情况可长字符串相同

print("*************************  分割线____3  **************************")

'''
在Python中，每个对象都有指向该对象的引用总数---引用计数

查看对象的引用计数：sys.getrefcount()
'''
import sys

print(sys.getrefcount(a))  # 20  这个命令查询的其实就是对象的引用数量 这个 20 指的就是内存中有几个引用指向对象100

o = "kjhgf"  #定义一个生僻的对象

print(sys.getrefcount(o))  # 2   注意：sys.getrefcount() 这个函数也会生成一个临时的引用 所以结果会比期望的多1


'''上面的计数结果和IDE不同 还是以IDE为准 应该是工具不同所牵扯的缓存不同 不过IDE应该是最为原生的结果所以它为准 (不过上面的意思明白就行了)'''

print("*************************  分割线____4  **************************")

'''垃圾回收
​ 当Python中的对象越来越多，占据越来越大的内存，启动垃圾回收(garbage collection)，将没用的对象清除。

1、原理
　　当Python的某个对象的引用计数降为0时，说明没有任何引用指向该对象，该对象就成为要被回收的垃圾。比如某个新建对象，被分配给某个引用，
    对象的引用计数变为1。如果引用被删除，对象的引用计数为0，那么该对象就可以被垃圾回收。
'''

# p = [123,321]  # 创建对象
# print(p.__del__())   #删除变量名 引用被销毁 refcount(计数变为0) 对象被收回 资源释放  （前提是没有其他引用指向它）

'''
3、注意
　　a、垃圾回收时，Python不能进行其它的任务，频繁的垃圾回收将大大降低Python的工作效率；
　　b、Python只会在特定条件下，自动启动垃圾回收（垃圾对象少就没必要回收）
　　c、当Python运行时，会记录其中分配对象(object allocation)和取消分配对象(object deallocation)的次数。当两者的差值高于某个阈值时，垃圾回收才会启动。
'''
import gc
print(gc.get_threshold())  #(700, 10, 10)  查看阀值
#700是垃圾回收的阀值 每10次0代垃圾回收，会配合1次1代垃圾回收；而10次1代垃圾回收，才会有1次二代垃圾回收
#新建对象为0代对象，当对象经历过垃圾回收 依然存后 就归入下一代

#我们也可以手动启动垃圾回收
print(gc.collect())  #手动启动垃圾回收


'''内存池机制
    python以 256k 为界限分为 大内存与小内存
        a、大内存由malloc进行分配
        b、小内存由内存池分配
        c、python的内存池(金字塔形)
            第三层：最上层，用户对python对象直接操作
            第一层和第二层：内存池，由python接口pyMem_malloc实现 若请求的对象大小为小内存即1k-256k之间，会使用内存管理系统进行分配，调用malloc
                           函数分配内存，但每次只会分配一块大小为256k的内存块，不会调用free函数释放内存，该内存块留在内存池中以便下次
                           调用(就是该对象被回收 内存块也依然留在内存池中 以便分配给其他对象 算是缓存或者说预加载)
            第0层：当请求的对象大小为大内存即大于256k 则malloc分配内存，同时free也会释放内存(以供malloc分配)
            第-1，-2 层：操作系统进行的操作层
'''

print("*************************  分割线____5  **************************")

'''
list去重
'''
ids = [1,4,3,3,4,2,3,4,5,6,1]
print(list(set(ids)))

import itertools
ids.sort()
for x,y in itertools.groupby(ids):
    print(x)

print("*************************  分割线____6  **************************")
'''类中的__init__(self)和类中的其他方法self说明：

    其实这俩可以放一起说的  __init__一个初始化的构造器 负责对新实例或对象分配内存 定义类实例对象的属性(因为在 __init__ 方法的内部，
    就可以把各种属性绑定到 self，因为 self 就指向创建的实例本身) __init__中的self是引用新创建的对象(这个指的是这个类的实例对象吧)
    而类中的其他方法的self 是指向外部调用的引用(当外部调用类内部的方法时 外部对象会将一个引用传入这个类的实例 而self就是为了接收这个
    引用的 以确保每一个引用的隔离性(毕竟一个类里可能有多个方法)，那如何确保隔离性呢？因为self还会声明区分局部变量的类的方法和属性)
'''

'''
xrange和range区别(xrange 在python3中已经被弃用)：
    在大多数情况下，xrange和range在功能方面完全相同。它们都提供了一种生成整数列表的方法，唯一的区别是range返回一个Python列表对象，
    x range返回一个xrange对象。这就表示xrange实际上在运行时并不是生成静态列表。它使用称为yielding的特殊技术根据需要创建值。
    该技术与为生成器的对象一起使用。因此如果你有一个非常巨大的列表，那么就要考虑xrange。
'''

print("*************************  分割线____7  **************************")
'''
NumPy中有哪些操作Python列表的函数？(numPy 这个回来有时间要研究下)

NumPy是Python中科学计算的基础包。它是一个Python库，提供多维数组对象，各种派生对象（如掩码数组和矩阵），以及用于数组快速操作的
各种API，有包括数学、逻辑、形状操作、排序、选择、输入输出、离散傅立叶变换、基本线性代数，基本统计运算和随机模拟等等。

Python的列表是高效的通用容器。它们支持（相当）有效的插入，删除，追加和连接，Python的列表推导使它们易于构造和操作。

它们有一定的局限性：它们不支持像素化加法和乘法等“向量化”操作，并且它们可以包含不同类型的对象这一事实意味着Python必须存储每个元素的类型信息，并且必须执行类型调度代码在对每个元素进行操作时。

NumPy不仅效率更高; 它也更方便。你可以免费获得大量的向量和矩阵运算，这有时可以避免不必要的工作。它们也得到有效实施。

NumPy数组更快，你可以使用NumPy，FFT，卷积，快速搜索，基本统计，线性代数，直方图等内置。
'''

'''
python 有Oops概念吗:
    Oops 内核执行出错时也会抱歉的对我们说：“哎呦（Oops），对不起，我把事情搞砸了”。Linux内核在发生kernel panic时会打印出Oops信息，
    把目前的寄存器状态、堆栈内容、以及完整的Call trace都show给我们看，这样就可以帮助我们定位错误。

    python是面向对象的编程语言，这意味着可以创建对象模型在python中解决任何程序（这意味着没有Oops喽 我们通过定义对象捕捉python错误）
    同时python可以被视为程序语言和结构语言
'''

'''
用python删除文件和用linux命令删除文件方法:
    python：os.remove(文件名)
    linux:       rm  文件名
'''

'''
正则表达式匹配中，（.*）和（.*?）匹配区别？
    （.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
    （.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
'''

print("*************************  分割线____8  **************************")

'''1--100的和'''
from functools import reduce
print(reduce(lambda x,y:x+y,range(101)))

print(sum(range(101)))

'''列表[1,2,3,4,5]，请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]？'''


listpow = [1,2,3,4,5]
res = [y for y in list(map(lambda x:x ** 2,listpow)) if y>10]  #这个列表里的过滤叫列表推导式
print(res)  #[16, 25]

import random
print({k:random.randint(4,9) for k in ['a','b','c','d']})  #字典推导式  结果大概这个样子 没次运行值都会变毕竟随机的{'a': 6, 'b': 7, 'c': 5, 'd': 5}

'''根据键的大小进行排序'''
dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
listm = sorted(dic.items(),key=lambda x:x[0],reverse=False)
print(dict(listm))

#其实我们还有另一种方法
import operator
# listm = sorted(dic.items(),key=operator.itemgetter(0),reverse=False)
# print(dict(listm))

'''利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"'''
from collections import Counter
c = Counter()
for i in "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h":
    c[i] += 1
print(c)

'''字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"'''
import re
a = "not 404 found 张三 99 深圳"
strsp = a.split(" ")
# res = re.findall(r"\d+|[a-zA-Z]+",a)
res = re.findall(r"[0-9a-zA-Z]+",a)
for r in res:
    if r in strsp:
        strsp.remove(r)
print(" ".join(strsp))

'''filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，
# 序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表。
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x:x % 2 !=0,a)))

'''列表推导式求列表所有奇数并构造新列表，b =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
b =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x for x in b if x % 2 != 0])

'''正则re.complie作用'''
    #其实就是预编译 把某种常用的正则表达式编译为对象 方便调用而且速度更快

'''a=（1，）b=(1)，c=("1") 分别是什么类型的数据？  挺有意思'''

a,b,c = (1,),(1),("1")
print("a(1,): %s,b(1): %s,c('1'): %s" % (type(a),type(b),type(c)))  #a(1,): <class 'tuple'>,b(1): <class 'int'>,c('1'): <class 'str'>

'''两个列表[1,5,7,9]和[2,2,6,8]合并为[9, 8, 7, 6, 5, 3, 2, 2, 1]'''
a = [1,5,7,9]
a.extend([2,2,6,8])
a.insert(a.index(5),3)
a.sort(reverse=True)
print(a)

'''[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]'''
a = [[1,2],[3,4],[5,6]]
fh = list()
print([j for i in a for j in i])

'''[1, 2, 3, 4, 5, 6, 7, 8, 9,10]变为 [[1, 2, 3], [4, 5, 6], [7, 8, 9],[10]'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print([a[x:x+3] for x in range(0,10,3)])

'''请将[i for i in range(3)]改成生成器'''
    # 生成器是特殊的迭代器：
    # 1、列表表达式的[]改为()即可变成生成器。
    # 2、函数在返回值得时候出现yield就变成生成器，而不是函数了，

print("*************************  分割线____9  **************************")
'''首字母大写'''
print('hello world'.title())  #标题化嘛 每个单词首字母都会大写   Hello World
print('hello world'.capitalize())#只有首字母才会大写  Hello world

'''
Python中help()和dir()函数的用法
    Help()和dir()这两个函数都可以从Python解释器直接访问，并用于查看内置函数的合并转储。
'''
print(help(sum((1,2,3,4)))) #help()函数用于显示文档字符串，还可以查看与模块，关键字，属性等相关的使用信息。
print(dir((1,2,3,4))) #dir()函数用于显示定义的符号。 比如这里面是一个元祖 他就会显示可操作元祖的所有函数

'''
在Python中split()，sub()，subn()功能 这个指的是正则里面的
'''
import re


print(re.split(r'[a-zA-Z]{2}','11qq22ww33ee44rr')) #使用正则表达式模式将给定字符串“拆分”到列表中。['11', '22', '33', '44', '']
print(re.sub(r'[a-zA-Z]{2}','a','11qq22ww33ee44rr'))#查找正则表达式模式匹配的所有子字符串，然后用不同的字符串替换它们 11a22a33a44a
print(re.subn(r'[a-zA-Z]{2}','a','11qq22ww33ee44rr'))#它类似于sub()，返回一个元祖 新值和个数 ('11a22a33a44a', 4)


'''a="张明 98分"，用re.sub，将98替换为100'''
a="张明 98分"
print(re.sub("\d+","100",a)) #张明 100分

'''正则匹配，匹配日期2018-03-20'''
'''# findall结果无需加group(),search需要加group()提取'''

url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
print(re.findall(r'dateRange=(.*?)%7C(.*?)&',url))  #[('2018-03-20', '2018-03-20')]
# gr = re.search(r'dateRange=(.*?)%7 C(.*?)&',url)
# print(gr.group(0)) #dateRange=2018-03-20%7C2018-03-20&
#   其实匹配并不难，提取一段特征语句，用（.*?）匹配即可。

'''正则匹配中文'''
til = "你好，hello，世界"
pattern = re.compile(r'[\u4e00-\u9fa5]+')
print(pattern.findall(til))


'''list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]'''
l = [2,3,5,4,9,6]
print(sorted(l,key=lambda x : x,reverse=False))
# [2, 3, 4, 5, 6, 9]  这也可以 不然的话  对一维的数据的话 key=lambda x : x 可以不要的 是代表的本身嘛（不加的话默认也是）

'''使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，
输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小】（传两个条件，x<0和abs(x)）'''
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
print(sorted(foo,key=lambda x:(x<0,abs(x))))

'''再来个例子：doo = [{'e':2},{'a':1},{'c':2},{'d':3},{'f':3},{'b':2}] 根据值数字排序 数字相同根据键排序'''
doo = [{'e':2},{'a':1},{'c':2},{'d':3},{'f':3},{'b':2}]
print(sorted(doo,key=lambda x:(list(x.values())[0],list(x.keys())[0]))) #[{'a': 1}, {'b': 2}, {'c': 2}, {'e': 2}, {'d': 3}, {'f': 3}]


# print(list({'qw':'qqqq'}.values()))

# lsort = list()
# while len(l) > 0:
#     lmin = min(l)
#     lsort.append(lmin)
#     l.remove(lmin)
#
# print(lsort)

'''x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果'''
x="abc"
y="def"
z=["d","e","f"]
print(x.join(y))  #dabceabcf
print(x.join(z))  #dabceabcf
import os
print(os.path.join(x,y)) # abc\def  这个时路径的拼接呀

'''zip 参数是可迭代对象 如列表 元组 以短的为主（最好保持长度一致 不然数据会丢失）  zip(x,y)成为一个zip类型的迭代对象 之前我理解错了'''
print([i for i in zip(x,y)])  #[('a', 'd'), ('b', 'e'), ('c', 'f')]


'''递归求和 1加到10'''
# print(sum(range(11)))

def sumf(num):
    if num >= 1:
        res = num + sumf(num - 1)
    else:
        res = 0
    return res

res = sumf(10)
print(res)

'''两个列表的差集 并集 交集'''
lk = [1,2,3,4]
lj = [3,4,5,6]
print(list(set(lk)|set(lj)))  #并集[1, 2, 3, 4, 5, 6]
print(list(set(lk).union(set(lj))))#并集[1, 2, 3, 4, 5, 6]
print(list(set(lk)&set(lj)))  #交集 [3, 4]
print(list(set(lk).intersection(set(lj))))#交集 [3, 4]
print(list(set(lk).difference(set(lj)))) #差集  以前面的set集合为准  [1, 2]


'''
all()和any()：
all:迭代器中所有的判断项返回都是真，结果才为真
any:只要迭代器中有一个元素为真就为真
python中什么元素为假:（0，空字符串，空列表、空字典、空元组、None, False）
'''
print(all(['a','b',None]))  #False
print(any(['a','b',None]))  #True

print(all(['a','b',[]]))  #False
print(any(['a','b',[]]))  #True

'''
__init__和__new__的区别：
'''
class Copm(object):

    def __init__(self): #init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数
        print("这是init方法：",self) #<__main__.Copm object at 0x02CB84F0>  执行顺序：3
        #__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值。
    def __new__(cls, *args, **kwargs): #__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
        print("这是cls的ID：",id(cls)) #47915992    执行顺序：1
        print("这是new方法：",object.__new__(cls))  #<__main__.Copm object at 0x02CB84F0> #两者地址相同  执行顺序：2
        return object.__new__(cls) #__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，
        # 可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例。


# 如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，
# 如果是其他类的类名，；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数
Copm()
print("这是类Comp的ID：",id(Copm)) #47915992  id相同证明指向的是同一个类，也就是cls就是创建的实例类  执行顺序：4

'''
单例模式:
因为创建对象时__new__方法执行，并且必须return 返回实例化出来的对象所cls.__instance是否存在，不存在的话就创建对象，
存在的话就返回该对象，来保证只有一个实例对象存在（单列）
'''
#实例化一个单例
class Singleton(object):
    __instance = None

    def __new__(cls, age ,name):
        #如果类属性__instance为空
        #那么久创建一个对象，并赋值为这个对象的引用，保证下次调用这个方法时
        #能够知道之间已经创建出对象了，这样就保证了只有一个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(18,"Singlet")
b = Singleton(28,"Sing")

print(id(a)) #2019990760
print(id(b)) #2019990760   打印ID，值一样，说明对象同一个。

a.age = 19
print(b.age) #19    两者为同一个实例 a改变 b也改变吗

#单例嘛 顾名思义 不管外界创建多少引用 去实例化对象  ，单例类只提供一个实例 比如上面的那个 返回的cls.__instance(我只提供这个)


print("*************************  分割线____10  **************************")

'''数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句'''
    #select distinct name from student

'''数据库优化查询方法'''
    # 外键、索引、联合查询、选择特定字段等等
'''
列出常见MYSQL数据存储引擎 (就看这一种就行了)
    InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），
    要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，
    因为支持事务的提交（commit）和回滚（rollback）。
'''
print("*************************  分割线____11  **************************")

'''
1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')

Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'

2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存

3、python2中使用ascii编码，python中使用utf-8编码

4、python2中unicode表示字符串序列，str表示字节序列

      python3中str表示字符串序列，byte表示字节序列

5、python2中为正常显示中文，引入coding声明，python3中不需要

6、python2中是raw_input()函数，python3中是input()函数

'''

'''
提高python运行效率的方法

    1、使用生成器，因为可以节约大量内存

    2、循环代码优化，避免过多重复代码的执行

    3、核心模块用Cython  PyPy等，提高效率

    4、多进程、多线程、协程

    5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率
'''


'''
写几个web返回的状态码吧：
    200 ok 处理完成
    204 No  Content 请求成功处理 但没有实体的主体返回
    206 Partial Content GET范围请求已经处理成功
    301 Moved Permanently 永久重定向，资源已永久分配新url
    302 Found 永久重定向 资源已临时分配新的url
    303 See Other 临时重定向 期望使用GET定向获取
    304 Not Modified 发送的附带条件请求未满足
    400 Bad Request  请求报文语法错误
    401 Unauthorized 需要通过HTTP认证，或认证失败
    403 Forbidden 请求资源被拒绝
    404 Not Found 没找到请求资源（服务器无理由拒绝）
    500 Internal Server Error 服务故障或web应用故障
    503 Service Unavailable 超负载或停机维护
'''

'''
python 常见错误：

    IOError：输入输出异常

    AttributeError：试图访问一个对象没有的属性

    ImportError：无法引入模块或包，基本是路径问题

    IndentationError：语法错误，代码没有正确的对齐

    IndexError：下标索引超出序列边界

    KeyError：试图访问你字典里不存在的键

    SyntaxError：Python代码逻辑语法出错，不能执行

    NameError：使用一个还未赋予对象的变量
'''

'''
简述cookie和session的区别

    1、session 在服务器端，cookie 在客户端（浏览器）。

    2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，
    同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，
    过期时间由开发人员设置。

    3、cookie安全性比session差。
'''

'''
如何在函数内修改全局变量：
    在函数内部的属性前面加一个global声明就行了呀
'''

'''
python2和python3的range(100)的区别:
    python2返回列表，python3返回range类型的迭代器，节约内存.
'''

'''
一句话解释什么样的语言能够用装饰器:
    函数可以作为参数传递的语言，可以使用装饰器。
'''

'''
lambda匿名函数好处
    精简代码，lambda省去了定义函数，map省去了写for循环过程
'''

'''
HTTP请求中get和post区别

    1、GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在请求头中的，
    我们是无法直接看到的。

    2、GET提交有数据大小的限制，一般是不超过1024个字节，而这种说法也不完全准确，HTTP协议并没有设定URL字节长度的上限，
    而是浏览器做了些处理，所以长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，一般来说是没有设置限制的，
    但是实际上浏览器也有默认值。总体来说，少量的数据使用GET，大量的数据使用POST。

    3、GET请求因为数据参数是暴露在URL中的，所以安全性比较低，比如密码是不能暴露的，就不能使用GET请求；POST请求中，
    请求参数信息是放在请求头的，所以安全性较高，可以使用。在实际中，涉及到登录操作的时候，尽量使用HTTPS请求，安全性更好。

'''

