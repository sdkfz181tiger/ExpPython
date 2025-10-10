# coding: utf-8

"""
1, Install
	$ brew install ffmpeg
2, All movies needs same fps to 30fps
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

	team_no = "99" # Team No
	original_input = team_no + "_original_fps30.mp4"

	# Clean
	shutil.rmtree(dir_output)
	os.mkdir(dir_output)

	# Capture
	capture_list = [
		{"path_movie": "door/01/" + team_no + "_fps30.mp4",    "file_png": "cap_01.png", "file_json": "cap_01.json"}
	]
	
	for capture in capture_list:
		# CircleCapture
		cCapture = CircleCapture(dir_input + capture["path_movie"])# キャプチャ元映像
		cCapture.captureFrame(dir_output, capture["file_png"])# Capture
		cCapture.dumpJson(dir_output, capture["file_json"])# Dump
	
	# Render
	render_list = [
		{"file_json": "cap_01.json", "color": (255,   0,   0)}
	]

	# CircleRenderer
	cRendrer = CircleRenderer(dir_input + original_input)# レンダー元映像
	cRendrer.renderFrame(dir_output, "out.mp4", render_list)# 視線データを描画
	cRendrer.writeAudio(dir_output, dir_input + original_input, "audio.mp3", "out.mp4", "comp_" + team_no + ".mp4")# Audio
	
if __name__ == "__main__":
	main()