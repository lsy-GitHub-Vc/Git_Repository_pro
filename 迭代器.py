from collections.abc import Iterable,Iterator
#3.8版本前不加abc

'''
可迭代对象：可以直接用于for循环的对象统称为可迭代对象(Iterable),
可以用isinstance() 去判断一个对象是否是Iterable对象

可以直接作用于for循环的数据类型一般分为两种
1、集合类的数据类型 list tuple dict set string
2、是genertor,包括生成器和带yield 的genertor function
'''

print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance("",Iterable))
#以上都是可迭代对象
print(isinstance((x for x in range(2)),Iterable)) #(x for x in range(2)) 这个应该是一个迭代器 为啥在判断是否为可迭代对象时返回True呢？奇怪 应该是版本的问题



'''
迭代器：迭代器不止只能作用于for循环，它还可以被next()函数持续调用并返回下一个值，直到返回一个StopIntration的异常
说明无法继续返回下一个值

可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator对象)
'''

print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance((),Iterator))
print(isinstance("",Iterator))
print(isinstance((x for x in range(2)),Iterator)) #判断是否为迭代器


#迭代器
y = (x for x in range(3))
print(next(y))
print(next(y))
print(next(y))

#转成Iterator对象  其他类型也可以
itr = iter([1,2,3,4,5])
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))