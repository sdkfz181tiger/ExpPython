# coding: utf-8

import cv2, datetime, json, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

JSON_PATH = "./out/result.json"

with open(JSON_PATH) as j:
	jsonObj = json.load(j)

data = jsonObj["data"]
for n in range(len(data)):
	frame = data[n]["frame"]
	x = int(data[n]["x"])
	y = int(data[n]["y"])
	print("%s, %d, %d" % (frame, x, y))



"""
MOVIE = "../assets/movies/sample01.mp4"

# Movie
cap_from = cv2.VideoCapture(MOVIE)# Movie
W     = int(cap_from.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
H     = int(cap_from.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
COUNT = int(cap_from.get(cv2.CAP_PROP_FRAME_COUNT))# Count
FPS   = int(cap_from.get(cv2.CAP_PROP_FPS))# Fps
print("Video W:%d H:%d COUNT:%d FPS:%d" % (W, H, COUNT, FPS))

fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
cap_to = cv2.VideoWriter("result.mp4", fourcc, FPS, (W, H))

for n in range(COUNT):
	ret, frame = cap_from.read()# Read
	if ret==False: break
	cap_to.write(frame)

cap_from.release()
cap_to.release()
"""

"""
def captureFrame(dir, name, ext=".png", off=16):

	if not cap.isOpened(): return
	os.makedirs(dir, exist_ok=True)# Directory
	path = os.path.join(dir, name)
	digit = len(str(int(COUNT)))
	print("saveFrame %s" % path)

	for n in range(COUNT):
		ret, frame = cap.read()# Read
		if ret==False: return
		if n%off!=0: continue
		writeFrame(n, "{}_{}.{}".format(path, str(n).zfill(digit), ext), frame)

def writeFrame(n, path, frame):

	bgr_lower  = np.array([0, 0, 180])
	bgr_upper  = np.array([50, 50, 255])
	img_mask   = cv2.inRange(frame, bgr_lower, bgr_upper)
	img_target = cv2.bitwise_and(frame, frame, mask=img_mask)
	img_gray   = cv2.cvtColor(img_target, cv2.COLOR_BGR2GRAY)

	_, threshold = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY)
	contours, _  = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	l_color = (255, 255, 255)
	l_width = 1
	f_style = cv2.FONT_HERSHEY_DUPLEX
	f_scale = 1
	f_color = (255, 255, 255)

	for cnt in contours:
		(x, y), radius = cv2.minEnclosingCircle(cnt)
		center = (int(x), int(y))
		if radius > 20:
			approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
			cv2.drawContours(img_gray, [approx], 0, l_color, l_width)
			cv2.putText(img_gray, "circle", center, f_style, f_scale, f_color)
			json_obj["data"].append({"frame": n, "x": int(x), "y": int(y)})# Append

	cv2.imwrite(path, img_gray)# Image

def dumpJson(dir, name, ext=".json"):
	os.makedirs(dir, exist_ok=True)# Directory
	path = os.path.join(dir, name+ext)
	with open(path, "w") as file:
		json.dump(json_obj, file, indent=2)

# Main
d_obj   = datetime.datetime.now()
s_year  = str(d_obj.year).zfill(4)
s_month = str(d_obj.month).zfill(2)
s_day   = str(d_obj.day).zfill(2)
s_hour  = str(d_obj.hour).zfill(2)
s_min   = str(d_obj.minute).zfill(2)
s_sec   = str(d_obj.second).zfill(2)
dir = "out_{}{}{}_{}{}{}".format(s_year, s_month, s_day, s_hour, s_min, s_sec)
captureFrame(dir, "grayscale")# Test
dumpJson(dir, "result")# Dump
cap.release()# Release
"""