#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:
#@function:-----------


import numpy as np

'''
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制， 复制 dtype 对象, 如果为 false，则是对内置数据类型对象的引用 不是返回原数据
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度


#就dtype而言内置类型较多 但基本上和C语言类型对应

bool_	布尔型数据类型（True 或者 False）
bool_	布尔型数据类型（True 或者 False）
int_	默认的整数类型（类似于 C 语言中的 long，int32 或 int64）
intc	与 C 的 int 类型一样，一般是 int32 或 int 64
intp	用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）
int8	字节（-128 to 127）
int16	整数（-32768 to 32767）
int32	整数（-2147483648 to 2147483647）
int64	整数（-9223372036854775808 to 9223372036854775807）
uint8	无符号整数（0 to 255）
uint16	无符号整数（0 to 65535）
uint32	无符号整数（0 to 4294967295）
uint64	无符号整数（0 to 18446744073709551615）
float_	float64 类型的简写
float16	半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
float32	单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
float64	双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
complex_	complex128 类型的简写，即 128 位复数
complex64	复数，表示双 32 位浮点数（实数部分和虚数部分）
complex128	复数，表示双 64 位浮点数（实数部分和虚数部分）
'''


print(np.array([1,2,3]))  #[1,2,3]
print(np.array([[1,2],[3,4]]))  #[[1 2]
#                                 [3 4]]
print(np.array([1,2,  3,  4,5],ndmin=2)) #[[1 2 3 4 5]]  二维数组
print(np.array([1, 2, 3],dtype=complex)) #[1.+0.j 2.+0.j 3.+0.j]  复数

'''
b	布尔型
i	(有符号) 整型
u	无符号整型 integer
f	浮点型
c	复数浮点型
m	timedelta（时间间隔）
M	datetime（日期时间）
O	(Python) 对象
S, a	(byte-)字符串
U	Unicode
V	原始数据 (void)
'''
# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
#实例1   类型字段名可以用于存取实际的 age 列
dt = np.dtype([('age',np.int8)])#或者i1吧
n = np.array([(10,),(20,),(30,)],dtype=dt)
print(n['age'])  #[10 20 30]

#实例2  类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。

student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student) #[('name', 'S20'), ('age', 'i1'), ('marks', '<f4')]

a = np.array([('lsy',27,60),('lst',12,80)],dtype=student)
print(a) #[(b'lsy', 27, 60.) (b'lst', 12, 80.)]


l = np.arange(24)
print(l)
# s = l.reshape(3,2,4)  #3维
s = l.reshape(3,2,2,2)  #4维  看方法里面的数字个数吧  拼接起来是24就行  这些数值应该分别代表每一个线性轴的数组个数 就是每一层的秩数
# print(s.ndim)  #维数
print(s)

print(s.shape)  #(3, 2, 2, 2)  其维度表示"行数"和"列数"。  就是array结构

#也可以改变其结构
nl = np.array([[1,2,3],[4,5,6]])
nl.shape = (3,2)
# sl = nl.reshape(3.2)  #这个也可以
# print(sl)
print(nl)

#ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。

ys = np.array([1,2,3,4],dtype=np.float64)
print(ys.itemsize) #8  64个bits 8个bits一个字节

print(nl.itemsize)   #4
print(s.itemsize)    #4  默认的类型是int32吗？


#返回内存信息
print(ys.flags)

'''
C_CONTIGUOUS (C)	数据是在一个单一的C风格的连续段中
F_CONTIGUOUS (F)	数据是在一个单一的Fortran风格的连续段中
OWNDATA (O)	数组拥有它所使用的内存或从另一个对象中借用它
WRITEABLE (W)	数据区域可以被写入，将该值设置为 False，则数据为只读
ALIGNED (A)	数据和所有元素都适当地对齐到硬件上
UPDATEIFCOPY (U)	这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新
'''