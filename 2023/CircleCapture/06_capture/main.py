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

	team_no = "13" # Team No
	original_input = team_no + "_original_fps30.mp4"

	# Clean
	shutil.rmtree(dir_output)
	os.mkdir(dir_output)

	# Capture
	capture_list = [
		{"path_movie": "captured/" + team_no + "/door_01_"  + team_no + ".mov",  "file_png": "door_01_01.png",  "file_json": "01.json"},
		{"path_movie": "captured/" + team_no + "/door_02_"  + team_no + ".mov",  "file_png": "door_02_01.png",  "file_json": "02.json"},
		{"path_movie": "captured/" + team_no + "/door_03_"  + team_no + ".mov",  "file_png": "door_03_01.png",  "file_json": "03.json"},
		{"path_movie": "captured/" + team_no + "/door_04_"  + team_no + ".mov",  "file_png": "door_04_01.png",  "file_json": "04.json"},
		{"path_movie": "captured/" + team_no + "/left_01_"  + team_no + ".mov",  "file_png": "left_01_01.png",  "file_json": "05.json"},
		{"path_movie": "captured/" + team_no + "/left_02_"  + team_no + ".mov",  "file_png": "left_02_01.png",  "file_json": "06.json"},
		{"path_movie": "captured/" + team_no + "/left_03_"  + team_no + ".mov",  "file_png": "left_03_01.png",  "file_json": "07.json"},
		{"path_movie": "captured/" + team_no + "/left_04_"  + team_no + ".mov",  "file_png": "left_04_01.png",  "file_json": "08.json"},
		{"path_movie": "captured/" + team_no + "/right_01_" + team_no + ".mov",  "file_png": "right_01_01.png", "file_json": "09.json"},
		{"path_movie": "captured/" + team_no + "/right_02_" + team_no + ".mov",  "file_png": "right_02_01.png", "file_json": "10.json"},
		{"path_movie": "captured/" + team_no + "/right_03_" + team_no + ".mov",  "file_png": "right_03_01.png", "file_json": "11.json"},
		{"path_movie": "captured/" + team_no + "/right_04_" + team_no + ".mov",  "file_png": "right_04_01.png", "file_json": "12.json"}
	]
	
	for capture in capture_list:
		# CircleCapture
		cCapture = CircleCapture(dir_input + capture["path_movie"])# キャプチャ元映像
		cCapture.captureFrame(dir_output, capture["file_png"])# Capture
		cCapture.dumpJson(dir_output, capture["file_json"])# Dump
	
	# Render
	render_list = [
		{"file_json": "01.json", "color": (  0,   0,   0)},
		{"file_json": "02.json", "color": (255, 255, 255)},
		{"file_json": "03.json", "color": (255,   0,   0)},
		{"file_json": "04.json", "color": (  0, 255,   0)},
		{"file_json": "05.json", "color": (  0,   0, 255)},
		{"file_json": "06.json", "color": (255, 255,   0)},
		{"file_json": "07.json", "color": (  0, 255, 255)},
		{"file_json": "08.json", "color": (255,   0, 255)},
		{"file_json": "09.json", "color": (100, 100, 100)},
		{"file_json": "10.json", "color": (100, 255, 255)},
		{"file_json": "11.json", "color": (255, 100, 255)},
		{"file_json": "12.json", "color": (255, 255, 100)}
	]

	# CircleRenderer
	cRendrer = CircleRenderer(dir_input + original_input)# レンダー元映像
	cRendrer.renderFrame(dir_output, "out.mp4", render_list)# 視線データを描画
	cRendrer.writeAudio(dir_output, dir_input + original_input, "audio.mp3", "out.mp4", "comp_" + team_no + ".mp4")# Audio
	
if __name__ == "__main__":
	main()