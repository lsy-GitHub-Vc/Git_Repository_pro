#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy

# def foo_1():
#     pass
#
# try:
#     foo_1()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')
#
#
# '''
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
#
# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
#
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning
# '''
#
# '''使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用bar()，bar()调用foo()，结果foo()出错了，这时，只要main()捕获到了，就可以处理：'''
# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#         '''记录错误:    如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，
#           就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
#           Python内置的logging模块可以非常容易地记录错误信息：  同样是出错，但程序打印完错误信息后会继续执行，并正常退出：'''
#         #logging.Exception(e)
#     finally:
#         print('finally...')
#
#
# # 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。
#
#
# '''调用栈   如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出'''
#
#
#
#
# ''' 抛出错误:  因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
#     Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
#
#     如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例'''
#
# class FooError(ValueError):
#     pass
#
# def fo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# fo('0')
#
# '''只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
#     尽量使用Python内置的错误类型。
#
# 最后，我们来看另一种错误处理的方式：'''
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()
#
# '''
# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
#
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，
# 所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，
# 就一直往上抛，最终会抛给CEO去处理。
#
# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
# '''
#
# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!') #只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。
#
# '''调试：  写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。
#
# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。  那就看下logging吧  其他的就不管了'''
#
# #logging不会抛出错误，而且可以输出到文件：
#
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n=>%d' % n)
# print(10/n)
#
# '''
# logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError: division by zero，没有任何信息。怎么回事？
# 别急，在import logging之后添加一行配置再试试： logging.basicConfig(level=logging.INFO)
#
#
# 结果： 文件解释器运行时
# $ python err.py
# INFO:root:n = 0
# Traceback (most recent call last):
#   File "err.py", line 8, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero
#
#
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件
# '''
#
#
#

'''单元测试：
  如果你听说过“测试驱动开发”（TDD：Test-Driven Development），单元测试就不陌生。

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

比如对函数abs()，我们可以编写出以下几个测试用例：

1、输入正数，比如1、1.2、0.99，期待返回值与输入相同；

2、输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；

3、输入0，期待返回0；

4、输入非数值类型，比如None、[]、{}，期待抛出TypeError。

把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。

如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通过，要么函数有bug，要么测试条件输入不正确，
总之，需要修复使单元测试能够通过。

单元测试通过后有什么意义呢？如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，如果通过，
说明我们的修改不会对abs()函数原有的行为造成影响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。

这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，
可以极大程度地保证该模块行为仍然是正确的。

我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：'''

class Dict(dict):


    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Dict object has no attribute %s' % key)

    def __setattr__(self, key, value):
        self[key] = value


    # if __name__ == '__main__':
    #     import doctest   #执行注释部分的代码
    #     doctest.testmod()

# d = Dict(a=1,b=2)
# print(d['e'])

#为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：

from 错误_调式和测试 import Dict
import unittest

class TestDict(unittest.TestCase):

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty



    if __name__ == '__main__':
        unittest.main()

'''
编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，
我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：
'''

#self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等


#另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError
#
# with self.assertRaises(KeyError):
#     value = d['empty']


# 而通过d.empty访问不存在的key时，我们期待抛出AttributeError：
#
# with self.assertRaises(AttributeError):
#     value = d.empty




'''
运行单元测试
一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：

if __name__ == '__main__':
    unittest.main()

这样就可以把mydict_test.py当做正常的python脚本运行：

$ python mydict_test.py
另一种方法是在命令行通过参数-m unittest直接运行单元测试：

$ python -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。

'''

'''
setUp与tearDown：
可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，
这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：'''

# class TestDict(unittest.TestCase):
#
#     def setUp(self):
#         print('setUp...')
#
#     def tearDown(self):
#         print('tearDown...')





'''文档测试：如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。比如re模块就带了很多示例代码：
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
  这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，
  那么，可不可以自动执行写在注释中的这些代码呢？答案是肯定的。'''