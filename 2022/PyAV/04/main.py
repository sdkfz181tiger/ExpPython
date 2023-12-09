# coding: utf-8

"""
2つの動画から画像を合成 using Pillow
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

# Frame -> Image
def frame2image(frame, mask=False):
	frame = frame.to_ndarray(format="bgra") # BGRA
	frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA) # RGBA
	if mask == True: frame = 255 - frame # Mask
	return Image.fromarray(frame)

# Image -> Frame
def image2frame(image):
	frame = np.array(image, dtype=np.uint8)
	frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGRA) # BGRA
	frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR) # BGR
	return frame

# Load
def load_video(file, mask=False):
	container = av.open(file)
	stream = container.streams.video[0]
	images = []
	for frame in container.decode(video=0):
		image = frame2image(frame, mask=mask) # Image
		images.append(image)
	return images, stream.width, stream.height, stream.average_rate

# Overlay
def overlay_video(back, front, mask):
	return Image.composite(back, front, mask=mask)

# Loading
v_back, w, h, rate = load_video(f_back, mask=False) # Back
v_fronts = [] # Fronts
v_masks = [] # Masks
for file in f_fronts:
	v_front, _, _, _ = load_video(file, mask=False)
	v_fronts.append(v_front)
	v_mask, _, _, _ = load_video(file, mask=True)
	v_masks.append(v_mask)

# Export
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
v_out = cv2.VideoWriter("../assets/out_pil.mp4", fourcc, 30, (w, h))

# Show
for i in range(30):
	time_sta = time.perf_counter() # Time(start)
	image = v_back[i] # Image
	if 0 < len(v_fronts):
		for j in range(len(v_fronts)):
			if len(v_fronts[j]) <= i: continue
			image = overlay_video(image, v_fronts[j][i], v_masks[j][i])
	frame = image2frame(image) # Frame
	# Time
	time_delay = time.perf_counter() - time_sta  # Time(delay)
	time_str = "FPS:{}".format(1.0 / time_delay)
	cv2.putText(frame, time_str, (30, 60), f_style, f_scale, f_color)
	cv2.imshow("Video", frame) # Show
	v_out.write(frame) # Export
	# "Q" to Quit
	if cv2.waitKey(25) & 0xFF == ord("q"): break

v_out.release()
cv2.destroyAllWindows()