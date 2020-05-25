# 邮箱库
import smtplib
#邮件文本
from email.mime.text import MIMEText

from time import sleep


#邮件服务器对象
SmtpServer = "smtp.qq.com"

#发送邮件地址(即我方账户)
Sender = "975763893@qq.com"

#授权密码  cennabebusycbedb
Password = "cennabebusycbedb"


#设置发送内容
Messge = "这是个测试邮件"

#转换为邮件文本
msg = MIMEText(Messge)

#设置标题
msg["Subject"] = "问候测试"

#发送者
msg["From"] = Sender


#创建连接对象
MailServer = smtplib.SMTP()
MailServer.connect(SmtpServer,25)

#登陆邮箱
print(Sender,Password)
MailServer.login(Sender,Password)


#发送
for i in range(10):
    print("第"+str(i+1)+"封发送")
    MailServer.sendmail(Sender,["suliushy@163.com"],msg.as_string())
    sleep(2)
#退出
MailServer.quit()


