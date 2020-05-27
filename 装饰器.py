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

# -----------------------------------------------------------------------

def log(text):   #（1）接受装饰器传的值
    def decorator(func):  #（3）接受now调用
        @functools.wraps(func) #需要把原始函数的__name__等属性复制到wrapper()函数中，
        def wrapper(*args, **kw):#（5）接受调用 接受now的参数
            print('%s %s():' % (text, func.__name__))#方法体  func.__name__可以拿到函数名
            return func(*args, **kw) #（6）最终返回
        return wrapper #（4）接受后调用weapper方法
    return decorator #（2） 接受值后返回到decorator方法中

@log('execute')  #向装饰器本身传值 装饰器需要三层结构
def now():
    print('2020-3-25')
#print(now.__name__)  #如果没有@functools.wraps(func) now函数返回的函数名为wrapper(可能因为他是最后执行的实例)，但是对于某些依赖签名的函数执行会报错
#所以需要@functools.wraps(func)将签名重新指向调用函数now
now()

#偏函数
#定义参数就叫偏函数
def int2(str1,base=2): #base表示进制
    return int(str1,base)

print(int2("1010"))


#也有专门的模块
int3 = functools.partial(int,base=2) #其实就是固定了base的参数 其实int内的参数可以认为**args （10111）一个元祖 而base=2则为**kwargs
print(int3("10111"))
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单