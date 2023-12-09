# coding: utf-8

"""
Install
	pip install opencv-python
	pip install numpy
"""

import cv2, time, random
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
	return {"video":cap, "w":w, "h":h, "x":0, "y":0}

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

#Capture
cap_main = get_video(file_main)
cX = int(cap_main["w"]/2) # Center
cY = int(cap_main["h"]/2)

# List
cap_subs = []
for n in range(3):
	cap_sub = get_video(file_sub)
	cap_sub["x"] = random.randint(-cX/2, cX/2)
	cap_sub["y"] = random.randint(-cY/2, cY/2)
	cap_subs.append(cap_sub)

while cap_main["video"].isOpened():
	time_sta = time.perf_counter() # Time(start)
	ret_m, frame_m = cap_main["video"].read() # Main

	# Overlay
	if ret_m == True:

		# Sub
		for cap_sub in cap_subs:
			ret_s, frame_s = cap_sub["video"].read() # Sub
			if ret_s == True:
				x = int(cX - cap_sub["w"]/2 + cap_sub["x"]) # Position
				y = int(cY - cap_sub["h"]/2 + cap_sub["y"])
				frame_m = overlay_img(frame_m, frame_s, (x, y)) # Overlay

		# Show
		time_delay = time.perf_counter() - time_sta  # Time(delay)
		time_str = "FPS:{}".format(1.0 / time_delay)
		cv2.putText(frame_m, time_str, (30, 60), f_style, f_scale, f_color)
		cv2.imshow("Video", frame_m)# Show
		# "Q" to Quit
		if cv2.waitKey(25) & 0xFF == ord("q"): break
	else:
		break

# Release
cap_main["video"].release()
cap_sub["video"].release()

cv2.destroyAllWindows()
