# coding: utf-8

import cv2
import numpy as np

# クロマキー対象の画像
img_back  = cv2.imread("./images/img_back.png")
img_front = cv2.imread("./images/img_green.png")

# クロマキー対象の色(Lower -> Upper)
bgr_lower = np.array([0, 250, 0])   # Lower
bgr_upper = np.array([10, 255, 10]) # Upper

# 画像を重ねて表示
def overlay_img(back, front, lower, upper, pos):

	# Position
	x, y = pos
	bH, bW = back.shape[:2]
	fH, fW = front.shape[:2]
	#print("back:", bH, bW)
	#print("front:", fH, fW)

	# Rect, ROI
	x1, y1 = max(0, x), max(0, y)
	x2, y2 = min(bW, x+fW), min(bH, y+fH)
	back_roi = back[y1:y2, x1:x2]
	front_roi = front[y1-y:y2-y, x1-x:x2-x]

	# Mask
	img_mask_1  = cv2.inRange(front_roi, lower, upper)
	img_mask_2  = 255 - img_mask_1 # Reverse
	#cv2.imwrite("./img_mask_1.png", img_mask_1)
	#cv2.imwrite("./img_mask_2.png", img_mask_2)

	# AND
	img_and_1 = cv2.bitwise_and(back_roi, back_roi, mask=img_mask_1)
	img_and_2 = cv2.bitwise_and(front_roi, front_roi, mask=img_mask_2)
	#cv2.imwrite("./img_and_1.png", img_and_1)
	#cv2.imwrite("./img_and_2.png", img_and_2)

	# OR
	img_or = cv2.bitwise_or(img_and_1, img_and_2)
	#cv2.imwrite("./img_or.png", img_or)

	# Override
	back[y1:y2, x1:x2] = img_or
	return back

img_dst = overlay_img(img_back, img_front, bgr_lower, bgr_upper, (0, 0))
cv2.imwrite("./img_dst.png", img_dst)