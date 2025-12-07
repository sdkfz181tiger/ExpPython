# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import random
import sprite
import tkinter

# キャンバスの幅と高さ
W, H = 600, 400

# Font
FONT = ("Arial", 16)

# カウンタ
cnt = 0

# マウスの座標
mx, my = 0, 0

# 速度
SPD_PLAYER = 4
SPD_ENEMY = 1

# Player
player = None

# Enemies
enemies = []

# Interval
interval_cnt = 0
interval_limit = 4

def init():
    global player

    # Player
    player = sprite.Sprite(cvs, "images/reimu.png", W/2, H/2, "aqua")
    
    # Enemies
    for i in range(10):
        append_enemy()
    
def update():
    global cnt, interval_cnt
    
    cvs.delete("hud")

    # カウンタ
    cnt = cnt + 1

    # Player
    player.update(cvs)
    overlap_area(player)

    # Enemies
    for enemy in enemies:
        enemy.update(cvs)
        overlap_area(enemy)
        if enemy.collide(player):
           player.die()

    # Interval
    interval_cnt = interval_cnt + 1
    if interval_limit < interval_cnt:
        interval_cnt = 0
        append_enemy()

    # HUD
    show_hud()

    # Update
    if not player.is_dead():
        root.after(30, update)

def append_enemy():
    enemy = sprite.Sprite(cvs, "images/marisa.png", 0, 0, "tomato")
    enemy.move(SPD_ENEMY, random.randint(0, 360))
    enemies.append(enemy)

def show_hud():

    # マウス座標
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # カウンタ
    msg = "CNT: {}".format(cnt)
    cvs.create_text(W-20, 20, text=msg,
                    fill="white", font=FONT, anchor="ne", tag="hud")

    # スコア
    msg = "SCORE: {}".format(len(enemies))
    cvs.create_text(20, 20, text=msg,
                    fill="white", font=FONT, anchor="nw", tag="hud")

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
    player.stop()

def on_mouse_moved(e):
    global mx, my
    mx, my = e.x, e.y

def on_mouse_clicked(e):
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
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
