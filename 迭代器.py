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

'''yield: '''
'''
首先，如果你还没有对yield有个初步分认识，那么你先把yield看做“return”，这个是直观的，它首先是个return，普通的return是什么意思，
就是在程序中返回某个值，返回之后程序就不再往下运行了。看做return之后再把它看做一个是生成器（generator）的一部分
（带yield的函数才是真正的迭代器），好了，如果你对这些不明白的话，那先把yield看做return,然后直接看下面的程序，
你就会明白yield的全部意思了：

'''

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))

'''
starting...
4
********************
res: None
4
'''

'''
我直接解释代码运行顺序，相当于代码单步调试：

1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象)

2.直到调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环

3.程序遇到yield关键字，然后把yield想想成return,return了一个4之后，程序停止，并没有执行赋值给res操作，此时next(g)语句执行完成，
所以输出的前两行（第一个是while上面的print的结果,第二个是return出的结果）是执行print(next(g))的结果，

4.程序执行print("*"*20)，输出20个*

5.又开始执行下面的print(next(g)),这个时候和上面那个差不多，不过不同的是，这个时候是从刚才那个next程序停止的地方开始执行的，
也就是要执行res的赋值操作，这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，
并没有给赋值操作的左边传参数），所以这个时候res赋值是None,所以接着下面的输出就是res:None,

6.程序会继续在while里执行，又一次碰到yield,这个时候同样return 出4，然后程序停止，print函数输出的4就是这次return出的4.


到这里你可能就明白yield和return的关系和区别了，带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，
next就相当于“下一步”生成哪个数，这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，
生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，然后遇到yield后，return出要生成的数，此步就结束。

'''
#                换为
#print(next(g)) -------> print(g.send(7))

'''
starting...
4
********************
res: 7
4
'''
'''
先大致说一下send函数的概念：此时你应该注意到上面那个的紫色的字，还有上面那个res的值为什么是None，这个变成了7，到底为什么，
这是因为，send是发送一个参数给res的，因为上面讲到，return的时候，并没有把4赋值给res，下次执行的时候只好继续执行赋值操作，
只好赋值为None了，而如果用send的话，开始执行的时候，先接着上一次（return 4之后）执行，先把7赋值给了res,然后执行next的作用，
遇见下一回的yield，return出结果后结束。

 

5.程序执行g.send(7)，程序会从yield关键字那一行继续向下运行，send会把7这个值赋值给res变量

6.由于send方法中包含next()方法，所以程序会继续向下运行执行print方法，然后再次进入while循环

7.程序执行再次遇到yield关键字，yield会返回后面的值后，程序再次暂停，直到再次调用next方法或send方法。
'''

# 这就结束了，说一下，为什么用这个生成器，是因为如果用List的话，会占用更大的空间，比如说取0,1,2,3,4,5,6............1000