# coding: utf-8

"""
Install
	pip install opencv-python
	pip install opencv-python-rolling
Tkinter
	brew install python-tk
"""

import cv2
import numpy as np
import tkinter as tk

def on_quit():
	print("Quit!!")
	tki.destroy()

def on_test_1():
	print("Test1!!")
	ent_a.delete(0, tk.END)
	ent_a.insert(0, "Hello, Tkinter!!")

def on_test_2():
	print("Test2!!")
	ent_b.delete(0, tk.END)
	ent_b.insert(0, ent_a.get())

def on_test_3():
	print("Test3!!")
	ent_a.delete(0, tk.END)
	ent_b.delete(0, tk.END)

# 画面作成
tki = tk.Tk()
tki.geometry("480x320")
tki.title("ボタンイベント")

# ラベル
lbl_a = tk.Label(text="LabelA")
lbl_a.place(x=100, y=70)
ent_a = tk.Entry(width=20)
ent_a.place(x=160, y=70)

lbl_b = tk.Label(text="LabelB")
lbl_b.place(x=100, y=120)
ent_b = tk.Entry(width=20)
ent_b.place(x=160, y=120)

# ボタン
btn_quit = tk.Button(tki, text="Quit", command=on_quit)
btn_quit.place(x=10, y=10)

btn_test_1 = tk.Button(tki, text="Btn1", command=on_test_1)
btn_test_1.place(x=140, y=170)

btn_test_2 = tk.Button(tki, text="Btn2", command=on_test_2)
btn_test_2.place(x=220, y=170)

btn_test_3 = tk.Button(tki, text="Btn3", command=on_test_3)
btn_test_3.place(x=300, y=170)

# 画面表示
tki.mainloop()