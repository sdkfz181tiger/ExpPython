# coding: utf-8

"""
Python3_Zenn
"""

import math
import tkinter
import random

# キャンバスの幅と高さ
W = 600
H = 400

# Font
FONT = ("Arial", 12)

# カラー
c_red = "tomato"
c_green = "lime"
c_blue = "aqua"

# マウスの座標
mx = 0
my = 0

# Ballの座標と大きさ
ball_x = W / 2
ball_y = H / 2
ball_r = 30

# Ballの速度、角度
ball_spd = 6
ball_rad = (360 * random.random()) * (math.pi / 180)
ball_vx = math.cos(ball_rad) * ball_spd
ball_vy = math.sin(ball_rad) * ball_spd

def on_mouse_moved(e):
    global mx, my
    mx = e.x
    my = e.y

def update():
    global ball_x, ball_y, ball_vx, ball_vy
    
    cvs.delete("all")

    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg, font=FONT)

    # Ballの座標、速度
    ball_x = ball_x + ball_vx
    ball_y = ball_y + ball_vy
    if ball_x < 0: ball_x = W
    if ball_y < 0: ball_y = H
    if W < ball_x: ball_x = 0
    if H < ball_y: ball_y = 0
    
    # Ballを描画する
    cvs.create_oval(ball_x, ball_y,
                    ball_x+ball_r, ball_y+ball_r,
                    fill=c_green, width=0)
    
    root.after(20, update)

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Motion>", on_mouse_moved)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
update()
root.mainloop()
