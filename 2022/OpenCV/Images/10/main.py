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

# PhotoImage
def create_photo_img(img_back, img_front, w, h):
	# Image(back)
	img_back = cv2.cvtColor(img_back, cv2.COLOR_BGRA2RGBA) # BGR -> RGB
	print("img_back:", img_back.shape)
	pil_back = Image.fromarray(img_back) # RGB -> PIL
	# Image(front)
	img_front = cv2.cvtColor(img_front, cv2.COLOR_BGRA2RGBA) # BGR -> RGB
	print("img_front:", img_front.shape)
	pil_front = Image.fromarray(img_front) # RGB -> PIL
	# Alpha blend(同一画角である事)
	pil_dst = Image.alpha_composite(pil_back, pil_front) # Alpha blend
	return ImageTk.PhotoImage(pil_dst) # PIL -> PhotoImage

# Application
class Application(tk.Frame):

	def __init__(self, root=None, back=None, front=None):
		super().__init__(root)

		# Width, Height
		self.w = 480
		self.h = 320

		# Window
		self.root = root
		self.root.geometry(str(self.w) + "x" + str(self.h))
		self.root.title("Hello, App!!")

		# Image(CV)
		self.img_back  = cv2.imread(back, cv2.IMREAD_UNCHANGED)
		self.img_front = cv2.imread(front, cv2.IMREAD_UNCHANGED)

		# Canvas
		self.canvas = tk.Canvas(root, bg="silver", width=self.w, height=self.h)
		self.canvas.place(x=0, y=0)
		self.show()

		# Button
		btn_quit = tk.Button(self.root, text="Quit", command=self.quit)
		btn_quit.place(x=10, y=10)
		btn_show = tk.Button(self.root, text="Show", command=self.show)
		btn_show.place(x=80, y=10)

	def quit(self):
		self.root.destroy()

	def show(self):
		# Image(CV)
		self.img_tk = create_photo_img(self.img_back, self.img_front, self.w, self.h)
		self.canvas.create_image(self.w/2, self.h/2, image=self.img_tk, anchor=tk.CENTER)

# Main
app = Application(root=tk.Tk(), back="./images/img_back.png", front="./images/img_front.png")
app.mainloop()