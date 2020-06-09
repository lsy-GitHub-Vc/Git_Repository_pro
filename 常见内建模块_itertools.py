#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy

import itertools

'''Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

首先，我们看看itertools提供的几个“无限”迭代器：'''

# nat = itertools.count(1,5)  #count(1) 会创建一个无限的迭代器  打印出自然数的序列 参数是开始位置和间隔  根本停不下来 结果：1,2,3,4,5,6......
#nat = itertools.cycle('ABC') #任意字符串也是序列的一种  结果：A,B,C,A,B,C,A,B,C,A......
nat = itertools.repeat('A',3) #重复一个元素 可以加次数限制 结果：A A A
for i in nat:
    print(i)

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
sat = itertools.count(0)
xzf = itertools.takewhile(lambda x:x<10,sat)
print(list(xzf))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



#itertools提供的几个迭代器操作函数更加有用：

'''chain:  chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：'''

for c in itertools.chain('aqsd','qwe'):
    print(c)   #a q s d q w e


'''groupby: groupby()把迭代器中相邻的重复元素挑出来放在一起：'''

for key,group in itertools.groupby('AAABBCCCDD'):
    print(key,list(group))

'''
A ['A', 'A', 'A']
B ['B', 'B']
C ['C', 'C', 'C']
D ['D', 'D']
'''

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，
# 就可以让元素'A'和'a'都返回相同的key：

for key,group in itertools.groupby('AaaBbccC,,ddD',lambda n:n.lower()):
    print(key,list(group))

'''
a ['A', 'a', 'a']
b ['B', 'b']
c ['c', 'c', 'C']
, [',', ',']
d ['d', 'd', 'D']
'''

def ite(x):

    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:

    iter = itertools.takewhile(lambda a:a<2*x,itertools.count(1,2))
    n = 1
    m = 0
    for i in iter:
        m += 1/i * n
        n *= -1
    return round(4*m,4)

print(ite(10000))