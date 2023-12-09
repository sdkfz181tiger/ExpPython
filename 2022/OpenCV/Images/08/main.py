# coding: utf-8

"""
Install
	pip install opencv-python
	pip install opencv-python-rolling
Tkinter
	brew install python-tk
"""

import cv2, random
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# Overlay
def overlay_img(img_back, img_front, lower, upper, pos):
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
	img_mask_1  = cv2.inRange(front_roi, lower, upper)
	img_mask_2  = 255 - img_mask_1 # Reverse
	# AND
	img_and_1 = cv2.bitwise_and(back_roi, back_roi, mask=img_mask_1)
	img_and_2 = cv2.bitwise_and(front_roi, front_roi, mask=img_mask_2)
	# OR
	img_or = cv2.bitwise_or(img_and_1, img_and_2)
	# Override
	img_back[y1:y2, x1:x2] = img_or
	return img_back

# PhotoImage
def create_photo_img(img_back, img_front, w, h):
	# Chromakey
	bgr_lower = np.array([0, 250, 0])   # Lower
	bgr_upper = np.array([10, 255, 10]) # Upper
	bH = img_back.shape[0]
	bW = img_back.shape[1]
	fH = img_front.shape[0]
	fW = img_front.shape[1]
	x = int(bW/2 - fW/2 + random.randint(-100, 100))
	y = int(bH/2 - fH/2 + random.randint(-100, 100))
	img_bgr = overlay_img(img_back, img_front, bgr_lower, bgr_upper, (x, y))
	img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # BGR -> RGB
	img_pil = Image.fromarray(img_rgb) # RGB -> PIL
	return ImageTk.PhotoImage(img_pil) # PIL -> PhotoImage

# Application
class Application(tk.Frame):

	def __init__(self, root=None):
		super().__init__(root)

		# Width, Height
		self.w = 480
		self.h = 320

		# Window
		self.root = root
		self.root.geometry(str(self.w) + "x" + str(self.h))
		self.root.title("Hello, App!!")

		# Image(File)
		#self.img_back = tk.PhotoImage(file="./images/img_back.png")
		#self.img_ninja = tk.PhotoImage(file="./images/img_black.png")

		# Image(CV)
		self.img_back  = cv2.imread("./images/img_back.png")
		self.img_front = cv2.imread("./images/img_front.png")

		# Image(CV)
		self.img_tk = create_photo_img(self.img_back, self.img_front, self.w, self.h)

		# Canvas
		self.canvas = tk.Canvas(root, bg="silver", width=self.w, height=self.h)
		self.canvas.place(x=0, y=0)
		#self.canvas.create_image(self.w/2, self.h/2, image=self.img_back, anchor=tk.CENTER)
		#self.canvas.create_image(self.w/2, self.h/2, image=self.img_ninja, anchor=tk.CENTER)
		self.canvas.create_image(self.w/2, self.h/2, image=self.img_tk, anchor=tk.CENTER)

# Main
app = Application(root=tk.Tk())
app.mainloop()