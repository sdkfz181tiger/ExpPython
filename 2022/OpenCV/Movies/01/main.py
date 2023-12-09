# coding: utf-8

"""
Install
	pip install opencv-python
	pip install numpy
"""

import cv2
import numpy as np

file_name = "../assets/sample01.mp4"

# Capture
cap = cv2.VideoCapture(file_name)

if cap.isOpened() == False:
	print("Cant't open:", file_name)

while cap.isOpened():
	# Read
	ret, frame = cap.read()
	if ret == True:
		# Image
		cv2.imshow("Video", frame)
		# "Q" to Quit
		if cv2.waitKey(25) & 0xFF == ord("q"):
			break
	else:
		break

cap.release()

cv2.destroyAllWindows()







