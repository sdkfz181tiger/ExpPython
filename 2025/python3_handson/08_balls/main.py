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
C_WHITE = "white"
C_BLACK = "black"
C_GRAY = "gray"
C_RED = "tomato"
C_GREEN = "lime"
C_BLUE = "aqua"

# 速度
SPD_PLAYER = 4
SPD_ENEMY = 1

# マウスの座標
mx = 0
my = 0

# Player
player = None

# Balls
balls = []

def init():
    global player, balls

    # Player
    player = sprite.Ball(W/2, H/2, 10, C_BLUE)

    # Balls
    for i in range(10):
        x = random.random() * W
        y = random.random() * H
        ball = sprite.Ball(x, y, 10, C_GREEN)
        ball.set_speed(SPD_ENEMY, random.randint(0, 360))
        balls.append(ball)

def update():
    cvs.delete("all")
    
    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill=C_WHITE, font=FONT)

    # Player
    player.update(cvs)
    overlap_area(player)

    # Balls
    for ball in balls:
        ball.update(cvs)
        overlap_area(ball)
    
    root.after(30, update)

def overlap_area(ball):
    if ball.x < 0: ball.set_x(W)
    if W < ball.x: ball.set_x(0)
    if ball.y < 0: ball.set_y(H)
    if H < ball.y: ball.set_y(0)

def on_key_pressed(e):
    global player
    #print("key:", e.keysym)
    k = e.keysym
    if k == "w":
        player.set_speed(SPD_PLAYER, 270)
    elif k == "a":
        player.set_speed(SPD_PLAYER, 180)
    elif k == "s":
        player.set_speed(SPD_PLAYER, 90)
    elif k == "d":
        player.set_speed(SPD_PLAYER, 0)
    else:
        player.set_speed(0, 0)

def on_mouse_moved(e):
    global mx, my
    mx = e.x
    my = e.y

def on_mouse_clicked(e):
    global player
    print("Mouse:", e)
    
# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Key>", on_key_pressed)
root.bind("<Motion>", on_mouse_moved)
root.bind("<Button>", on_mouse_clicked)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg=C_BLACK)
cvs.pack()
init()
update()
root.mainloop()
