# coding: utf-8

# 透過画像をオーバーレイする
import cv2
import numpy as np

img_back  = cv2.imread("./images/img_back.png", cv2.IMREAD_UNCHANGED)
img_front = cv2.imread("./images/img_front.png", cv2.IMREAD_UNCHANGED)
print("img_back:", img_back.shape)
print("img_front:", img_front.shape)

if img_back.shape[2] < 4:
	img_back = cv2.cvtColor(img_back, cv2.COLOR_RGB2RGBA)
if img_front.shape[2] < 4:
	img_front = cv2.cvtColor(img_front, cv2.COLOR_RGB2RGBA)

def overlay_img(back, front):
	back_rgb = back[:, :, :3] # RGB
	back_a   = back[:, :, 3] # Alpha
	front_rgb = front[:, :, :3] # RGB
	front_a   = front[:, :, 3] # Alpha
	mask = 255 - cv2.merge((front_a, front_a, front_a)) # Mask
	cv2.imwrite("./01_mask.png", mask)
	tmp = cv2.bitwise_and(back_rgb, mask) # AND
	cv2.imwrite("./02_and.png", tmp)
	tmp = cv2.bitwise_or(tmp, front_rgb) # OR
	cv2.imwrite("./03_or.png", tmp)
	return tmp

img_dst = overlay_img(img_back, img_front)
cv2.imwrite("./img_dst.png", img_dst)

