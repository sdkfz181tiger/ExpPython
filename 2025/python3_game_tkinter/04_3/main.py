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

# マウスの座標
mx = W / 2
my = H / 2

# 円の座標,半径
cx = mx
cy = my
radius = 30

def move(e):
    global mx, my
    mx = e.x
    my = e.y

def update():
    global mx, my, cx, cy
    dx = (mx - cx) / 10
    dy = (my - cy) / 10
    cx += dx
    cy += dy
    cvs.delete("all")
    cvs.create_oval(cx-radius, cy-radius,
                    cx+radius, cy+radius,
                    fill="pink", width=0)
    root.after(40, update)

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Motion>", move)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
update()
root.mainloop()
