#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:
#@function:----------

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello Word")

def myread(request):
    return HttpResponse("My name is xxx")

#传统传值
def study(request):
    context = dict()
    context['DUY'] = "study hard and make progress every day"
    return render(request,"django_study.html",context)


def study_1(request):
    return render(request,"django_study.html",{'DUY':"好好学习，天天向上"})

#测试列表取值
def study_2(request):
    return render(request,"django_study.html",{'varlist':["好好学习","天天向上"]})

#测试字典取值
def study_3(request):
    return render(request,"django_study.html",{'vardict':{"name":"mr zhangsan"}})

import datetime
#测试模板中datetime转换
def study_4(request):
    date1 = datetime.datetime.now()
    return render(request,"django_study.html",{"time":date1})

#模板 safe 该数据是安全的，不必对其进行转义，可以让该数据语义生效。
def study_5(request):
    url = "<a href='https://hao.360.com/'>360链接</a>"
    return render(request,"django_study.html",{"url":url})

#模板 if/else
def study_6(request):
    return render(request,"django_study.html",{"score":60})

#模板 for迭代
def study_7(request):
    return render(request,"django_study.html",{"iter":["one","two","three","four"]})

#模板 items迭代
def study_8(request):
    return render(request,"django_study.html",{"dic":{"henan":"zhengzhou","hebei":"chengde"}})

#模板 empty 循环为空时执行
def study_9(request):
    return render(request,"django_study.html",{"emptys":[]})

#自定义过滤器
def study_10(request):
    return render(request,"django_study.html",{"temp":10})