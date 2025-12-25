# coding: utf-8

"""
Python3_Zenn
"""

import math
import sprite
import tkinter
import random

# キャンバスの幅と高さ
W = 600
H = 400

# Font
FONT = ("Arial", 12)

# カラー
c_white = "white"
c_black = "black"
c_gray = "gray"
c_red = "tomato"
c_green = "lime"
c_blue = "aqua"

# マウスの座標
mx = 0
my = 0

# Balls
balls = []

def init():
    global balls

    # Balls
    for i in range(10):
        x = random.random() * W
        y = random.random() * H
        ball = sprite.Ball(x, y, 10)
        balls.append(ball)

def update():
    cvs.delete("all")
    
    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill=c_white, font=FONT)

    for ball in balls:
        ball.update(cvs)
    
    root.after(100, update)

def on_mouse_moved(e):
    global mx, my
    mx = e.x
    my = e.y

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Motion>", on_mouse_moved)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg=c_black)
cvs.pack()
init()
update()
root.mainloop()
