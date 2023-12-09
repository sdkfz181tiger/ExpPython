# coding: utf-8

"""
画像の合成
"""

import numpy as np
from PIL import Image, ImageChops

# 例1
def sample01():

	# Image
	img_back = Image.open("./images/img_back.png")
	img_front_black = Image.open("./images/img_front_black.png")
	img_front_alpha = Image.open("./images/img_front_alpha.png")
	print("img_back:", img_back.mode) # RGB
	print("img_front_black:", img_front_black.mode) # RGB
	print("img_front_alpha:", img_front_alpha.mode) # RGBA

	# Add
	img_add = ImageChops.add(img_back, img_front_black, scale=1.0, offset=0)
	img_add.save("img_dst_add.png")

	# Color
	img_gray  = img_back.convert("L") # RGB -> L
	img_gray  = img_gray.convert("RGB") # L -> RGB
	img_gray.save("img_gray.png")

	img_red   = Image.new("RGB", img_gray.size, color="red")
	img_dst_red = ImageChops.add(img_gray, img_red)
	img_dst_red.save("img_dst_red.png")

	img_green = Image.new("RGB", img_gray.size, color="green")
	img_dst_green = ImageChops.add(img_gray, img_green)
	img_dst_green.save("img_dst_green.png")

	img_blue  = Image.new("RGB", img_gray.size, color="blue")
	img_dst_blue = ImageChops.add(img_gray, img_blue)
	img_dst_blue.save("img_dst_blue.png")

sample01()

# 例2
def sample02():

	# Image
	img_back = Image.open("./images/img_back.png")
	img_front_black = Image.open("./images/img_front_black.png")
	img_front_alpha = Image.open("./images/img_front_alpha.png")

	# Blend
	img_blend_1 = ImageChops.blend(img_back, img_front_black, alpha=0.3)
	img_blend_2 = ImageChops.blend(img_back, img_front_black, alpha=0.6)
	img_blend_3 = ImageChops.blend(img_back, img_front_black, alpha=0.9)

	img_blend_1.save("./img_blend_1.png")
	img_blend_2.save("./img_blend_2.png")
	img_blend_3.save("./img_blend_3.png")

sample02()

# 例3
def sample03():

	# Image
	img_back = Image.open("./images/img_back.png")
	img_front_black = Image.open("./images/img_front_black.png")
	img_front_alpha = Image.open("./images/img_front_alpha.png")

	# Diff
	img_diff = ImageChops.difference(img_back, img_front_black)
	img_diff.save("img_diff.png")

	# Sub
	img_sub = ImageChops.subtract(img_back, img_front_black)
	img_sub.save("img_sub.png")

	# Lighter
	img_light = ImageChops.lighter(img_back, img_front_black)
	img_light.save("img_light.png")

	# Multiply
	img_multi = ImageChops.multiply(img_back, img_front_black)
	img_multi.save("img_multi.png")

	# Screen
	img_screen = ImageChops.screen(img_back, img_front_black)
	img_screen.save("img_screen.png")

	# Screen
	img_screen = ImageChops.screen(img_back, img_front_black)
	img_screen.save("img_screen.png")

	# Overlay
	img_overlay = ImageChops.overlay(img_back, img_front_black)
	img_overlay.save("img_overlay.png")

	# Hardlight
	img_h_light = ImageChops.hard_light(img_back, img_front_black)
	img_h_light.save("img_h_light.png")

	# Softlight
	img_s_light = ImageChops.soft_light(img_back, img_front_black)
	img_s_light.save("img_s_light.png")

	# Composite(Alpha)
	img_back_rgba = img_back.convert("RGBA") # RGB -> RGBA
	img_compo = Image.alpha_composite(img_back_rgba, img_front_alpha)
	img_compo.save("img_compo.png")

sample03()

