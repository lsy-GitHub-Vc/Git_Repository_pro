from django.db import models


#MySQLclient 目前只支持到 Python3.4  详情看 error文档.py

class stu_2(models.Model):   #以上的类名代表了数据库表名，且继承了models.Model
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    private = models.CharField(max_length=2,default='N')  #如果在这里添加一个新列的话 在makerigrations时会要求你设置默认值
    # 要么给所有的行上设置一个一次性的默认值(该列是空的) 要么退出来单独在该列上添加一个默认值
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)    #Tag 以 Contact 为外部键。 外键会降低效率的  用它干啥
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

'''
在命令行中运行:

$ python3 manage.py makemigrations 应用名  # 让 Django 知道我们在我们的模型有一些变更
    相当于扫描models看有哪些模型需要添加
$ python3 manage.py migrate 应用名   # 创建表结构


表名组成结构为：应用名_类名（如：Endeavor_stu_2）
'''


'''
contact = models.ForeignKey(Contact,on_delete=models.CASCADE)  关联外键
    CASCADE：此值设置，是级联删除。
    PROTECT：此值设置，是会报完整性错误。
    SET_NULL：此值设置，会把外键设置为 null，前提是允许为 null。
    SET_DEFAULT：此值设置，会把设置为外键的默认值。
    SET()：此值设置，会调用外面的值，可以是一个函数。一般情况下使用 CASCADE 就可以了
'''