# coding: utf-8

"""
1, 視線計測時、各動画を1本にした動画を使う事(目線が泳がなく)
2, original.mp4のフレームレートを合わせる事
	$ ffmpeg -i original.mp4 -r 30 original_fps30.mp4
"""

from modules.circle_capture import CircleCapture
from modules.circle_renderer import CircleRenderer

def main():
	print("main")

	# Directory
	dir_input = "../assets/team07_input/"
	dir_output  = "team07_output"

	capture_list = [
		{"path_movie": "cap_01.mov", "file_png": "cap_01.png", "file_json": "cap_01.json"},
		{"path_movie": "cap_02.mov", "file_png": "cap_02.png", "file_json": "cap_02.json"},
		{"path_movie": "cap_03.mov", "file_png": "cap_03.png", "file_json": "cap_03.json"},
		{"path_movie": "cap_04.mov", "file_png": "cap_04.png", "file_json": "cap_04.json"},
		{"path_movie": "cap_05.mov", "file_png": "cap_05.png", "file_json": "cap_05.json"},
		{"path_movie": "cap_06.mov", "file_png": "cap_06.png", "file_json": "cap_06.json"},
		{"path_movie": "cap_07.mov", "file_png": "cap_07.png", "file_json": "cap_07.json"},
		{"path_movie": "cap_08.mov", "file_png": "cap_08.png", "file_json": "cap_08.json"},
		{"path_movie": "cap_09.mov", "file_png": "cap_09.png", "file_json": "cap_09.json"},
		{"path_movie": "cap_10.mov", "file_png": "cap_10.png", "file_json": "cap_10.json"},
	]
	
	for capture in capture_list:
		# CircleCapture
		cCapture = CircleCapture(dir_input + capture["path_movie"])# キャプチャ元映像
		cCapture.captureFrame(dir_output, capture["file_png"])# Capture
		cCapture.dumpJson(dir_output, capture["file_json"])# Dump
	
	render_list = [
		{"file_json": "cap_01.json", "color": (255,   0,   0)},
		{"file_json": "cap_02.json", "color": (  0, 255,   0)},
		{"file_json": "cap_03.json", "color": (  0,   0, 255)},
		{"file_json": "cap_04.json", "color": (255, 255,   0)},
		{"file_json": "cap_05.json", "color": (  0, 255, 255)},
		{"file_json": "cap_06.json", "color": (255,   0, 255)},
		{"file_json": "cap_07.json", "color": (100,   0,   0)},
		{"file_json": "cap_08.json", "color": (  0, 100,   0)},
		{"file_json": "cap_09.json", "color": (  0,   0, 100)},
		{"file_json": "cap_10.json", "color": (255, 255, 255)},
	]

	# CircleRenderer
	cRendrer = CircleRenderer(dir_input + "original_fps30.mov")# レンダー元映像
	cRendrer.renderFrame(dir_output, "out_01.mov", render_list)# 視線データを描画
	cRendrer.writeAudio(dir_output, dir_input + "original_fps30.mov", "audio.mp3", "out_01.mov", "comp_01.mov")# Audio
	
if __name__ == "__main__":
	main()