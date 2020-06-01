#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy


'''
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，
我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，
但是，从编程习惯上不应该引用private函数或变量。

private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：
'''
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

'''
我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
'''
print(greeting('lsy'))

# "----------------------------------------------------------------------------------------------"

'''
关于类和实例及self
'''
class Student(object):
    '''
    __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
    '''
    def __init__(self, name, score, age): #这个是每一个构造函数的初始化方法
        self.__name = name
        self.__score = score
        self.__age = age
    #get方法用于返回class内的属性值 避免外部直接访问
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def get_age(self):
        return self.__age
    #set 用于修改属性值
    def set_score(self,score):
        if 0 < score < 100:
            self.__score = score
        else:
            raise ValueError("超限")
    #和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
    def print_score(self):
        print('%s: %d: %d' % (self.__name, self.__score,self.__age))

bart = Student('Bart Simpson', 59,20)  #一个类的实例
#print(bart._Student__name)  # 不可访问内部属性已经私有化  不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量  不要这么干
#bart.print_score()
#bart.set_score(69)
print(bart.get_name())
print(bart.get_score())
print(bart.get_age())

'''
多态：当我们用一个class创建一个类的时候 比如class a(object): def run(self) 同时我们也创建了一个类型a 和list tuple dict差不多 ，
当另一个类 继承 a 时 比如 class b(a)：def run(self),class c(a): def run(self)... 这些子类b和c的类型也继承a  isinstance(b,a)结果为True 及类型相同
同样如果有类继承b和c 他们的类型依然是a同时也是b或c 以为子类的类型是跟随父类的 所以继承链条越长 靠下的类所属类型就越多(其实这样并不好
链条越长结构也会变得冗余，关键会使子类的多样性变得复杂，应该使用多重继承 后面说)。我们按照a类型进行操作，因为子类都是都是a类型(统一操作类型)，
所以我们创建一个a类型的函数时def d(a): a.run,  我们呢调用 a或者他的子类传入任意类型 它就会自动调用实际类型的内部方法，
不管之前是如何调用的 比如：在def d(b()) 就是调用的class b 的实例内的run方法  调用方只管调用，不管细节，而当我们新增一种Animal的子类时，
只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
对扩展开放：允许新增a子类；
对修改封闭：不需要修改依赖a类型的d等函数。

其实说白了 创建一个父类类型的函数d 可以通过实例自由调用父类和其子类 因为他们属于同一类型a 当添加子类时也不需要修改外部调用的d函数
，我们只需要调用就可以了


静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入a类型，则传入的对象必须是a类型或者它的子类，否则，将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入a类型。我们只需要保证传入的对象有一个run()方法就可以了：

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子



小结
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
'''



'''
#多重继承

小结
MixIn:允许一个子类继承多个父类，这样一来我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
如编写一个多线程模式的UDP服务，定义如下: class MyUDPServer(UDPServer, ThreadingMixIn):
                                            pass
由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
只允许单一继承的语言（如Java）不能使用MixIn的设计。
'''