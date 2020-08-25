#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file: 表单请求
#@function:-----------

''''''
'''GET方法请求数据'''

from django.http import HttpResponse
from django.shortcuts import render

#表单
def search_from(request):
    return render(request,'search_from_get.html',locals())

#接受请求数据
def search_get(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = ' 你搜索的内容: '+request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

