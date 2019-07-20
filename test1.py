# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:36:28 2019

@author: 0obriano0
"""

from PIL import Image, ImageDraw, ImageFont

img = Image.open('./GTA5.jpg')
gray_level = img.convert('L')
gray_level.save('./GTA5_Gray_level_demo.jpg')

new_gray_level = Image.new("L", img.size, "#ffffff")

for loopnum1 in range(img.size[0]):
    for loopnum2 in range(img.size[1]):
        img_color = img.getpixel((loopnum1,loopnum2))
        gray = round(img_color[0]*0.299 + img_color[1]*0.587 + img_color[2]*0.114)
        new_gray_level.putpixel((loopnum1,loopnum2),gray)
        
new_gray_level.save('./GTA5_Gray_level_test.jpg')

def remove_(file,data):
    test_gray_level = new_gray_level.copy()
    for loopnum1 in range(img.size[0]):
        for loopnum2 in range(img.size[1]):
            gray = new_gray_level.getpixel((loopnum1,loopnum2))
            gray = gray & data
            test_gray_level.putpixel((loopnum1,loopnum2),gray)
            
    test_gray_level.save(file)
    
remove_('./GTA5_Gray_level_remove_0b11111110.jpg',0b11111110)