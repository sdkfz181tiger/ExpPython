# coding: utf-8

"""
2つの動画から画像を合成 using Pillow
"""

import cv2, av
import numpy as np
from PIL import Image

print("OpenCV:", cv2.__version__)
print("PyAV:", av.__version__)

# Input
f_back = "../assets/pudding01.mp4"
f_front = "../assets/poppin01.mov"

# Output
f_out = "../assets/out/test_{}.png"

# Images
i_backs  = []
i_fronts = []
i_masks  = []

# Frame -> Image
def frame2image(frame, mask=False):
	frame = frame.to_ndarray(format="bgra") # BGRA
	frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA) # RGBA
	if mask == True: frame = 255 - frame # Mask
	return Image.fromarray(frame)

# Image -> Frame
def image2frame(image):
	frame = np.array(image, dtype=np.uint8)
	return cv2.cvtColor(frame, cv2.COLOR_RGBA2BGRA) # BGRA

for frame in av.open(f_back).decode(video=0):
	i_backs.append(frame2image(frame))

for frame in av.open(f_front).decode(video=0):
	i_fronts.append(frame2image(frame))
	i_masks.append(frame2image(frame, True))

# Composite
for i in range(30):
	i_back = i_backs[i]
	i_front = i_fronts[i]
	i_mask = i_masks[i]
	i_out = Image.composite(i_back, i_front, mask=i_mask)
	i_out.save(f_out.format(i))