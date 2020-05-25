'''
线程 在一个进程内部 同时要执行多个事件 就需要同时运行多个“子任务”，我们把这个“子任务”就称为线程

线程是共享内存空间的并发执行的多任务 每一个线程都共享一个进程的资源 也就表示线程间是共享数据的

线程是最小的执行单元

线程锁解决数据混乱
模块
1、_thread模块  低级模块(接近于底层模块)
2、threading模块 高级模块 (对_thread进行了封装)
'''

import threading

#锁对象
lock = threading.Lock()

num = 0
def run(nu):
    print("子线程(%s)启动"%(threading.current_thread().name))
    #功能体
    global num
    for i in range(1000000):
        '''
        #加锁
        lock.acquire()
        try:
            num +=nu
            num -=nu
        finally:
            #释放锁
            lock.release()
        '''
        #和上面相同 不过死锁的几率应该会低点
        with lock:
            num +=nu
            num -=nu
    print("子线程(%s)结束"%(threading.current_thread().name))


if __name__ == "__main__":
    #任何进程都会启动一个线程，我们称之为主线程，主线程可以启动新的子线程
    #threading.current_thread().name 返回当前线程的实例
    print("主线程(%s)启动"%(threading.current_thread().name))
    #创建子线程   name传一个子线程名 args传数据
    t1 = threading.Thread(target=run,name="runThread",args=(6,))
    t2= threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    #等待线程结束
    t1.join()
    t2.join()
    print("num = "+str(num))
    print("主线程(%s)结束"%(threading.current_thread().name))
