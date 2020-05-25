'''
为每个线程开辟独立的空间 使属性独立

作用：为每一个线程绑定一个数据库链接，HTTP请求，用户身份等。这样每一个线程调用到的处理函数都可以非常方便的访问地访问到这些资源
'''

import threading,time

#创建一个ThreadLocal对象
#每个线程有独立的存储空间
#每个线程对ThreadLocal对象都可以读写 但互不影响
num = 0

local = threading.local()

def run(m,n):
    m+=n
    m-=n

def func(n):
    #每一个线程都有local.x 就是线程的局部变量
    local.x = num
    for i in range(100000):
        run(local.x,n)
    print("%s-%d"%(threading.current_thread().name,local.x))

if __name__ == "__main__":
    t1 = threading.Thread(target=func,name="runThread",args=(6,))
    t2 = threading.Thread(target=func,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num = "+str(num))



'''
控制线程数量
'''
sem = threading.Semaphore(3)

def run1():
    with sem:
        for i in range(5):
            print("%s-%d"%(threading.current_thread().name,i))
            time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run1).start()

