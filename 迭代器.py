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
y = (x for x in range(3))  #生成器
print(next(y))
print(next(y))
print(next(y))

#转成Iterator对象  其他类型也可以
itr = iter([1,2,3,4,5])  #转化为一个可迭代对象 生成器
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


def yield_1():
    for i in [1,2,3,4]:
        yield i
    print("----------------")
    for j in [5,6,7]:
        yield j
    return "**********"

y=yield_1()
while True:
    try:
        print(y.send(None))  #以后send将取代next
    except StopIteration as e:
        print(e.value)   #return的值包含在异常StopIteration的value中
        break


def a():
    print('aaa')
    p1 = yield '123'
    print('bbb')
    if (p1 == 'hello'):
        print('p1是send传过来的')
    p2= yield '234'
    print(p2)

r = a()
print(next(r))
'''
说一下执行的顺序，首先a()是个生成器；第一次执行要么next(r)要么r.send(None)，不能使用r.send('xxxxx')；这会报错的。
第一次执行时next(r)时，首先打印出aaa,
'''
r.send('hello')
'''
然后遇到yield即跳出，然后执行r.send('hello')时，p1则被赋值为hello了，然后继续接着上次运行，下一步打印出bbb，
然后打印出'p1是send传过来的',当再次遇到第二个yield时跳出，所以结果只打印了三行，后面的p2没有执行。
'''
