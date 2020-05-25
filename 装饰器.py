import functools

#装饰器
def outer(func):
    def inner(*args,**kwargs): #可以不定长参数 但最多通常6、7个 一个参数的话**kwargs是一个空的字典
        #添加修饰的功能
        #*args 元组   **kwargs 字典
        if kwargs.get("age") > 18:
            print("恭喜成年")

        print("********"+args[0])
        func(*args,**kwargs)

    return inner

@outer          #引用装饰器 @+方法名
def say(name,age):
    print("my name is %s ,I am %d years old " % (name,age))


say("shy",age=20)


#偏函数
#定义参数就叫偏函数
def int2(str1,base=2): #base表示进制
    return int(str1,base)

print(int2("1010"))


#也有专门的模块
int3 = functools.partial(int,base=2)
print(int3("10111"))