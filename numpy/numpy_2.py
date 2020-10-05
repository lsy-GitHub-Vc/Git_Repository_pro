#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:
#@function:-----------


import numpy as np

#数组的创建
'''
shape	数组形状
dtype	数据类型，可选
order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
'''
hf = np.empty([2,2],dtype=int,order='C')#这个可以创建一个空的数组  这种创建只提供了结构 数组的数值都是随机的 因为没有进行初始化
print(hf)
'''
[[ 1901493322 -1669367854]
 [ -343112973   356937655]]
'''

z = np.zeros(5,dtype=float,order='C') #创建指定大小的数组，数值用0来填充
print(z)

#自定以一个类型
k = np.zeros([2,2],dtype=[('x',np.int32),('y','i4')])
print(k)


o = np.ones(5,dtype=np.int,order='C') #创建指定大小的数组，数值用1来填充
print(o)

#正态分布数组
print(np.random.randn(3,2))

#创建随机分布整数型数组。100上200下 的二维数组
print(np.random.randint(100,200,(3,3)))