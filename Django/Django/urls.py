"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.urls.conf import path,re_path
from . import views,datadb,search_get,search_post,sear
from  django.contrib import admin

'''
Django 路由

Django1.1.x 版本
url() 方法：普通路径和正则路径均可使用，需要自己手动添加正则首位限制符号。

Django 2.2.x 之后的版本
    ·path：用于普通路径，不需要自己手动添加正则首位限制符号，底层已经添加。
    ·re_path：用于正则路径，需要自己手动添加正则首位限制符号。
'''

'''
正则路径中的有名分组
路由分发(include)
存在问题：Django 项目里多个app目录共用一个 urls 容易造成混淆，后期维护也不方便。

解决：使用路由分发（include），让每个app目录都单独拥有自己的 urls。

步骤：

    1、在每个 app 目录里都创建一个 urls.py 文件。
    2、在项目名称目录下的 urls 文件里，统一将路径分发给各个 app 目录。
    path("app01/", include("app01.urls")),
    path("app02/", include("app02.urls")),
'''





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.hello),
    path(r'my/',views.myread),
    url(r'stu/',views.study),
    path(r'zh/',views.study_1),
    path(r's2/',views.study_2),
    path(r's3/',views.study_3),
    path(r's4/',views.study_4),
    path(r's5/',views.study_5),
    path(r's6/',views.study_6),
    path(r"s7/",views.study_7),
    path(r"s8/",views.study_8),
    path(r"s9/",views.study_9),
    path(r"s10/",views.study_10),
    path(r'db1/',datadb.insertdb),
    path(r'db2/',datadb.selectdb),
    path(r'db3/',datadb.updatedb),
    path(r'db4/',datadb.deletedb),
    path(r'search_from/', search_get.search_from),
    path(r'search_get/', search_get.search_get),
    path(r'search_post/',search_post.search_post),
    path(r'search_post_1/', sear.search_post_1, name ="sear"),

    ]