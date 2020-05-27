import time
import os

words = "Love"
for item in words.split():
    print("\n".join(["".join([(item[(x-y) % len(item)] if ((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else " ") for x in range(-30,30)]) for y in range(12,-12,-1)]))
    time.sleep(1.5);


#判断数字
num = input("输入一个不为0的正整数:")

if num.isdigit() == False:
    print("请输入正确的数字")
    os._exit(0)

num = int(num)
if num ==0:

    print("不能为0")
else:
    list6=[]
    i = 2
    if num % i == 0 :
        num /= i
        list6.append(i)
        if num == 1 :
            list6.append(1)
            print("该数字为偶数也是个质数约数为"+str(list6)+"组成的")
        else:
            while num != 1:
                if num % i == 0:
                    list6.append(i)
                    num /= i
                else:
                    i+=1
            print("该数字为偶数 约数为"+str(list6)+"组成的")
    else:
        if num == 1 :
            print("最小的奇数1")
        else:
            j = 3
            while num != 1:
                if num % j == 0:
                    list6.append(j)
                    num /= j
                else:
                    j+=2
            if len(list6) == 1:
                print("该数是一个奇数一同时是一个质数")
            else:
                print("该数是一个奇数由约数"+str(list6)+"组成")