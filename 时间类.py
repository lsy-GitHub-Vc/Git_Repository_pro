import time
#日历模块
import calendar
#time.clock() 可以监控程序运行的时间 3.8版本用的time.perf_counter()
sum = 0
for i in range(10000):
    sum +=i

#print(time.clock())
print(time.perf_counter())

#返回指定某年某月的日历
print(calendar.month(2018,11))
#返回指定某年
print(calendar.calendar(2018))
#判断是否闰年 是为True
print(calendar.isleap(2018))
#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2018,11))