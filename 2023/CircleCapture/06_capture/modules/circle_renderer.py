# coding: utf-8

import cv2, datetime, ffmpeg, json, os
import numpy as np
from moviepy import VideoFileClip, AudioFileClip, AudioArrayClip
from PIL import Image

# CircleRenderer
class CircleRenderer:

	def __init__(self, path_movie):
		print("CircleRenderer")

		# Movie
		self.cap   = cv2.VideoCapture(path_movie)# Movie
		self.W     = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
		self.H     = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
		self.COUNT = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))# Count
		self.FPS   = int(self.cap.get(cv2.CAP_PROP_FPS))# Fps
		print("Video W:%d H:%d COUNT:%d FPS:%d" % (self.W, self.H, self.COUNT, self.FPS))

	def renderFrame(self, dir, path_movie, render_list):
		print("renderFrame!!")

		# Movie
		path = os.path.join(dir, path_movie)
		fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
		cap_out = cv2.VideoWriter(path, fourcc, self.FPS, (self.W, self.H))

		# JsonObjects
		obj_jsons = []

		# RenderList
		for render in render_list:
			# JSON
			path = os.path.join(dir, render["file_json"])
			with open(path, "r") as file:
				obj_jsons.append(json.load(file))

		# Render
		for n in range(self.COUNT):
			ret, frame = self.cap.read()# Read
			if ret==False: break
			self.drawGrid(frame, (140, 140, 140), 1)
			for i, render in enumerate(render_list):
				if len(obj_jsons[i]["data"]) <= n : continue
				data = obj_jsons[i]["data"][n]# Data
				if int(data["x"]) <= 0 or int(data["x"]) <= 0: continue
				# Color
				l_color = render["color"]
				l_width = 2
				f_style = cv2.FONT_HERSHEY_DUPLEX
				f_scale = 0.2
				f_color = (255, 255, 255)
				# Draw
				center = (int(self.W * (int(data["x"]) / 100)), int(self.H * (int(data["y"]) / 100)))
				radius = int(self.W/20 if self.W<self.H else self.H/20)
				text = "{0}:{0},{1}".format(data["frame"], center[0], center[1])
				cv2.circle(frame, center, radius, l_color, l_width)
				cv2.putText(frame, text, center, f_style, f_scale, f_color)
			cap_out.write(frame)

	def drawGrid(self, frame, l_color, l_width):
		g_size = int(self.W / 20)
		rows = int(self.H / g_size)
		cols = int(self.W / g_size)
		for r in range(1, rows):
			y = r * g_size
			cv2.line(frame, (0, y), (self.W, y), l_color, l_width)
			for c in range(1, cols):
				x = c * g_size
				cv2.line(frame, (x, 0), (x, self.H), l_color, l_width)

	def writeAudio(self, dir, path_from, file_audio, file_target, file_comp):
		print("writeAudio!!")
		# From
		clip_from = VideoFileClip(path_from).subclipped()
		# Audio
		path = os.path.join(dir, file_audio)
		clip_from.audio.write_audiofile(path)
		clip_audio = AudioFileClip(path)
		# Target
		path = os.path.join(dir, file_target)
		clip_target = VideoFileClip(path).subclipped()
		# Comp
		path = os.path.join(dir, file_comp)
		clip_comp = clip_target.with_audio(clip_audio)
		clip_comp.write_videofile(path, codec="libx264", audio_codec="aac")