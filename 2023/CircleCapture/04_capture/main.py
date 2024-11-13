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

from modules.circle_capture import CircleCapture
from modules.circle_renderer import CircleRenderer

def main():
	print("main")

	# Directory
	dir_input = "../assets/movies/"
	dir_output  = "test_output"

	capture_list = [
		{"path_movie": "cap_01.mp4", "file_png": "cap_01.png", "file_json": "cap_01.json"},
		{"path_movie": "cap_02.mp4", "file_png": "cap_02.png", "file_json": "cap_02.json"},
		{"path_movie": "cap_03.mp4", "file_png": "cap_03.png", "file_json": "cap_03.json"}
	]
	
	for capture in capture_list:
		# CircleCapture
		cCapture = CircleCapture(dir_input + capture["path_movie"])# キャプチャ元映像
		cCapture.captureFrame(dir_output, capture["file_png"])# Capture
		cCapture.dumpJson(dir_output, capture["file_json"])# Dump
	
	render_list = [
		{"file_json": "cap_01.json", "color": (255,   0,   0)},
		{"file_json": "cap_02.json", "color": (  0, 255,   0)},
		{"file_json": "cap_03.json", "color": (  0,   0, 255)}
	]

	# CircleRenderer
	cRendrer = CircleRenderer(dir_input + "original_fps30.mp4")# レンダー元映像
	cRendrer.renderFrame(dir_output, "out_01.mp4", render_list)# 視線データを描画
	cRendrer.writeAudio(dir_output, dir_input + "original_fps30.mp4", "audio.mp3", "out_01.mp4", "comp_01.mp4")# Audio
	
if __name__ == "__main__":
	main()