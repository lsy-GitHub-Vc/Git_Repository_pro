#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:
#@function:-----------

from django.http import HttpResponse
from django.shortcuts import render
from Endeavor.models import stu_2

'''插入数据'''
def insertdb(request):
    s2 = stu_2(name = "db2")
    s2.save()
    return HttpResponse("<p> 数据添加成功 </p>" )


'''获取数据'''
def selectdb(request):
    #初始化
    response = ""
    responsel = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    datalist = stu_2.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    res = stu_2.objects.filter(id = 1)

    #获取单个对象
    res1 = stu_2.objects.get(id = 1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    res2 = stu_2.objects.order_by("name")[0:2]

    #数据排序
    res3 = stu_2.objects.order_by("id")

    # 上面的方法可以连锁使用
    res4 = stu_2.objects.filter(name="db1").order_by("id")

    #for var in datalist:
    #for var in list(res):
    # for var in res2:
    # for var in res3:
    for var in res4:
        responsel += var.name+" "
    response = responsel        #这很正常 没有人会循环给web展示数据
    return HttpResponse("<li>"+response+"</li>")


'''更新数据'''
def updatedb(request):
    #修改一个id=1的name字段
    upd = stu_2.objects.get(id = 1)
    upd.name = "db0"
    upd.save()

    #也可以
        #upone = stu_2.objects.filter(id = 1).update(name ="db0")   #这个会返回影响数吧

    #修改所有列
    #upall = stu_2.objects.all().update(name = "db0")
    return HttpResponse("<p>修改成功</p>")


'''删除数据'''
def deletedb(request):
    #删除id = 3 的数据
    delone = stu_2.objects.get(id = 3)
    delone.delete()

    #也可
    #delone = stu_2.objects.filter(id = 3).delete()  #返回影响数吧

    #删除所有数据
    #delall = stu_2.objects.all().delete()

    return  HttpResponse("<p> 删除成功</p>")