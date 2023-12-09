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

path_in  = "jumping_in.mov"
path_out = "jumping_out.gif"

w = 180
h = 80

x1 = 70
y1 = 330
x2 = x1 + w
y2 = y1 + h

clip = VideoFileClip(path_in)
clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
clip.write_gif(path_out, fps=6)
clip.close()
