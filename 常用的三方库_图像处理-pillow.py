#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author:lsy

from PIL import Image,ImageFile

'''PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。

由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow'''


'''
操作图像
来看看最常见的图像缩放操作，只需三四行代码：
'''

#获取图片对象
Img = Image.open(r'E:\PyCharm\project\16pic_1987421_b.jpg','r')

#获取图像尺寸
# w,h = Img.size
# print('Original image size: %sx%s' % (w, h))

print(Img.format)
print(Img.mode)

#缩放50%
# g = Image.resize((w//2, h//2),Img.ANTIALIAS)
# print('Resize image to: %sx%s' % (w//2, h//2))
# g.save()

#模糊
# im2 = Img.filter(ImageFile.BLUR)
# im2.save('blur.jpg', 'jpeg')


from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype(r'E:\PyCharm\project\测试文件\arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')