# coding: utf-8

"""
1, original.mp4のフレームレートを合わせる事
	$ ffmpeg -i original.mp4 -r 30 original_fps30.mp4
"""

from modules.circle_capture import CircleCapture
from modules.circle_renderer import CircleRenderer

def main():
	print("main")

	# Directory
	dir = "output_00"

	capture_list = [
		{"path_movie": "../assets/movies/cap_01_720.mp4", "file_png": "cap_01.png", "file_json": "cap_01.json"},
		{"path_movie": "../assets/movies/cap_02_720.mp4", "file_png": "cap_02.png", "file_json": "cap_02.json"},
		{"path_movie": "../assets/movies/cap_03_720.mp4", "file_png": "cap_03.png", "file_json": "cap_03.json"},
		{"path_movie": "../assets/movies/cap_04_720.mp4", "file_png": "cap_04.png", "file_json": "cap_04.json"},
		{"path_movie": "../assets/movies/cap_05_720.mp4", "file_png": "cap_05.png", "file_json": "cap_05.json"}
	]
	
	for capture in capture_list:
		# CircleCapture
		cCapture = CircleCapture(capture["path_movie"])# キャプチャ元映像
		cCapture.captureFrame(dir, capture["file_png"])# Capture
		cCapture.dumpJson(dir, capture["file_json"])# Dump
	
	render_list = [
		{"file_json": "cap_01.json", "color": (255, 0, 0)},
		{"file_json": "cap_02.json", "color": (0, 255, 0)},
		{"file_json": "cap_03.json", "color": (0, 0, 255)},
		{"file_json": "cap_04.json", "color": (255, 255, 0)},
		{"file_json": "cap_05.json", "color": (0, 255, 255)}
	]

	# CircleRenderer
	cRendrer = CircleRenderer("../assets/movies/original_720_fps30.mp4")# レンダー元映像
	cRendrer.renderFrame(dir, "out_01.mp4", render_list)# 視線データを描画
	cRendrer.writeAudio(dir, "../assets/movies/original_720_fps30.mp4", "audio.mp3", "out_01.mp4", "comp_01.mp4")# Audio

if __name__ == "__main__":
	main()