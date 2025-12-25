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
ball_r = 10

# Ballの速度、角度
ball_spd = 2
ball_rad = (360 * random.random()) * (math.pi / 180)
ball_vx = math.cos(ball_rad) * ball_spd
ball_vy = math.sin(ball_rad) * ball_spd

# Barの座標と大きさ
bar_x = W / 2
bar_y = H - 60
bar_w = 80
bar_h = 10

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
    if ball_x < ball_r: ball_vx = ball_vx * -1.0
    if ball_y < ball_r: ball_vy = ball_vy * -1.0
    if W < ball_x + ball_r: ball_vx = ball_vx * -1.0
    if H < ball_y + ball_r: ball_vy = ball_vy * -1.0
    
    # Ballを描画する
    cvs.create_oval(ball_x-ball_r, ball_y-ball_r,
                    ball_x+ball_r, ball_y+ball_r,
                    fill=c_green, width=0)
    
    # Barの座標
    bar_x = mx

    # Bar x Ball
    dx = abs(ball_x - bar_x)
    dy = abs(ball_y - bar_y)

    # Bar x Ball
    if dx < bar_w/2 and dy < (bar_h/2 + ball_r):
        if ball_vy < 0:
            ball_y = bar_y + bar_h/2 + ball_r
        else:
            ball_y = bar_y - bar_h/2 - ball_r
        ball_vy = ball_vy * -1.0 # y方向を逆転
         
    # Barを描画する
    cvs.create_rectangle(bar_x - bar_w/2, bar_y - bar_h/2,
                             bar_x + bar_w/2, bar_y + bar_h/2,
                             fill=c_blue, width=0)
    
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
