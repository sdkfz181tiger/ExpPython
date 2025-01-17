# coding: utf-8

"""
2つの動画から画像を合成 using OpenCV
"""

import cv2, av, time
import numpy as np
from PIL import Image

print("OpenCV:", cv2.__version__)
print("PyAV:", av.__version__)

# Back
f_back = "../assets/pudding01.mp4"
# Fronts
f_fronts = ["../assets/poppin01.mov", "../assets/frame01.mov"]

# Font
f_pos   = (30, 60)
f_style = cv2.FONT_HERSHEY_PLAIN
f_scale = 2
f_color = (0, 0, 0)

# Load
def load_video(file):
	container = av.open(file)
	stream = container.streams.video[0]
	frames = []
	for frame in container.decode(video=0):
		frames.append(frame.to_ndarray(format="bgra")) # BGRA
	return frames, stream.width, stream.height, stream.average_rate

# Overlay
def overlay_video(back, front):
	return cv2.addWeighted(back, 1.0, front, 1.0, 0)

# Back, Overlay
v_back, w, h, rate = load_video(f_back)
v_fronts = []
for file in f_fronts:
	v_front, _, _, _ = load_video(file)
	v_fronts.append(v_front)

# Export
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
v_out = cv2.VideoWriter("../assets/out_cv2.mp4", fourcc, 30, (w, h))

# Show
for i in range(80):
	time_sta = time.perf_counter() # Time(start)
	frame = v_back[i] # Frame
	print("frame:", i, frame.shape)
	if 0 < len(v_fronts):
		for front in v_fronts:
			if len(front) <= i: continue
			frame = overlay_video(frame, front[i])
	# Time
	time_delay = time.perf_counter() - time_sta  # Time(delay)
	time_str = "FPS:{}".format(1.0 / time_delay)
	cv2.putText(frame, time_str, (30, 60), f_style, f_scale, f_color)
	cv2.imshow("Video", frame) # Show
	v_out.write(cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)) # Export
	# "Q" to Quit
	if cv2.waitKey(25) & 0xFF == ord("q"): break

v_out.release()
cv2.destroyAllWindows()