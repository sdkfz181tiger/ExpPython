# coding: utf-8

"""
Command
バージョン確認
	python --version
インストール済みライブラリ一覧
	pip3 list
ライブラリインストール
	pip3 install numpy
"""

# MoviePy
from moviepy.editor import *

print("Hello, Python3!?")

path_in  = "sample_in.mp4"
path_out = "sample_out.mp4"

w = 90
h = 110

x1 = 55
y1 = 110
x2 = x1 + w
y2 = y1 + h

clip = VideoFileClip(path_in)
clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
clip.write_videofile(path_out, fps=29)
clip.close()
