from types import MethodType
#给类添加方法
'''
重写的两个函数：
__str__()
__repr__()

self 代表当前调用的属性

python中当函数执行结束对应的属性和对象也将释放，也可通过del+对象或属性进行对象的释放和属性的删除

权限私有化

限制添加的属性
'''

class Prece():

    #__slots__ = ("name","age","height","__weight") #设置添加属性限制 非下列属性不可添加
    #self 代表当前被调用的属性 __init__构造函数  现在相当于重写了一个构造函数
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.__weight = weight #前面加__ 私有化属性 使外部不能更改 想要更改需要通过内部函数实现


    def setWeight(self,weight):
        #数据过滤
        if weight < 0:
            weight = 0
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    '''
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,weight):
        #数据过滤
        if weight < 0:
            weight = 0
        self.__weight = weight
    '''
    def __str__(self):
        return "%s-%d-%d-%d" % (self.name,self.age,self.height,self.__weight)

    #def __repr__(self):
        #return "%s-%d-%d-%d" % (self.name,self.age,self.height,self.weight)

    def  acquittal(self):
        print("对象释放")

    #析构函数本身基本没什么操作 用于解析构造函数 不写也默认存在
    def __del__(self):
        print("析构函数")


per = Prece("hehe",20,170,60)
#print(per.name,per.age,per.height,per.weight)
print(per)
#手工释放per函数
#del per
per.acquittal()

#while 1 :
    #pass

per1 = Prece("haha",30,180,70)
#per1.age = 40 #修改了age
#per1.money = 100 #添加新属性
#print(per1.money)
per1.setWeight(50)
#per1.weight(50)
print(per1)
per1.acquittal()

def addbrc(addoder):
    print("--------%s" % (addoder))

per1.addty = MethodType(addbrc,"ceshifangfa") #添加方法 后面方法名和参数
per1.addty() #可以正常执行 在per1对象中有addty()

per1.addtyp = 123
print(per1.addtyp)