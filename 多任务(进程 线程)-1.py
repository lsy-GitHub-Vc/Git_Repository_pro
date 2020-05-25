'''
说白了 多任务的并行只存在于多核CPU上实现的，但当任务数多余CPU数 操作系统会把某些任务在某个CPU上轮流调度
并发：看上去一起执行，任务数多余CPU数
并行：真正的一起执行，任务数少于CPU数

全局变量在多个进程中不能共享

实现多任务的方式;
1、多进程模式
2、多线程模式
3、协程模式
4、多进程+多线程模式
'''
import time
#进程对象
from multiprocessing import Process
import os
'''
1、进程    一个任务就是一个进程
进程是系统中资源分配的基本单位 每个进程都有自己的 数据段 代码段 堆栈段
进程间的执行先后是不确定的
'''

def runc (str):
    #os.getpid() 进程号 os.getppid() 父进程号
    print("*******%s*******%s****%s" % (str,os.getpid(),os.getppid()))
    time.sleep(3)


if __name__ == "__main__":
    print("主(父)程序启动"+str(os.getpid()))

    #创建一个子进程对象 指明子进程方法 还可以给子进程方法内传参
    p = Process(target=runc,args=("lsy",))

    #启动
    p.start()

    #主进程一般不实现具体的功能 一般含有多个子进程 让他们去做具体的实现 join()就是等待所有子进程都实现完毕然后再去向下执行父进程（一般就结束了）
    p.join()
    print("父进程结束")
    time.sleep(1)