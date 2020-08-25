#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:
#@function:-----------

from django import template
from datetime import datetime
from django.utils.safestring import mark_safe

register = template.Library()

#自定义过滤器
@register.filter(name="filter_1") #过滤器在模板中使用的名字
def filter_1(f1,f2):
    return f1 * f2
# register.filter("filter_1",filter_1)  这个也可以  不过还是装饰器看起来舒服点

#自定义标签 格式化时间
@register.tag(name="tags_1")

#需要装载标签
#解析器
def do_format(parse,token):  #parse是解析器对象 ，包含标签的名字和格式化的格式
    try:
        tag_name,format_string = token.split_contents()  #分离标签的名字和格式化对象
    except:
        raise template.TemplateSyntaxError('syntax')
    return CurrentNode(format_string[1:-1])  #传入模板的节点类   CurrentNode

class CurrentNode(template.Node):
    def __init__(self,format):
        self.format_string = str(format)

    #把当前时间格式化后返回
    def render(self, context):
        now = datetime.now()
        return now.strftime(self.format_string)


@register.tag(name="tags_2")
def makesafe(parse,token):
    try:
        name,tuple_value = token.split_contents()
        print(tuple_value)
    except:
        raise template.TemplateSyntaxError('synta')
    return makesafeclass(tuple_value[1:-1])

class makesafeclass(template.Node):
    def __init__(self,safetup):
        self.safetup = eval(safetup)  #不是string类型的话 都会转成string 这个传过来 "('xxx','fff')"  要在转换回原来的类型

    def render(self, context):
        temp_html = "<input type='text' id='%s' class='%s' />" % self.safetup
        return  mark_safe(temp_html)  #定义标签时，用上 mark_safe 方法，令标签语义化，相当于 jQuery 中的 html() 方法。
                                       #和前端HTML文件中的过滤器 safe 效果一样。在HTML中使用该自定义标签，在页面中动态创建标签


