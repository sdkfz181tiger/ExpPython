# coding: utf-8

"""
Install
	pip install opencv-python
	pip install numpy
"""

import cv2, time
import numpy as np

# File
file_main = "../assets/sample01.mp4"
file_sub  = "../assets/sample02.mp4"

# Mask
bgr_lower = np.array([0, 230, 0])   # Lower
bgr_upper = np.array([80, 255, 80]) # Upper

# Font
f_style = cv2.FONT_HERSHEY_DUPLEX
f_scale = 1
f_color = (255, 255, 255)

# Video
def get_video(path):
	cap = cv2.VideoCapture(path)
	if cap.isOpened() == False:
		print("Cant't open:", path)
		return None
	w     = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
	h     = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
	count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))# Count
	fps   = int(cap.get(cv2.CAP_PROP_FPS))# Fps
	print("Video W:%d H:%d COUNT:%d FPS:%d" % (w, h, count, fps))
	return cap, w, h, count, fps

#Capture
cap_main, M_W, M_H, M_COUNT, M_FPS = get_video(file_main)
cap_sub, S_W, S_H, S_COUNT, S_FPS  = get_video(file_sub)

# Center
center = int(M_W/2 - S_W/2), int(M_H/2 - S_H/2)

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
	img_mask_1 = cv2.inRange(front_roi, bgr_lower, bgr_upper)
	img_mask_2 = 255 - img_mask_1 # Reverse
	# AND
	img_and_1 = cv2.bitwise_and(back_roi, back_roi, mask=img_mask_1)
	img_and_2 = cv2.bitwise_and(front_roi, front_roi, mask=img_mask_2)
	# OR
	img_or = cv2.bitwise_or(img_and_1, img_and_2)
	# Override
	img_back[y1:y2, x1:x2] = img_or
	return img_back

while cap_main.isOpened():
	
	time_sta = time.perf_counter()   # Time(start)
	ret_m, frame_m = cap_main.read() # Main
	ret_s, frame_s = cap_sub.read()  # Sub

	if ret_m == True and ret_s == True:
		
		img_dst = overlay_img(frame_m, frame_s, center)# Overlay
		time_delay = time.perf_counter() - time_sta # Time(delay)
		time_str = "FPS:{}".format(1.0 / time_delay)
		cv2.putText(img_dst, time_str, (30, 60), f_style, f_scale, f_color)
		cv2.imshow("Video", img_dst)# Show

		# "Q" to Quit
		if cv2.waitKey(25) & 0xFF == ord("q"): break
	else:
		break

# Release
cap_main.release()
cap_sub.release()

cv2.destroyAllWindows()
