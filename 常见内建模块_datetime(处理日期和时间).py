#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy


'''内建'''

from datetime import datetime,timedelta,timezone

'''datetime : datetime是Python处理日期和时间的标准库'''

######获取当前日期和时间
nowtime = datetime.now()
print(nowtime)      #2020-06-05 15:27:10.316288
print(type(nowtime))   #datetime.now()返回当前日期和时间，其类型是datetime。

#获取指定日期和时间
print(datetime(2020,6,5,15,29))    #2020-06-05 15:29:00


#####datetime转换为timestamp
'''
在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0
（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
你可以认为：
    timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
对应的北京时间是：
    timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。
'''
######把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
dtime = datetime(2020,6,5,15,29)
print(dtime.timestamp())  #1591342140.0   注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

######timestamp转换为datetime
print(datetime.fromtimestamp(1591342140.0))  #2020-06-05 15:29:00  这是转换为本地时间 就是北京时间  北京是东8区 所以和的格林威治标准时间差八个小时

#timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(1591342140.0)) #2020-06-05 07:29:00    格林威治标准时间


######str转换为datetime
#很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
print(datetime.strptime('2020-6-5 18:19:59', '%Y-%m-%d %H:%M:%S'))


######datetime转换为str
print(datetime.now().strftime('%a, %b %d %H:%M'))


######datetime加减

#对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：

#print(nowtime+timedelta(hours = 10))
print(nowtime+timedelta(days = 1,seconds = 5,minutes = 4,hours = 2))#加了一天零2小时4分5秒

#能加也能减 都一样 就不写了


######时区转换
#我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：

# 拿到UTC时间，并强制设置时区为UTC+0:00:
dte = datetime.utcnow().replace(tzinfo=timezone.utc)
print(dte)
# astimezone()将转换时区为北京时间:
da_bj = dte.astimezone(timezone(timedelta(hours = 8)))
print(da_bj)
# astimezone()将转换时区为东京时间:
da_dj = dte.astimezone(timezone(timedelta(hours = 9)))
print(da_dj)
'''
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。

利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述da_bj到da_dj的转换
'''



'''小结：datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。'''