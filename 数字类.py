import math
import random
print(min(1,23,4,56,6))  #最小值
print(max(1,2,3,45,6,))  #最大值
print(pow(2,3))          #2的3次方
print(round(3.456,2))    #四舍五入保留两位
print(abs(-100))         #绝对值
print(math.floor(6.9))   #向下取整
print(math.ceil(18.1))   #向上取整
print(math.modf(10.01))  #返会整数与小数部分
print(math.sqrt(16))     #开方
print(random.choice([1,2,34,5,6,"r","q"])) #从列表随机拿
print(random.choices([1,2,34,5,6,"r","q"]))#随机拿到一个含一个元素的列表
print(random.choice("qwer"))  #["q","w","e","r"]取
print(random.randrange(1,100,2)) #从开始是递增+2 (都是奇数了)
print(random.randrange(0,100,2)) #从开始是递增+2 (都是偶数了) 会取到0
print(random.random())           #取0到1之间的小数数 包含0
print(random.randint(0,100))     #随机数
listp = [1,2,3,4,5,6]
random.shuffle(listp)
print(listp)  #对列表随机排序
print(id(listp))  #查看变量的地址
print(random.uniform(1,4))      #随机生成1到4之间的实数包括1和4的整数和小数


#变量作用域
#局部 全局 内建