# coding: utf-8

"""
Install
	pip install opencv-python
	pip install opencv-python-rolling
"""

import cv2
import numpy as np

# トラックバーのテスト

# コールバック
def do_nothing(x):
	pass

# ウィンドウ
cv2.namedWindow("Image")

# イメージ
img = np.zeros((320, 480, 3), np.uint8)

# トラックバー(トグル)
cv2.createTrackbar("Toggle", "Image", 0, 1, do_nothing)

# トラックバー(BGR)
cv2.createTrackbar("Blue", "Image", 0, 255, do_nothing)
cv2.createTrackbar("Green", "Image", 0, 255, do_nothing)
cv2.createTrackbar("Red", "Image", 0, 255, do_nothing)

# トラックバー(HSV)
cv2.createTrackbar("Hue", "Image", 0, 179, do_nothing)
cv2.createTrackbar("Saturation", "Image", 0, 255, do_nothing)
cv2.createTrackbar("Value", "Image", 0, 255, do_nothing)

# メイン処理
while True:
	toggle = cv2.getTrackbarPos("Toggle", "Image")

	if toggle == 0:
		# 0の時はBGR
		b = cv2.getTrackbarPos("Blue", "Image")
		g = cv2.getTrackbarPos("Green", "Image")
		r = cv2.getTrackbarPos("Red", "Image")
		img[:] = [b, g, r] # 画像に適用

	else:
		# 1の時はHSV
		h = cv2.getTrackbarPos("Hue", "Image")
		s = cv2.getTrackbarPos("Saturation", "Image")
		v = cv2.getTrackbarPos("Value", "Image")
		img[:] = [h, s, v] # 画像に適用
		img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

	# Key
	k = cv2.waitKey(1) & 0xFF
	if k == ord("q"):
		# Q
		break

	# Show
	cv2.imshow("Image", img)

cv2.destroyAllWindows()