from urllib import request
import gevent,time
from gevent import monkey

# monkey.patch_all()
# def urllib2(url):
#     pshate = request.urlopen(url)
#     psbody = pshate.readline()
#     print(psbody)
#
#
# gevent.joinall([
#     gevent.spawn(urllib2,"https://hao.360.com/"),
#     gevent.spawn(urllib2,"https://www.baidu.com/"),
# ])



# monkey.patch_all()   #将程序中所有IO操作做上标记使程序非阻塞状态
# def url_request(url):
#     print('get:%s'%url)
#     resp = request.urlopen(url)
#     data = resp.read()
#     print('%s bytes received from %s'%(len(data),url))
#
# async_time_start = time.time() #开始时间
# gevent.joinall([
#     gevent.spawn(url_request,'https://www.python.org/'),
#     gevent.spawn(url_request,'https://www.nginx.org/'),
#     gevent.spawn(url_request,'https://www.ibm.com'),
# ])
# print('haoshi:',time.time()-async_time_start) #总用时
# def foo():
#     print('running in foo')
#     gevent.sleep(2)
#     print('com back from bar in to foo')
# def bar():
#     print('running in bar')
#     gevent.sleep(2)
#     print('com back from foo in to bar')
#
# gevent.joinall([      #创建线程并行执行程序，碰到IO就切换
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ]

