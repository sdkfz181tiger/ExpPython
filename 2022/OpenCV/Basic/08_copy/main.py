# coding: utf-8

import cv2, datetime, ffmpeg, json, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

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