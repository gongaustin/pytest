import itchat
import os
from os import listdir
import math
from PIL import Image

itchat.auto_login()
friends = itchat.get_friends(update=True)
user = friends[0]["NickName"]
print(user)

# 建立文件夹来装好友的头像----- mkdir()方法用来创建文件夹（目录）
os.mkdir(user)

# 将头像存到一个文件夹下
number = 0
for friend in friends:
    img = itchat.get_head_img(userName=friend["UserName"])
    fileImage = open(user + "/" + str(number) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    number += 1

# listdir()方法用于返回指定文件夹下包含的文件或文件夹的名字的列表，在此处就是：每一张图片的名字
pics = listdir(user)
# 获取照片的张数
numberPics = len(pics)
# 设置每张照片的大小
eachsize = int(math.sqrt(float(1080*1080)/numberPics))
# 获取每一行放置多少张图片
numbline = int(1080/eachsize)
# 设置图片的大小为 640*640
toImage = PIL.Image.new("RGBA",(1080,1080))

x = 0
y = 0
# pic 为每一张图片
for pic in pics:
    try:
        # 打开图片
        img = PIL.Image.open(user + "/" + pic)
    except IOError:
        print("Error : 没有找到文件或读取文件失败")
    else:
        # 缩小图片 && ANTIALIAS（抗锯齿）
        img = img.resize((eachsize,eachsize),PIL.Image.ANTIALIAS)
        #拼接图片 paste()方法，粘贴图片，在拼接图片时将图片一张张粘贴上去
        toImage.paste(img, (x * eachsize,y * eachsize))
        x += 1
        if x == numbline:
            x = 0
            y += 1

# 保存拼接后的抬头像
toImage.save(user + ".BMP")
# 将拼接好的图片发送给文件传输助手
itchat.send_image(user + ".BMP" , 'filehelper')