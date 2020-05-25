'''
输出格式
'''
import os

print("a\nb\nc")
print('''
a
b
c
''')
#上面两种相同

#\t  制表符 默认4个空格  有的系统8个空格
print("a\tb")

#r 对于字符串内的字符不转义
print(r"a\\t\\b")

#字符串
print(eval("12+3"),eval("{'a':1}"),eval("['a',1]"))  #将字符串当成有效的表达式来求值并返回结果  15 {'a': 1} ['a', 1]
print("QWEqwe".lower())                                #字母转小写
print("QWEqwe".upper())                                #字母转大写
print("QWEqwe".swapcase())                             #字母大转小，小转大
print("qWEqwe".capitalize())                           #首字母大写其余小写
print("qWE qwe".title())                               #每个单词的首字母大写
print("qWEqwe".center(40,"*"))                         #填充一个字符类型r
print("qWEqwe".ljust(40,"$"),"*")                      #左对齐 字符填充不写默认空格
print("qWEqwe".rjust(40,"$"),"*")                      #右对齐 字符填充不写默认空格
print("qWEqwe".zfill(40))                               #右对齐 前面补0
print("qWEqwertyasd".count("q",3,12))                  #返回字符个数 可以加间隔段
print("qWEqwertyasd".find("q"))                        #返回字符第一次出现的下标位置 可以加间隔段(懒得写了)  没找到返回-1 rfing()从右向左找
print("qWEqwertyasd".index("s"))                       #和find相同 不同的是当找不到字符串时不会返回-1  而是会抛出异常
print("   qWEqwertyasd  ".strip())                     #去空格 lstrip()  rlstrip() 左去空格和右去空格  口号内可以填其他字符 例:strip("*")
print("12315".isdigit())                                #是否纯数字
print("qweqw".isalpha())                                #是否纯字母
print("qq11ww22".isalnum())                             #只能为数字和字母
# isupper 至少有一个大写英文其余是什么无所谓但不能有小写英文
#islower  和上面一样不过变成了小写
print("Hello Today".istitle())                          #是否为标题化   首字母大写
print("  ".isspace(),"\t".isspace(),"\n".isspace(),"\r".isspace())        #是否为纯空格及纯白符
print("qweqw".split("q",3))                             #字符串截取及截取个数
str1 = '''
lsy a is good man!
lsy a is nice man!
lsy a handsome man!
'''
print(str1.splitlines())                                  #针对于换行符 \r \r\n \n 的截取 参数为True时截取会保留换行符

list7 = ["a","b","c","d"]
print("x".join(list7))                                    #以指定的字符分隔符将list7中的元素组成一个字符串


#max  min  取最大最小值

str2 = "this a text text text charcter1"
str3 = str2.replace("text","rep",1)
print(str3)                                                #替换某些字符串 参数1是指替换一个 不写全部替换

'''
舍弃  不可控 风险太大
str4 = "this a text text text charcter1"
str5 = str.maketrans("text","play")   #创建字符对应表  这个是按单字节进行对应的 及t--p  e--l 会把字符串内的都替换掉
str6 = str4.translate(str5)           #字符替换        不可控制
print(str6)
'''

print(str2.startswith("this"))                             #是否已某字符串开头 可圈定范围
print(str2.endswith("er1"))                                #结尾

str8 = str2.encode()                                        #编码 默认参数为utf-8，strict(抛出错误异常) 但通常我们并不需要这个异常所以可以填ignore(不抛异常)
print(str8)

print(str8.decode("utf-8","ignore"))                       #解码 参数保证和编码时一致


print("--------------------------------------------------------------------------------------------------")

#列表
list1=[1,2,3,"back",5]
print(list1.extend([1,"sp",4,"bk"]),list1)              #添加列表（）
print(list1.insert(2,"0"),list1)                         #在下标处添加元素
print(list1.pop(),list1)                                 #删除下标处数据 不填参数默认删除最后一个元素
print(list1.remove("sp"),list1)                          #删除第一个匹配参数的元素
print(list1.index("back",1,6))                           #查询元素下标 可以限制范围 只规定开始下标也可以
print(list1.count("back"))                               #某一元素个数
print(list1.reverse(),list1)                             #倒序 元素反转 不牵扯数据本身大小 也适用于有str类型的
list2=[2,4,6,1,3,7,5]
print(list2.sort(),list2)                                #正序 会根据根据元素大小排序只适用于纯数字类型列表
print(max(list2))                                        #只适用于纯数字列表  min也一样
print(list1.clear(),list1)                               #清除所有元素(列表对象保留  [])

#拷贝
#浅拷贝
list3 = [1,2,3,4,5]
list4 = list3
list4.append(6)
print(list3,list4,id(list3),id(list4))                  #list4去拷贝list3时只是拷贝的list3的指针(在栈区(存的变量)  就是在栈取开辟了一个list3相同的空间)并没有开辟新的内存(堆区(存的数据))

#深拷贝
list5 = list3.copy()
list5.append(7)
print(list3,list5,id(list3),id(list5))                  #会在堆区开辟一个新空间



#元组
bins = (1,2,3,4,[1,2,3])
bins[-1][0] = 100           #在元组中list是在堆中不共享空间 元组储存的是list空间的指针 所以我们可以改变元组中list的值
print(bins)

#del bins                    #删除

#字典
dict1 = {"a":"b","c":"d"}
print(dict1.values())                                  #字典值 列表类型
print(dict1.keys())                                    #键值  列表类型
print(dict1.items())                                   #[('a', 'b'), ('c', 'd')]
print(dict1.pop("a"))                                   #删除键 会返回值

#dict和list比较  dict插入和查询快不会因为key-value增加而变慢  不过dict内存占用较多 会导致浪费 而list和他相反数据量大会变慢 但是占用内存较小


#set
#创建一个set需要一个list,dict或元组作为支撑  set只存储键值 时不可重复和无序的
s1 = set([1,2,3,4,2,3,4])
print(s1)

s2 = set((1,"2","c","z"))
print(s2)

s3 = set({"z":"x","c":"v"})
print(s3)

print(s3.add("2"),s3)                                       #添加 我们也可以添加一个元组因为它是不可变的
print(s3.update([6,7,8]),s3)                                #插入整个list tuple 字符串(字符串会以单个字符的形式插入) 打碎插入
print(s3.remove("z"),s3)                                    #删除元素
print(s2 & s3)                                              #交集
print(s2 | s3)                                              #并集
print("*********************************************************************************")

'''
#判断数字
num = input("输入一个不为0的正整数:")

if num.isdigit() == False:
    print("请输入正确的数字")
    os._exit(0)

num = int(num)
if num ==0:

    print("不能为0")
else:
    list6=[]
    i = 2
    if num % i == 0 :
        num /= i
        list6.append(i)
        if num == 1 :
            list6.append(1)
            print("该数字为偶数也是个质数约数为"+str(list6)+"组成的")
        else:
            while num != 1:
                if num % i == 0:
                    list6.append(i)
                    num /= i
                else:
                    i+=1
            print("该数字为偶数 约数为"+str(list6)+"组成的")
    else:
        if num == 1 :
            print("最小的奇数1")
        else:
            j = 3
            while num != 1:
                if num % j == 0:
                    list6.append(j)
                    num /= j
                else:
                    j+=2
            if len(list6) == 1:
                print("该数是一个奇数一同时是一个质数")
            else:
                print("该数是一个奇数由约数"+str(list6)+"组成")
'''