import urllib.request,urllib.parse
import ssl
import json
#向指定url发送请求  返回服务器响应数据(文件对象) timeout超时时间
pathw = "http://www.baidu.com"
response = urllib.request.urlopen(pathw,timeout=0.5)

#data = response.read() #返回对象字符串
#data = response.readlines()  #返回对象列表 推荐
path = r"E:\PyCharm\project_1\测试文件\biadu.html"

#with open(path,"wb") as fil:
#    fil.write(data)
#print(data)

#info() 返回相关信息
print(response.info())

#返回状态码
print(response.getcode())

#返回当前正在爬取的url地址
print(response.geturl())

#url中的中文解码
urlstr = "https://www.so.com/s?q=%E4%BC%98%E9%85%B7&src=srp&fr=hao_360so_suggest_history_b&psid=25ed510895023950ab32541651c941f6&eci=b230aecd93f53a9a&nlpv=suggest_3.2.2"

newurl1 = urllib.request.unquote(urlstr)
print(newurl1)
print("***************************")
#url中文编码
newurl2 = urllib.request.quote(newurl1)
print(newurl2)



'''
网页直接写入文件
urlretrieve 会产生一些缓存
'''
urllib.request.urlretrieve("http://www.baidu.com",filename=r"E:\PyCharm\project_1\测试文件\biadu2.htm1")

#清缓存
urllib.request.urlcleanup()


'''
伪装成浏览器
'''

#模拟报文头部的User-Agent(浏览器版本信息# )

head = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

#设置一个请求体
#req = urllib.request.Request(pathw,headers=head)

#请求
#response_1 = urllib.request.urlopen(req)
#print(response_1.read().decode("utf-8"))


'''
用随机的user-agent访问
'''




'''
HTTP 请求
使用场景：进行客户端和服务器之间的通讯
GET:通过url网址传递信息，可以在url网址上添加传递的信息
POST:可以向服务器提交数据 比较安全
PUT:请求服务器存储数据
DELETE:请求服务器删除数据
HEAD:获取HTTP报文头
OPTIONS:获取当前URL所支持的请求类型
'''

'''
JSON
GET
'''
#json格式转字典
jsonstr = '{"name":"lsy","age":["20","21","22"]}'

jsonData = json.loads(jsonstr)
print(jsonData)
print(type(jsonData))

#字典转json
jsonData_1 = json.dumps(jsonData)
print(jsonData_1)
print(type(jsonData_1))



'''
读本地josn文件
'''
path2 = r"E:\PyCharm\project_1\测试文件\ceshi.json"
path3 = r"E:\PyCharm\project_1\测试文件\ceshi_1.json"

with open(path2,"rb") as file1:
    print(json.load(file1))

#写json文件
dict1 = {"a":"b","c":"d"}

with open(path3,"w") as file2:
    json.dump(dict1,file2)

'''
POST
'''
url = r"https://mail.163.com/js6/main.jsp"

#登陆的账户 密码 键为输入框name
data = {
    "email":"ksdhsk",
    "password":"sdsds"
}

#给数据打包
postback = urllib.parse.urlencode(data).encode("utf-8")

#请求体
req = urllib.request.Request(url,postback)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")


response_2 = urllib.request.urlopen(req)

print(response_2.read().decode("utf-8"))


'''
ajax 动态抓取 (这个实际运用中牵扯到  分布式)
'''

#在打开请求的地址是加入该参数 可以不去验证安全上下文 用于抓取Https网址  动态抓取时写个方法循环 url动态改下stat起始位置就行了
#context = ssl._create_unverified_context()
#response_2 = urllib.request.urlopen(req,context=context)