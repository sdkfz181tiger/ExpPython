# coding: utf-8

"""
基数変換問題ジェネレーター(16進整数 -> 10進数)
"""

import os, math, random
from PIL import Image, ImageFont, ImageDraw

text_title = "HEX \\(x_x;)/ HELL 100"
text_explain = "次にある16進数の値を、全て10進数に基数変換しなさい"
text_example = "(例)\n\n  A4 = 20"
dir_name = "01"

# Font
font_path_w4 = "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc";
font_path_w6 = "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc";
font_color = (0, 0, 0)

base_x = 250
base_y = 800
pad_x  = 980
pad_y  = 210

rows = 10
cols = 2

seed = 0# 偶数ジャンプする事!!

# Random
rdms = list(range(100))
random.seed(seed)
random.shuffle(rdms)

# Nums
nums = rdms[0:rows*cols]
#nums = list(range(100))
nums.sort()

# Alphabets
alphabets = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

# Int to Hex
def int2hex(num):
	result = ""
	while(0 < num):
		result = alphabets[num%16] + result
		num = int(num / 16)
	return result

for i in range(2):

	type_flg = i % 2
	type_name = "mondai" if type_flg else "kaito"

	images = []

	# Image
	image = Image.new("RGB", (2150, 3035), (255, 255, 255))

	# Draw
	draw = ImageDraw.Draw(image)
	# Title
	font = ImageFont.truetype(font_path_w6, 80)
	draw.text((base_x, 200), text_title, font=font, fill=font_color)
	# Name
	font = ImageFont.truetype(font_path_w6, 40)
	draw.text((image.size[0]/2 + 500, 250), "氏名:", font=font, fill=font_color)
	# Explain
	font = ImageFont.truetype(font_path_w6, 50)
	draw.text((260, 420), text_explain, font=font, fill=font_color)
	# Example
	font = ImageFont.truetype(font_path_w4, 40)
	draw.text((base_x, base_y - pad_y), text_example, font=font, fill=font_color)

	for r in range(rows):
		for c in range(cols):
			i = c + r * cols
			num = nums[i]
			text = "(" + str(i+1) + ")" + "\n\n     " + int2hex(num) + " = "
			if type_flg == 0: text += str(num)
			pos_x = base_x + c * pad_x
			pos_y = base_y + r * pad_y
			pos = (pos_x, pos_y)
			font = ImageFont.truetype(font_path_w6, 40)
			draw.text(pos, text, font=font, fill=font_color)

	# Directory
	if(not os.path.isdir(dir_name)): os.mkdir(dir_name)

	images.append(image)

	# Save
	image_out = "./" + dir_name + "/" + type_name + ".pdf"
	images[0].save(image_out, "PDF", 
		quality=100, save_all=True, append_images=images[1:], optimize=True)