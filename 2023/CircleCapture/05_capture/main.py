# coding: utf-8

"""
1, Install
	$ brew install ffmpeg
2, Fix fps to 30fps
	$ ffmpeg -i original.mp4 -r 30 original_fps30.mp4
3, Ready venv
	source your_location_of_venv_directory/bin/activate
4, Install modules
	python3 -m pip install opencv-python
	python3 -m pip install ffmpeg-python
	python3 -m pip install moviepy
	python3 -m pip install matplotlib
5, Run
	python3 main.py
"""

import os, shutil
from modules.circle_capture import CircleCapture
from modules.circle_renderer import CircleRenderer

def main():
	print("main")

	# Directory
	dir_input  = "../assets/movies/"
	dir_output = "test_output"

	original_input = "12_original_fps30.mp4"

	# Clean
	shutil.rmtree(dir_output)
	os.mkdir(dir_output)

	# Capture
	capture_list = [
		{"path_movie": "door/01/12_fps30.mp4",    "file_png": "cap_01.png", "file_json": "cap_01.json"},
		{"path_movie": "door/02/12_fps30.mp4",    "file_png": "cap_02.png", "file_json": "cap_02.json"},
		{"path_movie": "door/03/12_fps30.mp4",    "file_png": "cap_03.png", "file_json": "cap_03.json"},
		{"path_movie": "door/04/12_fps30.mp4",    "file_png": "cap_04.png", "file_json": "cap_04.json"},
		{"path_movie": "w_left/01/12_fps30.mp4",  "file_png": "cap_05.png", "file_json": "cap_05.json"},
		{"path_movie": "w_left/02/12_fps30.mp4",  "file_png": "cap_06.png", "file_json": "cap_06.json"},
		{"path_movie": "w_left/03/12_fps30.mp4",  "file_png": "cap_07.png", "file_json": "cap_07.json"},
		{"path_movie": "w_left/04/12_fps30.mp4",  "file_png": "cap_08.png", "file_json": "cap_08.json"},
		{"path_movie": "w_right/01/12_fps30.mp4", "file_png": "cap_09.png", "file_json": "cap_09.json"},
		{"path_movie": "w_right/02/12_fps30.mp4", "file_png": "cap_10.png", "file_json": "cap_10.json"},
		{"path_movie": "w_right/03/12_fps30.mp4", "file_png": "cap_11.png", "file_json": "cap_11.json"},
		{"path_movie": "w_right/04/12_fps30.mp4", "file_png": "cap_12.png", "file_json": "cap_12.json"}
	]
	
	for capture in capture_list:
		# CircleCapture
		cCapture = CircleCapture(dir_input + capture["path_movie"])# キャプチャ元映像
		cCapture.captureFrame(dir_output, capture["file_png"])# Capture
		cCapture.dumpJson(dir_output, capture["file_json"])# Dump
	
	# Render
	render_list = [
		{"file_json": "cap_01.json", "color": (255,   0,   0)},
		{"file_json": "cap_02.json", "color": (  0, 255,   0)},
		{"file_json": "cap_03.json", "color": (  0,   0, 255)},
		{"file_json": "cap_04.json", "color": (255, 255,   0)},
		{"file_json": "cap_05.json", "color": (255,   0, 255)},
		{"file_json": "cap_06.json", "color": (  0, 255, 255)},
		{"file_json": "cap_07.json", "color": (255,   0,   0)},
		{"file_json": "cap_08.json", "color": (  0,   0,   0)},
		{"file_json": "cap_09.json", "color": (  0,   0, 255)},
		{"file_json": "cap_10.json", "color": (255,   0,   0)},
		{"file_json": "cap_11.json", "color": (  0, 255,   0)}
	]

	# CircleRenderer
	cRendrer = CircleRenderer(dir_input + original_input)# レンダー元映像
	cRendrer.renderFrame(dir_output, "out_01.mp4", render_list)# 視線データを描画
	cRendrer.writeAudio(dir_output, dir_input + original_input, "audio.mp3", "out_01.mp4", "comp_01.mp4")# Audio
	
if __name__ == "__main__":
	main()