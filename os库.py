import os
#os包含了普遍的操作系统功能
import shutil
#这个算是os功能的补充模块
print(shutil.copyfile(src="",dst=""))  #复制文件 两个路径吧  从哪儿到哪儿  我现在就知道这一个


#获取操作系统类型   nt-->Windows  posix--> Linux Unix 或 Mac OS X
print(os.name)

#获取系统的详细信息  Windows操作系统不支持该方法
#print(os.uname())

#获取操作系统的所有环境变量
print(os.environ)

#获取指定的环境变量
print(os.environ.get("APPDATA"))

#获取当前目录
print(os.curdir)

#获取当前的工作目录，即当前python脚本所在的目录
print(os.getcwd())

#返回指定目录下的所有文件
print(os.listdir("E:\PyCharm\project_1"))

#创建新目录 可以填绝对路径
#os.mkdir("text")

#删除目录 可以填绝对路径
#os.rmdir("text")

#获取文件属性 可以填绝对路径
print(os.stat("text1"))

#重命名
#os.rename("text","text1")

#删除文件
#os.remove()

#运行shell命令  write:写字板  mspaint:画板  msconfig:系统配置  notepad:记事本
#os.system("notepad")
os.system("taskkill /f /im notepad.exe") #关闭运行的程序

#查看当前的绝对路径
print(os.path.abspath("."))

#拼接路径
#print(os.path.join("E:\PyCharm\project_1\测试文件","wh.txt"))

#拆分路径
print(os.path.split("E:\PyCharm\project_1\测试文件\wh.txt"))

#获取扩展名
print(os.path.splitext("E:\PyCharm\project_1\测试文件\wh.txt"))

#获取文件的目录
print(os.path.dirname("E:\PyCharm\project_1\测试文件\wh.txt"))

#获取文件名
print(os.path.basename("E:\PyCharm\project_1\测试文件\wh.txt"))

#判断是否为目录
print(os.path.isdir("E:\PyCharm\project_1\测试文件"))

#判断文件是否存在
print(os.path.isfile("E:\PyCharm\project_1\测试文件\wh.txt"))

#判断目录是否存在
print(os.path.exists("E:\PyCharm\project_1\测试文件"))

#文件大小 字节
print(os.path.getsize("E:\PyCharm\project_1\测试文件\wh.txt"))

