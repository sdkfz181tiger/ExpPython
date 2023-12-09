# coding: utf-8

"""
深層学習を使った予測_MNIST
"""

from modules.SimpleDL import MyModel
from modules.Utility import load_model

import numpy as np
import tkinter

# マウスドラッグで実行される関数
def draw(event):
	global draw_input
	x = int(event.x / 15)
	y = int(event.y / 15)
	canvas.create_rectangle(x*15, y*15,
		x*15+15, y*15+15, fill="black", width=1)
	draw_input[x + y*28] = 255

# 予測ボタンが押された時に実行
def predict():
	pred = model.predict([draw_input / 255.0])
	pred_classes = np.argmax(pred, axis=1)
	label["text"] = str(pred_classes[0])

# クリアボタンが押された時に実行
def clear():
	global draw_input
	draw_input = np.zeros(28 * 28)
	canvas.delete("all")
	label["text"] = " "

"""
メイン処理
"""

# 入力データ
draw_input = np.zeros(28 * 28)

# Model
model = load_model("mnist.model")

# Tk
root = tkinter.Tk()
root.geometry("420x540")

# Canvas
canvas = tkinter.Canvas(root, width=420, height=420, bg="white")
canvas.pack()
canvas.bind("<B1-Motion>", draw)

# Buttons
btn1 = tkinter.Button(root, text="=予測=", command=predict)
btn1.pack(side="left")
btn2 = tkinter.Button(root, text="=削除=", command=clear)
btn2.pack(side="left")

# Label
label = tkinter.Label(root, text=" ", font=("", "78"))
label.pack(side="bottom")

root.mainloop()
