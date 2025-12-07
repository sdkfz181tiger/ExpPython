# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import random
import sprite
import tkinter

# キャンバスの幅と高さ
W, H = 600, 420

# Font
FONT = ("Arial", 16)

# マウスの座標
mx, my = 0, 0

# 鬼軍団
demons = []

# カウンタ
counter = 0

def init():
    global counter

    # 鬼軍団
    for i in range(10):
        x = random.random() * W
        y = random.random() * H
        demon = sprite.Demon(cvs, x, y, 20)
        spd = random.randint(1, 4)
        deg = random.randint(0, 360)
        demon.move(spd, deg) # ランダムで移動
        demons.append(demon)

    # カウンタ
    counter = len(demons)
    
def update():
    
    cvs.delete("hud")

    # マウス座標
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # カウンター
    msg = "COUNTER: {}".format(counter)
    cvs.create_text(20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="nw")

    # 鬼軍団
    for demon in demons:
        overlap_area(demon) # オーバーラップ
        demon.update(cvs)

    # 画面更新
    if 0 < counter:
        root.after(30, update)

def overlap_area(obj):
    if obj.x < 0: obj.set_x(W)
    if W < obj.x: obj.set_x(0)
    if obj.y < 0: obj.set_y(H)
    if H < obj.y: obj.set_y(0)

def on_mouse_moved(e):
    global mx, my
    mx, my = e.x, e.y

def on_mouse_clicked(e):
    global counter
    #print("Clicked:", e.x, e.y)

    # 鬼軍団
    for demon in demons:
        if demon.is_inside(e.x, e.y):
            if demon.is_dead(): continue
            demon.die(cvs)
            counter = counter - 1 # カウンタ
            break

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Motion>", on_mouse_moved) # マウス(Motion)
root.bind("<Button>", on_mouse_clicked) # マウス(Click)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
