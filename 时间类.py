import time
#日历模块
import calendar
#time.clock() 可以监控程序运行的时间 3.8版本用的time.perf_counter()
sum = 0
for i in range(10000):
    sum +=i

#print(time.clock())
print(time.perf_counter())  #程序执行所需时间(系统执行时间)

time.process_time()  # 返回进程运行时间

#时间戳
print(time.time()) #1591341315.1846259

#当前时间 从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数
print(time.localtime(time.time())) #time.struct_time(tm_year=2020, tm_mon=6, tm_mday=5, tm_hour=15, tm_min=15, tm_sec=15, tm_wday=4, tm_yday=157, tm_isdst=0)

# 获取格式化的时间  你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
print(time.asctime(time.localtime(time.time())))  #Fri Jun  5 15:20:32 2020

#格式化日期 我们可以使用 time 模块的 strftime 方法来格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))  #2020-06-05 15:20:32

# 格式化成Fri Jun 05 15:21:38 2020形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))  #Fri Jun 05 15:21:38 2020

# 将格式字符串转换为时间戳
a = "Fri Jun 05 15:21:38 2020"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))  #1591341698.0

#返回指定某年某月的日历
print(calendar.month(2018,11))
#返回指定某年
print(calendar.calendar(2018))
#判断是否闰年 是为True
print(calendar.isleap(2018))
#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2018,11))




'''
python中时间日期格式化符号：

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''