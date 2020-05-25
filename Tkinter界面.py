import tkinter


def fund():
    print("按钮测试")

def showInfo():
    #获取输入框的值
    print(e.get())

def update():
    #判断选中的标签
    messge = ""
    if hobby1.get() == True:
        messge+="姓名\n"
    if hobby2.get() == True:
        messge+="电话\n"
    if hobby3.get() == True:
        messge+="身份证号\n"

    #清空上次执行的数据
    text1.delete(0.0,tkinter.END)
    text1.insert(tkinter.INSERT,messge)

def update1():
    #获取单选框的value
    print(r.get())

def listFrame(event):
    #获取列表框中选定的值
    print(lb.get(lb.curselection()))

def scaleNum():
    #Scale 取值
    print(sca.get())
    #SpinBox
    print(va.get())

def showMenu(event):
    #Menu鼠标右键菜单 鼠标事件位置坐标
    menubar1.post(event.x_root,event.y_root)

def tpMenu(event):
    print("*********")

#创建主窗口
win = tkinter.Tk()
#标题
win.title("标题")
#大小
#win.geometry("400x400+200+20")
#进入消息循环(放控件)
'''
Label；标签控件可以显示文本
主窗口对象  text:文字，bg:背景色， fg:字体颜色， font:字体规格， width:宽， height:高， wraplength:设置该长度后换行
justify:换行后的对齐方式，anchor:文字位置 参数 n上 e右 s下 w左 ne右上 等等  center居中(默认的)
'''
label = tkinter.Label(win,text="测试窗口",bg="pink",fg="red",font=("黑体",15),width=10,height=4,wraplength=100,
                      justify="left",anchor="center")

label.pack()
'''
Button 按钮
'''
button1 = tkinter.Button(win,text="按钮",command=fund,width=5, height=1)
button2 = tkinter.Button(win,text="关闭",command=win.quit,width=5, height=1,bg="red")
button3 = tkinter.Button(win,text="测试输入框输出",command=showInfo,width=15, height=1)
button4 = tkinter.Button(win,text="测试Scale取值和SpinBox取值",command=scaleNum,width=25,bg="yellow")
'''
Entry 输入控件
用于显示简单的文本内容
show:密文显示,textvariable:可用于接受外围变量
'''
#创建输入框的接受对象 可用于接受数据和设置默认值
e = tkinter.Variable()

entry = tkinter.Entry(win,textvariable=e)
#设置默认值
e.set("默认值测试")
#获取输入的值
e.get()

'''
Text 文本控件  用于显示多行文本
height:显示的行数
'''
str='''
你肯定有许多自己独有的宝贝，肯定在某些方面你能干得出色，任何人都没有理由妄自菲薄！
当然，我不是鼓励你为了哗众取宠而身着奇装异服，为了标新立异而举止反常；
不是说别人大乐你皱眉、别人上课你睡觉、别人说逗死了你说“真可笑”是与众不同。
我所说的与众不同盆含一种向上的力量，它是与高尚的价值取向相应相和的出类拔萃。认识到自己与众不同，
这仅仅是一个前提和基础，我们借此达到一种牢靠的平衡，接下来要做的是热情十足地挖掘潜能，坚韧不拔地优化劣势，
以持之以恒的积累期待石破天惊的萌发，在适合你的那一方面迎接脱颖而出的时刻，完成一份接近完满的人生！
你肯定有许多自己独有的宝贝，肯定在某些方面你能干得出色，任何人都没有理由妄自菲薄！
当然，我不是鼓励你为了哗众取宠而身着奇装异服，为了标新立异而举止反常；
不是说别人大乐你皱眉、别人上课你睡觉、别人说逗死了你说“真可笑”是与众不同。
我所说的与众不同盆含一种向上的力量，它是与高尚的价值取向相应相和的出类拔萃。认识到自己与众不同，
这仅仅是一个前提和基础，我们借此达到一种牢靠的平衡，接下来要做的是热情十足地挖掘潜能，坚韧不拔地优化劣势，
以持之以恒的积累期待石破天惊的萌发，在适合你的那一方面迎接脱颖而出的时刻，完成一份接近完满的人生！
'''
text = tkinter.Text(win,width=30,height=5)

#创建滚动条
scroll = tkinter.Scrollbar()

#插入一个多行文本
text.insert(tkinter.INSERT,str)

#side:放到窗体的哪一侧  fill填充
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.RIGHT,fill=tkinter.Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

'''
CheckButton  多选框控件
'''
#创建变量用于判断
hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()

check1 = tkinter.Checkbutton(win,text="姓名",variable=hobby1,command=update)
check1.pack()
check2 = tkinter.Checkbutton(win,text="电话",variable=hobby2,command=update)
check2.pack()
check3 = tkinter.Checkbutton(win,text="身份证号",variable=hobby3,command=update)
check3.pack()

#创建文本用于记录选定的值
text1 = tkinter.Text(win,width=10,height=5)
text1.pack()

'''
Radiobutton 单选框
'''
r = tkinter.IntVar()
radio = tkinter.Radiobutton(win,text="是",value=1,variable=r,command=update1)
radio.pack()
radio1 = tkinter.Radiobutton(win,text="否",value=2,variable=r,command=update1)
radio1.pack()

'''
Listbox 列表框控件  包含一个或者多个文本框
作用：在Listbox控件的小窗口显示一个字符串
'''
#selectmode 表示文本框样式
#tkinter.BROWSE,tkinter.SINGLE(鼠标选中后不可以滑动选中)，tkinter.EXTENDED(支持shift和ctrl),tkinter.MULTIPLE(支持多选)
lvb = tkinter.StringVar()
lb = tkinter.Listbox(win,selectmode=tkinter.BROWSE,listvariable=lvb)
#lb1 = tkinter.Listbox(win,selectmode=tkinter.SINGLE)
#lb2 = tkinter.Listbox(win,selectmode=tkinter.EXTENDED)
#lb3 = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
#lb.pack()
#lb1.pack()
#lb2.pack()
#lb3.pack()
for item in ["a","b","c","d","e","f"]*3:
    #按顺序添加
    lb.insert(tkinter.END,item)
    #lb1.insert(tkinter.END,item)
    #lb2.insert(tkinter.END,item)
    #lb3.insert(tkinter.END,item)

#在开始处添加
lb.insert(tkinter.ACTIVE,"p")

#参数为下标 一个参数删除点或两个参数删除段
#lb.delete(1)

#选中 一个参数选中点或两个参数选中段
#lb.select_set(1,3)
#取消选中 一个参数取消选中点或两个参数取消选中段
#lb.select_clear(2,4)

#个数
print(lb.size())
#拿值 参数要写点或段
print(lb.get(1))
#改变框中的值
#lvb.set(("3","2","1"))
#输出选中的下标
#print(lb.curselection())
#判断是否选中
print(lb.select_includes(1))

#绑定事件  双击 按钮 右键
lb.bind("<Double-Button-1>",listFrame)

#创建滚动条
scl = tkinter.Scrollbar(win)
'''
scl.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=scl.set)
lb.pack(side=tkinter.RIGHT,fill=tkinter.BOTH)
scl["command"]=lb.yview
'''
scl.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.pack(side=tkinter.RIGHT,fill=tkinter.Y)
scl.config(command=lb.yview)
lb.config(yscrollcommand=scl.set)

'''
Scale  供用户拖拽指示器改变变量的值
orient=tkinter.VERTICAL 竖直
orient=tkinter.HORIZONTAL 水平
tickinterval = 数字标识
length = 水平长度或者说竖直高度
'''
sca = tkinter.Scale(win,from_=0,to=100,orient=tkinter.VERTICAL,length=200,tickinterval=10)
sca.pack()
button4.pack()

#设置默认值
sca.set(20)

'''
SpinBox 数值范围控件
increment:步长
'''
va = tkinter.StringVar()
#这里面还有一个values=()的参数 它会从元组里拿数据展示 当用values时from_=0,to=100,increment=2 这几个参数就不用了
spi = tkinter.Spinbox(win,from_=0,to=100,increment=2,textvariable=va)
spi.pack()
#默认值
va.set(30)
#取值
#va.get()

'''
Menu 顶级菜单
'''
#创建一个菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

#创建一个菜单选项
menu1 = tkinter.Menu(menubar,tearoff=False)
menu2 = tkinter.Menu(menubar,tearoff=False)
menubar.add_cascade(label="语言",menu=menu1)
menubar.add_cascade(label="字体",menu=menu2)
#给菜单选项添加内容
for item1 in ["Python","C","C++","C#","Java","JS","汇编"]:
    #加个分割线
    menu1.add_separator()
    menu1.add_command(label=item1)

menu2.add_command(label="宋体")
menu2.add_command(label="楷书")
menu2.add_command(label="行书")

#Menu鼠标右键菜单
menubar1 = tkinter.Menu(win)

menu3 = tkinter.Menu(menubar1,tearoff=False)
menubar1.add_cascade(label="查看",menu=menu3)
menubar1.add_cascade(label="个性化",menu=menu3)
menubar1.add_cascade(label="刷新",menu=menu3)

menu3.add_command(label="看啥看")
menu3.add_command(label="没看啥")
menu3.add_command(label="请关掉")

win.bind("<Button-3>",showMenu)

#挂载到视图
entry.pack()
button3.pack()
button1.pack()
button2.pack()
win.mainloop()