import os
import collections
import time
'''
遍历一个目录打印出该目录下的所有文件及目录,当是目录时继续进入目录下打印该目录下信息


1、深度遍历(栈遍历) 在栈中采用先进后出的模式存取数据
2、广度遍历（队列遍历）在队列中采用先进先出的模式存储数据
'''

#深度遍历
def traAllFile(filePath):

    shedList = [] #创建一个模拟的栈列表

    shedList.append(filePath) #将目录添加到栈中

    while len(shedList) != 0:
        #从栈里取出数据
        dirlistpop = shedList.pop()
        #获取目录下文件
        bydirlist = os.listdir(dirlistpop)
        #print(bydirlist)

        for pathfileml in bydirlist:
            #拼接地址
            filepathasb = os.path.join(dirlistpop,pathfileml)
            #判断是否为目录
            if os.path.isdir(filepathasb):
                shedList.append(filepathasb)
                print("这是个目录:"+pathfileml)
            else:
                print("普通文件:"+pathfileml)

traAllFile("D:\ceshiwenjianjia")

print("-----------------------------分割线-------------------------------------")

#广度遍历
def roomAllFile(romallfile):
    queuelist = collections.deque() #创建一个模拟队列

    queuelist.append(romallfile)

    while len(queuelist) != 0:

        queuelistpop = queuelist.popleft()#从左至右

        quefilelist = os.listdir(queuelistpop)#读目录

        for filetread in quefilelist:
            #拼路径
            readfilepath = os.path.join(queuelistpop,filetread)

            if os.path.isdir(readfilepath):#判断是否为目录
                queuelist.append(readfilepath)
                print("这是个目录:"+filetread)
            else:
                print("普通文件:"+filetread)

roomAllFile("D:\ceshiwenjianjia")