# coding: utf-8

"""
Install
	pip install opencv-python
	pip install numpy
"""

import cv2
import numpy as np

# Capture
file_main = "../assets/sample01.mp4"
cap_main = cv2.VideoCapture(file_main)
if cap_main.isOpened() == False:
	print("Cant't open:", file_main)

W     = int(cap_main.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
H     = int(cap_main.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
COUNT = int(cap_main.get(cv2.CAP_PROP_FRAME_COUNT))# Count
FPS   = int(cap_main.get(cv2.CAP_PROP_FPS))# Fps
print("Video W:%d H:%d COUNT:%d FPS:%d" % (W, H, COUNT, FPS))

# Img
file_green = "../assets/img_green.png"
img_green = cv2.imread(file_green)
if img_green is None:
	print("Cant't open:", file_green)

# Center
gH = img_green.shape[0]
gW = img_green.shape[1]
center = int(W/2-gW/2), int(H/2-gH/2)

# Mask
bgr_lower = np.array([0, 250, 0])   # Lower
bgr_upper = np.array([10, 255, 10]) # Upper

# Overlay
def overlay_img(img_back, img_front, pos):
	# Position
	x, y = pos
	bH, bW = img_back.shape[:2]
	fH, fW = img_front.shape[:2]
	# Rect, ROI
	x1, y1 = max(0, x), max(0, y)
	x2, y2 = min(bW, x+fW), min(bH, y+fH)
	back_roi = img_back[y1:y2, x1:x2]
	front_roi = img_front[y1-y:y2-y, x1-x:x2-x]
	# Mask
	img_mask_1  = cv2.inRange(front_roi, bgr_lower, bgr_upper)
	img_mask_2  = 255 - img_mask_1 # Reverse
	# AND
	img_and_1 = cv2.bitwise_and(back_roi, back_roi, mask=img_mask_1)
	img_and_2 = cv2.bitwise_and(front_roi, front_roi, mask=img_mask_2)
	# OR
	img_or = cv2.bitwise_or(img_and_1, img_and_2)
	# Override
	img_back[y1:y2, x1:x2] = img_or
	return img_back

while cap_main.isOpened():
	# Main
	ret_m, frame_m = cap_main.read()

	if ret_m == True:
		# Overlay
		img_dst = overlay_img(frame_m, img_green, center)
		# Show
		cv2.imshow("Video", img_dst)
		# "Q" to Quit
		if cv2.waitKey(25) & 0xFF == ord("q"):
			break
	else:
		break

# Release
cap_main.release()

cv2.destroyAllWindows()
