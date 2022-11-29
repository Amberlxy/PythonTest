#!/usr/bin/python
# -*- coding: UTF-8 -*-

# iPhone5分辨率:1136*640

from PIL import Image
import os

filenames = []
new_path = r"./Photos_n/"

def get_files():
    suffix = ['.jpg','.png','.jpeg','.JPG','.PNG','.JPEG']
    for filename in os.listdir(r"./Photos/"):
        if os.path.splitext(filename)[-1] in suffix:
            filenames.append(filename)
        else:
            continue
    return filenames

def mkdir(path):
	folder = os.path.exists(path)
	if not folder:                 
		os.makedirs(path)            
	else:
		return
	
def output_image():
    for i in range(0,len(get_files())):
        img = Image.open(r"./Photos/" + get_files()[i])
        # imgSize = img.size
        width, height = img.size
        # maxSize = max(imgSize)
        # minSize = min(imgSize)
        if width < 640 and height < 1136:
            img_new = img.copy()
        elif height > width:
            img_new = img.resize((int(height / (width / 640)),1136),Image.ANTIALIAS)
        else:
            img_new = img.resize(640,(int(width / (height / 1136))),Image.ANTIALIAS)
        
        mkdir(new_path)
        img_new.save(r'./Photos_n/' + get_files()[i])

if __name__ == '__main__':
    if not os.path.exists(r"./Photos/"):
        print('文件夹不存在')
    else:
        output_image()