# coding: utf-8

"""
かじるプログラミング
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

# Enemies
enemies = []

def init():
    global player, balls

    # Player
    player = sprite.Ball(W/2, H/2, 10, C_BLUE, C_RED)

    # Enemies
    for i in range(10):
        x = random.random() * W
        y = random.random() * H
        enemy = sprite.Ball(x, y, 10, C_GREEN, C_RED)
        enemy.move(SPD_ENEMY, random.randint(0, 360))
        enemies.append(enemy)

def update():
    cvs.delete("all")
    
    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill=C_WHITE, font=FONT)

    # Player
    player.update(cvs)
    overlap_area(player)

    # Enemies
    for enemy in enemies:
        enemy.update(cvs)
        overlap_area(enemy)
        if enemy.collide(player):
            enemy.die()
    
    root.after(30, update)

def overlap_area(obj):
    if obj.x < 0: obj.set_x(W)
    if W < obj.x: obj.set_x(0)
    if obj.y < 0: obj.set_y(H)
    if H < obj.y: obj.set_y(0)

def on_key_pressed(e):
    global player
    #print("key:", e)
    k = e.keysym
    if k == "w":
        player.move(SPD_PLAYER, 270)
    elif k == "a":
        player.move(SPD_PLAYER, 180)
    elif k == "s":
        player.move(SPD_PLAYER, 90)
    elif k == "d":
        player.move(SPD_PLAYER, 0)

def on_key_released(e):
    global player
    player.stop()

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
root.bind("<KeyPress>", on_key_pressed) # キーボード(Press)
root.bind("<KeyRelease>", on_key_released) # キーボード(Release)
root.bind("<Motion>", on_mouse_moved) # マウス(Motion)
root.bind("<Button>", on_mouse_clicked) # マウス(Click)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg=C_BLACK)
cvs.pack()
init()
update()
root.mainloop()
