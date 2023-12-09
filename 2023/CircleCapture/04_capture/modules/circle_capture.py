# coding: utf-8

import cv2, datetime, ffmpeg, json, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# CircleCapture
class CircleCapture:

	def __init__(self, path_movie):
		print("CircleCapture")

		# Movie
		self.cap   = cv2.VideoCapture(path_movie)# Movie
		self.W     = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
		self.H     = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
		self.COUNT = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))# Count
		self.FPS   = int(self.cap.get(cv2.CAP_PROP_FPS))# Fps
		print("Video W:%d H:%d COUNT:%d FPS:%d" % (self.W, self.H, self.COUNT, self.FPS))

		# Json
		self.json_str = """{
			"data":[]
		}
		"""
		self.json_obj = json.loads(self.json_str)

	def captureFrame(self, dir, file_png, off=1):
		#print("captureFrame!!")

		if not self.cap.isOpened(): return
		os.makedirs(dir, exist_ok=True)# Directory
		file_names = file_png.split(".")
		name = file_names[0]
		ext = file_names[len(file_names)-1]
		path = os.path.join(dir, name)
		digit = len(str(int(self.COUNT)))
		for n in range(self.COUNT):
			ret, frame = self.cap.read()# Read
			if not ret: return
			if n%off!=0: continue
			self.writeFrame(n, "{}_{}.{}".format(path, str(n).zfill(digit), ext), frame)

	def writeFrame(self, n, path, frame):
		#print("writeFrame!!")

		bgr_lower  = np.array([0, 0, 180])
		bgr_upper  = np.array([80, 80, 255])
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

		found = False
		for cnt in contours:
			(x, y), radius = cv2.minEnclosingCircle(cnt)
			center = (int(x), int(y))
			percent = (int((x/self.W)*100), int((y/self.H)*100))
			if radius > 20:
				approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
				cv2.drawContours(img_gray, [approx], 0, l_color, l_width)
				cv2.putText(img_gray, "{0},{1}".format(percent[0], percent[1]), center, f_style, f_scale, f_color)
				self.json_obj["data"].append({"frame": n, "x": percent[0], "y": percent[1]})# Found
				found = True
				break
		if not found: self.json_obj["data"].append({"frame": n, "x": 0, "y": 0})# Not found
		#cv2.imwrite(path, img_gray)# Image(For test!!)

	def dumpJson(self, dir, file_json):
		#print("dumpJson!!")

		os.makedirs(dir, exist_ok=True)# Directory
		path = os.path.join(dir, file_json)
		with open(path, "w") as file:
			json.dump(self.json_obj, file, indent=2)

