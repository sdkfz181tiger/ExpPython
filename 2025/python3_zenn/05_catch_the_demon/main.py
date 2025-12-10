# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import random
import sprite
import tkinter

W, H = 480, 320

FONT = ("Arial", 16)

mx, my = 0, 0

bg_photo, bg_image = None, None

TOTAL_DEMONS = 10

demons = []

def init():
    """ 初期化関数 """
    global bg_photo, bg_image

    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)

    # 鬼軍団
    for i in range(TOTAL_DEMONS):
        x = random.random() * W
        y = random.random() * H
        demon = sprite.DemonSprite(cvs, x, y, 20)
        spd = random.randint(1, 4)
        deg = random.randint(0, 360)
        demon.move(spd, deg)
        demons.append(demon)
    
def update():
    """ 更新関数 """
    cvs.delete("hud")

    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 鬼軍団
    for demon in demons:
        overlap_area(demon) # 画面外判定
        demon.update(cvs)

    root.after(30, update)

def overlap_area(obj):
    if obj.x < 0: obj.set_x(W) # x座標が画面の左端より小さい時は右端へ
    if W < obj.x: obj.set_x(0) # x座標が画面の右端より大きい時は左端へ
    if obj.y < 0: obj.set_y(H)
    if H < obj.y: obj.set_y(0)

def on_mouse_clicked(e):
    print("Clicked:", e.x, e.y)

def on_mouse_moved(e):
    global mx, my
    mx, my = e.x, e.y

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Button>", on_mouse_clicked) # マウス(Click)
root.bind("<Motion>", on_mouse_moved) # マウス(Motion)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
