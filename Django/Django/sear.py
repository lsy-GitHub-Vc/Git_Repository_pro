#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:
#@function:-----------

from  django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from django.urls import reverse


def search_post_1(request):
    if request.method == "GET":
        return HttpResponse("随便写点")
    else:
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        if username == "sear1" and pwd == "sear1":
            return HttpResponse("这是猜对了？")
        else:
            return reverse('sear')
