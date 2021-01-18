#!/usr/bin/python3

import requests
from PIL import Image,ImageDraw,ImageFont

def get_avatar_file():
    num = str(input("请输入QQ号："))
    url = "http://q1.qlogo.cn/g?b=qq&nk=" + num + "&s=640"
    folder_path = "/Users/amber/Downloads/"
    html = requests.get(url)   # get函数获取图片链接地址，requests发送访问请求
    imageFile = folder_path + num +'.png'
    with open(imageFile, 'wb') as file:  # 'wb':以二进制文本形式将图片数据写入
        file.write(html.content)
        file.flush()     # 刷新缓冲区
    file.close()
    return imageFile
    # image = Image.open(imageFile)
    # image.show()
    # print(imageFile)

def avatar_badge():
    imageFile = get_avatar_file()
    im = Image.open(imageFile)  ##文件存在的路径
    draw = ImageDraw.Draw(im)
    width, height = im.size
    font = ImageFont.truetype('/System/Library/Fonts/Symbol.ttf', 100)

    draw.text((width - 100, 50), '1', font=font , fill = (255, 0, 0))
    im = im.resize((int(width*0.5), int(height*0.5)))
    
    im.save("/Users/amber/Downloads/Avatar_new.PNG")     ## 将"Avatar.PNG"保存为"Avatar_new.PNG"
    im.show()

if __name__ == '__main__':
    avatar_badge()
