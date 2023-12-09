# coding: utf-8

"""
基数変換問題ジェネレーター(2進数 -> 10進小数)
"""

import os, math, random
from PIL import Image, ImageFont, ImageDraw

text_title = "BINARY \\(x_x;)/ HELL"
text_explain = "次にある2進数の値を、全て10進数に変換しなさい"
text_example = "(例)\n\n  0.01 = 0.25"
dir_name = "01"

# Font
font_path_w4 = "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc";
font_path_w6 = "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc";
font_color = (0, 0, 0)

base_x = 250
base_y = 1000
pad_x  = 980
pad_y  = 360

rows = 5
cols = 2

# Numbers
numerators = list(range(1, 11))
denominators = [2, 4, 8] # Easy
# denominators = [4, 8, 16] # Normal
# denominators = [8, 16, 32] # Hard
#print(numerators, denominators)

# Numbers
nums = set()
for n in numerators:
	for d in denominators:
		num = n / d
		if(math.modf(num)[0] == 0): continue
		if(math.modf(num)[1] != 0): continue
		nums.add(num)
nums = list(nums)
random.shuffle(nums)

# Float to Binary
def float2binary(num):
	result = "0."
	while(num != 0):
		num *= 2
		modf = math.modf(num)
		if(modf[1] == 1):
			result += "1"
		else:
			result += "0"
		num = modf[0]
	return result

for i in range(2):

	type_flg = i % 2
	type_name = "mondai" if type_flg else "kaito"

	images = []

	for o in range(10):
		offset = o * 10
		if(len(nums) <= offset): break

		# Image
		image = Image.new("RGB", (2150, 3035), (255, 255, 255))

		# Draw
		draw = ImageDraw.Draw(image)

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
		font = ImageFont.truetype(font_path_w4, 60)
		draw.text((base_x, base_y - pad_y), text_example, font=font, fill=font_color)
		# Page
		page = "= " + str(o+1) + " ="
		font = ImageFont.truetype(font_path_w6, 40)
		draw.text((image.size[0]/2, image.size[1]-120), page, font=font, fill=font_color, anchor="mm")

		for r in range(rows):
			for c in range(cols):
				i = c + r * cols
				if(len(nums) <= i+offset): continue
				num = nums[i+offset]
				text = "(" + str(i+1) + ")" + "\n\n  " + float2binary(num) + " = "
				if type_flg == 0: text += str(num)
				pos_x = base_x + c * pad_x
				pos_y = base_y + r * pad_y
				pos = (pos_x, pos_y)
				font = ImageFont.truetype(font_path_w4, 60)
				draw.text(pos, text, font=font, fill=font_color)

		# Directory
		if(not os.path.isdir(dir_name)): os.mkdir(dir_name)

		images.append(image)
		
	# Save
	image_out = "./" + dir_name + "/" + type_name + ".pdf"
	images[0].save(image_out, "PDF", 
		quality=100, save_all=True, append_images=images[1:], optimize=True)
	