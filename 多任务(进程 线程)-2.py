from multiprocessing import Pool,Process,Queue
import os,random,time

def run(name):
    print("子进程%s启动--%s"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("子进程%s结束--%s--耗时%.2f"%(name,os.getpid(),start-end))

def run1(name):
    print("1____子进程%s启动--%s"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("1____子进程%s结束--%s--耗时%.2f"%(name,os.getpid(),start-end))

'''
进程间通讯   Queue队列

'''
def write(pc):
    print("启动写的子进 程--%s"%(os.getpid()))
    for qu in ["A","B","C","D"]:
        pc.put(qu)
    print("结束写的子进程--%s"%(os.getpid()))

def read(pc):
    print("启动读的子进程--%s"%(os.getpid()))
    while True:  #出啊过来的数据是一个内存地址 无法确定长度  所以只能用死循环读取 读完后调用    pr.terminate() 强制杀死
        print("value = %s"%(pc.get(True)))  #每次循环读一数据
        print("结束读的子进程--%s"%(os.getpid()))

if __name__=="__main__":
    print("父进程启动")

    #创建多个进程
    #创建进程池
    #cpu核心数 4核的 写不写都行
    pp = Pool(4)

    for i in range(5):
        #创建进程 放入进程池统一管理
        pp.apply_async(run,args=(i,))
    for j in range(5):
        #创建进程 放入进程池统一管理
        pp.apply_async(run1,args=(j,))

    #进程池join之前必须调用close,调用close后就不能继续添加新的进程了
    pp.close()
    #进程池中的join 会等待进程池中的所有子进程都结束完毕 才会继续执行父进程
    pp.join()

    '''创建一个消息队列用于进程间通讯'''
    pc = Queue()
    '''创建进程'''
    ps = Process(target=write,args=(pc,))
    pr = Process(target=read,args=(pc,))

    ps.start()
    pr.start()

    ps.join()
    #terminate() 强制结束进程 因为du的方法是由死循环持续的读 可以理解为写的进程停止读的方法也会被强行停止
    pr.terminate()

    print("父进程结束")



'''子进程：很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的'''

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])   #nslookup  这个是运行命令吧   类似打开应用吧  反正就是规定一个子进程的功能吧
print('Exit code',r)

#结果：
# $ nslookup www.python.org
# Server:		192.168.19.4
# Address:	192.168.19.4#53
#
# Non-authoritative answer:
# www.python.org	canonical name = python.map.fastly.net.
# Name:	python.map.fastly.net
# Address: 199.27.79.223
#
# Exit code: 0

'''如果子进程还需要输入，则可以通过communicate()方法输入：'''
print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode(encoding='gbk'))
print('Exit code:',p.returncode)



#上面的代码相当于在命令行执行命令nslookup，然后手动输入： set q=mx
#                                                       python.org
#                                                       exit

# $ nslookup
# 默认服务器:  bogon
# Address:  192.168.43.1
#
# > > 服务器:  bogon
# Address:  192.168.43.1
#
# python.org	MX preference = 50, mail exchanger = mail.python.org
# >
# Exit code: 0

#说实话不太懂