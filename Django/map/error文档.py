#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file: error
#@function:-----------


'''Django error:'''

'''
modle模块连接数据库时：

原因是 MySQLclient 目前只支持到 Python3.4，因此如果使用的更高版本的 python，需要修改如下：

通过报错信息的文件路径找到 ...site-packages\Django-2.0-py3.6.egg\django\db\backends\mysql 这个路径里的 base.py文件，
把这两行代码注释掉（代码在文件开头部分）：

if version < (1, 3, 13):
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
'''