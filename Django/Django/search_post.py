#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:
#@function:-----------

from  django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.views.decorators import csrf

'''POST方法请求数据'''
#之前我们使用了GET方法。视图显示和请求处理分成两个函数处理。
#提交数据时更常用POST方法。我们下面使用该方法，并用一个URL和处理函数，同时显示视图和处理请求

#接受post请求
def search_post(request):
    ctx = dict()
    if request.method == "POST":
        ctx["rlt"] = request.POST["q"]
    return render(request,"search_from_post.html",ctx)



'''
随着功能的增加，路由层的 url 发生变化，就需要去更改对应的视图层和模板层的 url，非常麻烦，不便维护。

这时我们可以利用反向解析，当路由层 url 发生改变，在视图层和模板层动态反向解析出更改后的 url，免去修改的操作。

反向解析一般用在模板中的超链接及视图中的重定向。
'''

#设置了别名
def search_post_1(request):
    if request.method == "GET":
        return HttpResponse("随便写点")
    else:
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        if username == "sear1" and pwd == "sear1":
            return HttpResponse("这是猜对了？")
        else:
            return redirect(reverse('sear'))







'''
request 这个参数是一个 HttpRequest 对象 HttpRequest对象包含当前请求URL的一些信息：
    比如上面的 method参数 通过它我们可以获取请求类型 GET或POST 还有其他的参数 用到的话自己找吧
    https://www.runoob.com/django/django-form.html
'''


'''
QueryDict对象:

在HttpRequest对象中, GET和POST属性是django.http.QueryDict类的实例。

QueryDict类似字典的自定义类，用来处理单键对应多值的情况。

QueryDict实现所有标准的词典方法。还包括一些特有的方法：
https://www.runoob.com/django/django-form.html
'''