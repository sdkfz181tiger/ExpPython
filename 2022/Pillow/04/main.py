# coding: utf-8

"""
画像の読込
"""

import numpy as np
from PIL import Image

# 例1
def sample01():
	# Png
	img = Image.open("./images/img_back.png")# 読込
	img = img.rotate(45)# 回転
	img.save("img_dst.png")# 保存

sample01()

# 例2
def sample02():
	# Jpeg
	img = Image.open("./images/img_back.png")# 読込
	img.save("img_dst.jpg", dpi=(100, 100), quality=5)# 保存
	
sample02()

# 例3
def sample03():
	# Gif
	img = Image.open("./images/img_back.png")# 読込
	imgs = []
	for i in range(30):
		imgs.append(img.rotate(i*12))
	img.save("img_dst.gif", save_all=True, append_images=imgs, duration=30, loop=2)
	
sample03()
