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
# path = r"E:\readw.txt"
# file1 = open(path,"r")

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
path1 = [r"E:\PyCharm\project\测试文件\wh.txt",r"E:\PyCharm\project\测试文件\wh1.txt"]

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
path2 = r"E:\PyCharm\project\测试文件\wh.txt"
arrlist = [1,2,3,4,5,"This is the test file"]
arrlist1 = {"a":"test","b":None}
with open(path2,"wb") as file6:
    pickle.dump(arrlist1,file6)

file6.close()
#读该文件
with open(path2,"rb") as file7:
    print(pickle.load(file7))

file7.close()

'''StringIO,ByteIO :  很多时候，数据读写不一定是文件，也可以在内存中读写。 '''

#StringIO    内存中读写Str

from io import StringIO,BytesIO


FStr = StringIO()

with open(path1[1],"r+",encoding="utf-8") as file8:
    for xl in file8.readlines():
        FStr.write(xl.rstrip('\n')+"*")   #在StringIO的实例用write写入内存   用read()是读不到的


print(FStr.getvalue()) #获取写到内存中的数据

with open(path1[0],"a+",encoding="utf-8") as file9:
    for op in FStr.getvalue().split("*"):
        file9.write(op+'\n')

FStr.close()


FStry = StringIO('Hello!\nHi!\nGoodbye!')

SF = FStry.readlines()
for Hr in SF:
    print(Hr)

FStry.close()


'''ByteIO   StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。'''

# 写
Bf = BytesIO()
print(Bf.write("中文".encode("utf-8")))

print(Bf.getvalue())

Bf.close()

#读  b'\xe4\xb8\xad\xe6\x96\x87'

BI = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(BI.read().decode(encoding='utf-8'))
print(BI.getvalue().decode(encoding='utf-8'))
print(BI.read(),BI.getvalue())
BI.close()



'''序列化：我们把变量从内存中变成可存储或传输的过程称之为序列化  在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。'''

#E:\PyCharm\project\测试文件\序列化测试文档

import pickle
#对象序列化 写入文件

#dumps 和 dump   前一个应该传入一个对象，后一个可以传入两个参数 包含一个文件IO流的对象 可以同时写入文件

pathseq = r'E:\PyCharm\project\测试文件\序列化测试文档'
d = dict(name='Bob', age=20, score=88)

#print(pickle.dumps(d))  #结果 b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\
                        # x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.' 这些都是Python保存的对象内部信息。

with open(pathseq,"wb") as fileseq:
    pickle.dump(d,fileseq)


#loads()和load() :当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象(和dumps对应)，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：

with open(pathseq,"rb") as filereadseq:
    print(pickle.load(filereadseq))    #{'name': 'Bob', 'age': 20, 'score': 88}



'''JSON:如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
    因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，
    并且比XML更快，而且可以直接在Web页面中读取，非常方便。'''

import json

print(json.dumps(d))
#由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。



class Students(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    # def __str__(self):
    #     return "%s %s %s" % (self.name,self.age,self.score)     #御坂 18 90

# def StuSeq(std):    #这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
#     return {
#         "name" : std.name,
#         "age"  : std.age,
#         "score": std.score
#     }
s = Students('baby',20,60)
# print(json.dumps(s,default=StuSeq))
#没有转换函数StuSeq的情况下  TypeError: Object of type Students is not JSON serializable

'''误的原因是Student对象不是一个可序列化为JSON的对象。

如果连class的实例对象都无法序列化为JSON，这肯定不合理！

别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：

https://docs.python.org/3/library/json.html#json.dumps

这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。

可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：'''

#不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：

print(json.dumps(s,default=lambda obj:obj.__dict__))

'''
因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，
我们传入的object_hook函数负责把dict转换为Student实例：'''

def RevStuSeq(dic):
    return Students(dic["name"],dic["age"],dic["score"])


dic_str = '{"score":90,"name":"御坂","age":18}'
#print(eval(dic_str)) #字符串的字典 转换为字典
print(json.loads(dic_str,object_hook=RevStuSeq))     #这个就是Students的实例  用__str__打印出的实例中的属性：  御坂 18 90



'''小结：Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，
当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
既做到了接口简单易用，又做到了充分的扩展性和灵活性。'''