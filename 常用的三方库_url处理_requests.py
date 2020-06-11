#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy

'''我们已经讲解了Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。

更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。'''


'''使用requests
要通过GET访问一个页面，只需要几行代码：'''

import requests

reque = requests.get(r'https://hao.360.com/',timeout = 2.5)  #获取连接的对象
#print(reque.status_code)  #行数吧
# print(reque.text)     #网页数据  <!DOCTYPE html>\n<!--[if lt IE 7 ]><html class="ie6" lang="zh-cn">......

#获取响应头
print(reque.headers)

#requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
print(reque.cookies)

#要在请求中传入Cookie，只需准备一个dict传入cookies参数：
# cs = {'token': '12345', 'status': 'working'}
# r = requests.get(url, cookies=cs)



# 对于带参数的URL，传入一个dict作为params参数：
rs = requests.get(r'https://www.so.com/s',params={'q': 'python', 'cat': '1001'}) #这个参数应该是查询参数
#一个浏览器查询的例子#https://www.so.com/s?ie=utf-8&src=hao_360so_b_cube&shb=1&hsid=e6de436cfb1de30c&q=python+PIL+RESIZE
print(rs.url)  #https://www.so.com/s?q=python&cat=1001


#requests自动检测编码，可以使用encoding属性查看：
print(rs.encoding)   #UTF-8

#无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
# print(reque.content)  #b'<!DOCTYPE html>\n<!--[if lt IE 7 ]><html class="ie6" lang="zh-cn">......

#requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取： 类似这样我也有点模糊
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
#
# print(r.json())

#需要传入HTTP Header时，我们传入一个dict作为headers参数：

# rqs = requests.get(r'https://hao.360.com/',params={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(rqs.text)

'''要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：'''

reqp =  requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

#requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON

# #类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
# upload = {'file':open('report.xls', 'rb')}
# rsf = requests.post(url,files=upload)
#
# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
#
# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。


