# coding: utf-8
import time
from my_modules.movie_analysis import MovieCapture, MovieExporter

# MovieCapture
# 映像から円を判定し、JSONファイルに座標を書き出す
# 注意!!:合成元のオリジナル映像もOBS画面キャプチャしたものを使う事(FPSズレ対応)
# 編集ソフトを使い、"1970x720 30FPS"に出力したものでも可能
PREFIX = "teamD"

m_capture = MovieCapture()
m_capture.capture("../movies/" + PREFIX + "/01.mp4", "user_01", 1)
# m_capture.capture("../movies/" + PREFIX + "/02.mp4", "user_02", 1)
# m_capture.capture("../movies/" + PREFIX + "/03.mp4", "user_03", 1)
# m_capture.capture("../movies/" + PREFIX + "/04.mp4", "user_04", 1)

time.sleep(5)# Sleep

# MovieExporter
# JSONから座標を取得して動画へ描画する
json_list = [
	"./out/user_01/result.json",
	"./out/user_02/result.json",
	"./out/user_03/result.json",
	"./out/user_04/result.json"
]
color_list = [
	(255, 100, 100),
	(100, 255, 100),
	(100, 100, 255),
	(255, 255, 255)
	]
mp4_input  = "../original/" + PREFIX + "/original_ver2.mp4"# 合成元のファイル(OBS画面キャプチャしたものを使う事)
mp4_frames = "../result/" + PREFIX + "_frames.mp4"# フレームのみのファイル
mp4_output = "../result/" + PREFIX + "_output.mp4"# 音声合成後のファイル

m_exporter = MovieExporter()
m_exporter.exportMovie(mp4_input, mp4_frames, json_list, color_list)
m_exporter.exportSound(mp4_input, mp4_frames, mp4_output)