# coding: utf-8

"""
画像のマスク
"""

import numpy as np
from PIL import Image

# 例1
def sample01():

	# Image
	img_back = Image.open("./images/img_back.png")
	img_front = Image.open("./images/img_front_black.png")
	# Crop
	img_bbox = img_front.getbbox()
	img_crop = img_front.crop(img_bbox)
	img_gray = img_crop.convert("L") # RGB -> L
	arr_gray = img_gray.tobytes() # Image -> Bytes
	arr_mono = [255 if b > 30 else 0 for b in arr_gray] # Gray -> Mono
	img_mono = Image.frombytes(img_gray.mode, img_gray.size, bytes(arr_mono))
	img_mono.save("img_crop_mono.png")
	# Paste(L画像を使う場合)
	img_back.paste(img_crop, box=(0, 0), mask=img_mono)
	img_back.save("img_crop_black_dst.png")

sample01()

# 例2
def sample02():

	# Image
	img_back = Image.open("./images/img_back.png")
	img_front = Image.open("./images/img_front_alpha.png")
	# Crop
	img_bbox = img_front.getbbox()
	img_crop = img_front.crop(img_bbox)
	img_crop.save("img_crop_crop.png")
	# Paste(RGBA画像を使う場合)
	img_back.paste(img_crop, box=(0, 0), mask=img_crop)
	img_back.save("img_crop_alpha_dst.png")

sample02()

# 例3
def sample03():

	# Image
	img_back = Image.open("./images/img_back.png")
	img_front = Image.open("./images/img_front_alpha.png")
	# Composite
	img_dst = Image.composite(img_back, img_front, mask=img_front)
	img_dst.save("img_composite_dst.png")

sample03()







