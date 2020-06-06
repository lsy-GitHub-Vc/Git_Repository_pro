#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy


from collections import namedtuple,deque,defaultdict,OrderedDict


'''namedtuple'''

'''我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：'''
# p = (1,2)

# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：

point = namedtuple('point',['x','y'])
p = point(1,2)
print(p.x,p.y)

'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

可以验证创建的Point对象是tuple的一种子类：
'''

print(isinstance(p,tuple))  #True
print(isinstance(p,point))  #True
print(isinstance(point,tuple))  #False  #p即为tuple类型又为tuple类型  point不是tuple类型


#类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义
circle = namedtuple('circle',['x','y','r'])

'''deque'''
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

'''defaultdict: 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：'''

dic = defaultdict(lambda :'N/A')
dic['a'] = 'b'
print(dic['a'],dic['c'])  #key c 不存在返回'N/A'

# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

'''OrderedDict: 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict：'''
seqdic = dict([('a', 1), ('b', 2), ('c', 3)])
print(seqdic) # {'a': 1, 'b': 2, 'c': 3}  虽然一直是这样 看起来是有序的 但是还是用下面方式保险点
seqd = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(dict(seqd))
#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

