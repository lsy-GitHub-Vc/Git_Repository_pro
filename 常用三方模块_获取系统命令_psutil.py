#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy

'''psutil'''
'''
用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，
如ps，top，free等等。要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。

在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，
它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
'''

import psutil

'''获取CPU信息'''
#我们先来获取CPU的信息：
print(psutil.cpu_count())  # 4  cpu逻辑数量
print(psutil.cpu_count(logical=False)) # 4 cpu物理核心
# 2说明是双核超线程, 4则是4核非超线程

#统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

#再实现类似Liunx top命令的CPU使用率，每秒刷新一次，累计10次：
# for i in range(10):
#     print(psutil.cpu_percent(interval=1,percpu=True))  #一秒刷一次
    #print(psutil.cpu_times_percent(interval=3,percpu=True))  #这个单位我搞不懂 结果和cpu_times()挺像的不过 它返回的是三次结果


'''获取内存信息'''
#使用psutil获取物理内存和交换内存信息，分别使用
print(psutil.virtual_memory())  #svmem(total=8459030528, available=1557372928, percent=81.6, used=6901657600, free=1557372928)
print(psutil.swap_memory())     #sswap(total=15807361024, used=13962596352, free=1844764672, percent=88.3, sin=0, sout=0)

# 返回的是字节为单位的整数，可以看到，总内存大小是8459030528 = 8 GB，已用6901657600 = 6.9 GB，使用了81.6,%。
# 而交换区大小是15807361024 = 1.5 GB。


'''获取磁盘信息'''
#可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
print(psutil.disk_partitions()) #磁盘分区信息
# [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed')]

print(psutil.disk_usage('C:'))#磁盘使用情况  sdiskusage(total=64424505344, used=49839775744, free=14584729600, percent=77.4)

print(psutil.disk_io_counters())#磁盘IO  sdiskio(read_count=3769862, write_count=4476124, read_bytes=128562923520, write_bytes=99030957568, read_time=12706, write_time=5340)

#可以看到，磁盘'C:'的总容量是64424505344 = 64 GB，使用了77.4%。文件格式是NTFS，opts中包含rw表示可读写，journaled表示支持日志。


'''获取网络信息'''
#psutil可以获取网络接口和网络连接信息：
print(psutil.net_io_counters()) #获取网络读写字节/包的个数  snetio(bytes_sent=2624082, bytes_recv=54685829, packets_sent=23147, packets_recv=42934, errin=0, errout=0, dropin=0, dropout=0)
print(psutil.net_if_addrs()) #获取网络接口信息
print(psutil.net_if_stats()) #获取网络接口状态

print(psutil.net_connections())#获取当前网络连接信息
# 你可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限，这种情况下，
# 可以退出Python交互环境，用sudo重新启动：

# $ sudo python3
# Password: ******
# Python 3.8 ... on darwin
# Type "help", ... for more information.
# >>> import psutil
# >>> psutil.net_connections()


'''获取进程信息'''
#通过psutil可以获取到所有进程的详细信息：
print(psutil.pids()) #获取进程id
print(psutil.Process(12740))  #获取指定进程ID=12740
print(psutil.Process(12740).name())#获取该进程名
print(psutil.Process(12740).exe())#获取该进程exe的路径
print(psutil.Process(12740).cwd())#获取该进程工作目录
print(psutil.Process(12740).cmdline())#获取该进程启动的命令行
print(psutil.Process(12740).ppid()) #父进程id
print(psutil.Process(12740).parent())#父进程
print(psutil.Process(12740).children())#子进程列表
print(psutil.Process(12740).status())#进程状态
print(psutil.Process(12740).username())#进程用户名
print(psutil.Process(12740).create_time())#进程创建时间
print(psutil.Process(12740).cpu_times())#进程使用cpu的时间
print(psutil.Process(12740).memory_info())#进程使用的cpu
print(psutil.Process(12740).open_files())#进程打开的文件
print(psutil.Process(12740).connections())#进程相关的网络连接
print(psutil.Process(12740).num_threads())#进程的线程数量
print(psutil.Process(12740).threads())#进程所有的线程信息
print(psutil.Process(12740).environ())#进程的环境变量
#print(psutil.Process(12740).terminate())#结束进程

'''
和获取网络连接类似，获取一个root用户的进程需要root权限，启动Python交互环境或者.py文件时，需要sudo权限。

psutil还提供了一个test()函数，可以模拟出ps命令的效果：
'''

print(
    psutil.test()
)

'''
psutil使得Python程序获取系统信息变得易如反掌。

psutil还可以获取用户信息、Windows服务等很多有用的系统信息，
'''