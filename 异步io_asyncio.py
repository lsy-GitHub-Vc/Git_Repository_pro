#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 #@time:
#@Author:lsy
#@file:asyncio
#@function:-----------

'''asyncio'''

'''
asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。


1、event_loop 事件循环：程序开启一个无限循环，把一些函数注册到事件循环上，当满足事件发生的时候，调用相应的协程函数

2、coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。

3、task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含了任务的各种状态

4、future: 代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别

5、async/await 关键字：python3.5用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。


'''
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    #刷新底层传输的写缓冲区。也就是把需要发送出去的数据，从缓冲区发送出去。没有手工刷新，asyncio为你自动刷新了。
    # 当执行到reader.readline()时，asyncio知道应该把发送缓冲区的数据发送出去了。
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop() #获取循环事件
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))  ## 执行coroutine
loop.close()

# 可见3个连接由一个线程通过coroutine并发完成。

'''async/await'''

'''

用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。

# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：

    1、把@asyncio.coroutine替换为async；
    2、把yield from替换为await。
    这俩关键字能用 不过下面有红色波浪线 但不影响使用

'''


# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#

# async def do_some_work(x):
#     print("waiting:", x)
#     r = await asyncio.sleep(1)
#     print("Hello again!")




'''aiohttp:

asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，
因此可以用单线程+coroutine实现多用户的高并发支持。

asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
'''

from aiohttp import web

'''
然后编写一个HTTP服务器，分别处理以下URL：

    1、/ - 首页返回b'<h1>Index</h1>'；

    2、/hello/{name} - 根据URL参数返回文本hello, %s!。

代码如下：
'''
'''
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index<h1>', content_type='text/html')

async def hello(request):
    await  asyncio.sleep(0.5)
    text = '<h1>hello,%s!<h1>' % request.match_info['name']
    return web.Response(text=text.encode(encoding='utf-8'),content_type='text1/html')


async def init(loop):
    app = web.Application()  #创建一个事件的申请对象
    app.router.add_route('GET','/',index)    #add_route 给事件对象添加一个渠道      router(路由) 说白了他就是一个分配任务的函数吧 增加 删除等等
    # app.router.add_route('GET','/hello/{name}',hello)
    srv =  await loop.create_server(app._make_handler(),'127.0.0,1', 9000)
    print('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()   #创建一个事件的循环对象
loop.run_until_complete(init(loop))       #执行coroutine(写成)
loop.run_forever()             #这个确保事件循环的持久性吧  可能
'''


import asyncio,aiohttp

#aiohttp的简单实使用  读取网页
# async def fetch_async(url):
#  print(url)
#  async with aiohttp.request("GET",url) as r:
#   reponse = await r.text(encoding="utf-8") #或者直接await r.read()不编码，直接读取，适合于图像等无法编码文件
#   print(reponse)
#
# tasks = [fetch_async('http://www.baidu.com/'), fetch_async('http://www.chouti.com/')]
#
# event_loop = asyncio.get_event_loop()
# results = event_loop.run_until_complete(asyncio.gather(*tasks))
# event_loop.close()


#发起一个session请求 度网页
# async def fetch_async(url):
#     print(url)
#     async with aiohttp.ClientSession() as session:  #协程嵌套，只需要处理最外层协程即可fetch_async
#         async with session.get(url) as resp:
#             print(resp.status)
#             print(await resp.text()) #因为这里使用到了await关键字，实现异步，所有他上面的函数体需要声明为异步async
#
# tasks = [fetch_async('http://www.baidu.com/'), fetch_async('http://www.cnblogs.com/ssyfj/')]
#
# event_loop = asyncio.get_event_loop()
# results = event_loop.run_until_complete(asyncio.gather(*tasks))
# event_loop.close()

#除了上面的get方法  会话还支持 post put  delete
# session.put('http://httpbin.org/put', data=b'data')
# session.delete('http://httpbin.org/delete')
# session.head('http://httpbin.org/get')
# session.options('http://httpbin.org/get')
# session.patch('http://httpbin.org/patch', data=b'data')


#https://www.jb51.net/article/163537.htm   这个讲的挺详细的  用法多着呢


