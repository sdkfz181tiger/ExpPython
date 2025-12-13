# coding: utf-8

"""
Python3_Zenn
"""

import tkinter

# キャンバスの幅と高さ
W = 600
H = 400

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")

# 虹の色
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

s = W / len(rainbow)
for i in range(len(rainbow)):
    x = i * s
    y = 0
    cvs.create_rectangle(x, y, x+s, y+s, fill=rainbow[i])

cvs.pack()
root.mainloop()
