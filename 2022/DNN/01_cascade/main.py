# coding: utf-8

"""
Viola-Jones法による顔検出
特徴:
	OpenCVで広く使われてきた手法
	明暗の特徴とカスケード型の分類器を組み合わせる
分類器:
	https://github.com/opencv/opencv/tree/master/data/haarcascades
"""

import cv2, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Directory
dir_current = os.path.dirname(__file__)

# Image
img_from = os.path.join(dir_current, "image.jpg")
capture = cv2.VideoCapture(img_from)
if not capture.isOpened():
	raise IOError("Can't open image...")

# Cascade
path_xml = os.path.join(dir_current, "../models/cascade/haarcascade_frontalface_default.xml")
cascade = cv2.CascadeClassifier(path_xml)
if cascade is None:
	raise IOError("Can't read cascade...")

# Grayscale
result, image = capture.read()
img_to = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detection
height, width = img_to.shape
min_size = (int(width/10), int(height/10))
boxes = cascade.detectMultiScale(img_to, minSize = min_size)
for box in boxes:
	cv2.rectangle(img_to, box, (255, 255, 255), 1, cv2.LINE_AA)
cv2.imwrite("result.png", img_to)