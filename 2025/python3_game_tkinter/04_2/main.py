# coding: utf-8

"""
Python3_Zenn
"""

import tkinter

# キャンバスの幅と高さ
W = 600
H = 400

# Font
FONT = ("Arial", 24)

def move(e):
    cvs.delete("all")
    x = e.x
    y = e.y
    msg = "x:{}, y:{}".format(x, y)
    cvs.create_text(x, y, text=msg, font=FONT)

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.bind("<Motion>", move)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
root.mainloop()
