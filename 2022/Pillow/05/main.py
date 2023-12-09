# coding: utf-8

"""
画像の生成
"""

import numpy as np
from PIL import Image

W = 256
H = 256
SIZE = (W, H)

# 例1
def sample01():

	# Black
	img_black = Image.new("L", SIZE)
	img_black.save("img_black.png")

	# Gray
	img_gray = Image.new("L", SIZE, color=128)
	img_gray.save("img_gray.png")

	# RGB
	img_red = Image.new("RGB", SIZE, color=(255, 0, 0))
	img_red.save("img_red.png")

	img_green = Image.new("RGB", SIZE, color="#00FF00")
	img_green.save("img_green.png")

	img_blue = Image.new("RGB", SIZE, color="blue")
	img_blue.save("img_blue.png")

sample01()

# 例2
def sample02():

	# Bytes
	img_black = Image.frombytes("L", SIZE, bytes([0]*W*H))
	img_black.save("img_bytes_black.png")

	# Gradiation
	img_grad_h = Image.frombytes("L", SIZE, bytes(list(range(W))*H))
	img_grad_h.save("img_bytes_grad_h.png")

	img_grad_v = Image.frombytes("L", SIZE, bytes(list(range(W))*H))
	img_grad_v = img_grad_v.rotate(90)
	img_grad_v.save("img_bytes_grad_v.png")

	# RGB
	img_rgb_red = Image.frombytes("RGB", SIZE, bytes([255, 0, 0]*W*H))
	img_rgb_red.save("img_bytes_rgb_red.png")

	img_rgb_white = Image.frombytes("RGB", SIZE, bytes([255]*W*H*3))
	img_rgb_white.save("img_bytes_rgb_white.png")

	arr_pink = bytearray([255]*W*H*3) # bytesは値を変更できない
	for i in range(1, len(arr_pink), 3):
		arr_pink[i] = 0 # Blueのみ0
	img_rgb_pink = Image.frombytes("RGB", SIZE, bytes(arr_pink))
	img_rgb_pink.save("img_bytes_rgb_pink.png")

	arr_grad = bytearray([255]*W*H*3) # bytesは値を変更できない
	for i in range(1, len(arr_grad), 3):
		arr_grad[i] = (i // 3) % 256 # 0 ~ 255
	img_rgb_grad = Image.frombytes("RGB", SIZE, bytes(arr_grad))
	img_rgb_grad.save("img_bytes_rgb_grad.png")
	
sample02()

# 例3
def sample03():

	# Image -> Bytes
	img_back = Image.open("./images/img_back.png")
	img_gray = img_back.convert("L") # RGB -> L
	img_gray.save("img_mask_gray.png")

	arr_gray = img_gray.tobytes() # Image -> Bytes
	arr_mono = [255 if b > 164 else 0 for b in arr_gray] # Gray -> Mono
	img_mono = Image.frombytes(img_gray.mode, img_gray.size, bytes(arr_mono))
	img_mono.save("img_mask_mono.png")

sample03()