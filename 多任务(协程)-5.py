#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:协程
#@function:-----------
'''
协程
'''
'''
Python通过yield提供了对协程的基本支持，但是不完全。而第三方的gevent为Python提供了比较完善的协程支持。

gevent是第三方库，通过greenlet实现协程，其基本思想是：

当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成：
'''
from gevent import monkey
import gevent,time
from urllib import request,response

def f0(n):
    for i in range(n):
        print (gevent.getcurrent(), i)

g1 = gevent.spawn(f0, 5)
g2 = gevent.spawn(f0, 5)
g3 = gevent.spawn(f0, 5)
g1.join()
g2.join()
g3.join()

print("分割线1----------------------------------------------")
'''
可以看到，3个greenlet是依次运行而不是交替运行。

要让greenlet交替运行，可以通过gevent.sleep()交出控制权：
'''
def f1(n):
    for i in range(n):
        print (gevent.getcurrent(), i)
        gevent.sleep(0)


g1 = gevent.spawn(f1, 5)
g2 = gevent.spawn(f1, 5)
g3 = gevent.spawn(f1, 5)
g1.join()
g2.join()
g3.join()


print("分割线2---------------------------------------------")
'''
3个greenlet交替运行，

把循环次数改为500000，让它们的运行时间长一点，然后在操作系统的进程管理器中看，线程数只有1个。

当然，实际代码里，我们不会用gevent.sleep()去切换协程，而是在执行到IO操作时，gevent自动切换，代码如下：
'''

monkey.patch_all() #将程序中的所有io操作做上标记 使程序为非阻塞状态
def f2(url):
    print('GET: %s' % url)
    reps = request.urlopen(url)
    redata = reps.read(1000)
    print('%d bytes received from %s.' % (len(redata), url))

timestat = time.time()

gevent.joinall([      #创建线程并行执行程序，碰到IO就切换
        gevent.spawn(f2, "https://www.python.org/"),
        gevent.spawn(f2, "https://www.yahoo.com/"),
        gevent.spawn(f2, "https://hao.360.com/"),
])
print("耗时",time.time()-timestat)
'''
从结果看，3个网络操作是并发执行的，而且结束顺序不同，但只有一个线程。
'''


'''
使用gevent，可以获得极高的并发性能，但gevent只能在Unix/Linux下运行，在Windows下不保证正常安装和运行。

由于gevent是基于IO切换的协程，所以最神奇的是，我们编写的Web App代码，不需要引入gevent的包，也不需要改任何代码，
仅仅在部署的时候，用一个支持gevent的WSGI服务器，立刻就获得了数倍的性能提升
'''

'''
最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，
协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，
所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

Python对协程的支持是通过generator实现的。

在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。

但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。

来看例子：

传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。

如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：
'''

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)


'''
注意到consumer函数是一个generator，把一个consumer传入produce后：

    1、首先调用c.send(None)启动生成器；

    2、然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

    3、consumer通过yield拿到消息，处理，又通过yield把结果传回；

    4、produce拿到consumer处理的结果，继续生产下一条消息；

    5、produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

最后套用Donald Knuth的一句话总结协程的特点：

“子程序就是协程的一种特例。”
'''