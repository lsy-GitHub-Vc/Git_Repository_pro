'''
格式：
try:
    语句1
except 错误码 as e:
    语句2
......
except 错误码 as e:
    语句n
esle:               可有可无
    语句e


try.....except.....finally  一般用这个吧
'''


#例子

try:
    print(3 / 0)
    print(num)
except ZeroDivisionError as e:
    print("除数为0了")
except NameError as e:
    print("没有该变量")
else:
    print("***********")



#使用except而不使用任何错误类型  一般都这样
try:
    print(4/0)
except:
    print("程序异常")

try:
    print(5/0)
except (ZeroDivisionError,NameError):
    print("出现了ZeroDivisionError或NameError异常")

#错误都继承自BaseException


#断言
#例子
'''
def ass(num,div):
    #给某些变量加一些限制说明  在抛异常时更加明确
    assert div != 0,"div不能等于0"
    return num/div

print(ass(10,0))
'''

#文件读写
#1、打开文件
'''
open(path,flag[,encoding][,errors]) 文件路径，打开方式 [编码][错误处理]
打开方式
r  只读 句柄在开头（就是文件描述符）
rb 读二进制方式打开
r+ 读写 开头
w  打开一个文件只用于写入 如果文件存在会覆盖 不存在则创建
wb 打开文件写入二进制
w+ 打开一个文件用于读写
a  用于文件追写 ，如果文件存在 文件句柄会放到末尾
a+
'''

#例子
path = r"E:\readw.txt"
file1 = open(path,"r")

#读文件
#str1 = file1.read(10)  #不传参读全部  传参读字符数
#print(str1)

#str2 = file1.readline() #读一行 参数也是字符数
#print(str2)

#str3 = file1.readlines() #读出所有行 并返回一个list   若给定的数字大于0，返回的实际size字符的行数
#print(str3)

#修改文件描述符的位置
#file1.seek()     #参数内填的就是开始的字符位置 0就是开头  可以设置间隔 比如3---15 就是读4到十五处的字符

#file1.close()



#with (open(path,"r",encoding="utf-8")) as file2:
#    print(file2.readlines())


#写文件
path1 = [r"E:\PyCharm\project_1\测试文件\wh.txt",r"E:\PyCharm\project_1\测试文件\wh1.txt"]

#file3 = open(path1,"w")

#file3.write("dsfgdfgjhjgfdssdfSDFDSA")

#文件是写入缓冲区的  flush()可以立即刷新缓冲区 使数据写入  当缓冲区满的时候也会自动刷新 close()也会刷新
#file3.flush()
#file3.close()

#调用whit...as...这个函数是我们可以重写__enter__和__exit__这两个函数 whit是调用这两个进行开始和结束的 我们可以重新定义它
#来满足我们的一些需求 适用于关闭某些资源 比如线程 事务 及一次写入多个文件 另一种方法调用内置库from contextlib import contextmanager
'''
class ent(object):
    def __init__(self,path2):
        self.path2 = path2
        self.hand = open(path2,"a")
    def __enter__(self):
        return self.hand
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.hand.close()
'''

from contextlib import contextmanager

#和上面的方法差不多
@contextmanager
def context(path3):
    fil = open(path3,"a")

    try:
        #类似于return但是yield返回的是一个生成器， 一个生成器就是一个可迭代的对象(迭代对象不一定是生成器哟)
        yield fil
    finally:
        fil.close()

for j in path1:
    with context(j) as file4 :
        file4.write("asdsadac")



#特殊数据写入
#数据持久性包
import pickle

#对于数据为list tuple dict set的数据写入
path2 = r"E:\PyCharm\project_1\测试文件\wh.txt"
arrlist = [1,2,3,4,5,"This is the test file"]
arrlist1 = {"a":"test","b":None}
with open(path2,"wb") as file6:
    pickle.dump(arrlist1,file6)

file6.close()
#读该文件
with open(path2,"rb") as file7:
    print(pickle.load(file7))

file7.close()