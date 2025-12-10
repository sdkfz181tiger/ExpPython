# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math   # 数学的計算をするモジュール
import random # ランダムを生成するモジュール
import sprite # Spriteモジュール
import tkinter

W, H = 480, 320

FONT = ("Arial", 16)

mx, my = 0, 0

bg_photo, bg_image = None, None

# 鬼軍団の数
TOTAL_DEMONS = 10

# 鬼軍団
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
        demons.append(demon)
    
def update():
    """ 更新関数 """
    cvs.delete("hud")

    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 鬼軍団
    for demon in demons:
        demon.update(cvs)

    # 画面更新
    root.after(30, update)

def on_mouse_clicked(e):
    global counter
    #print("Clicked:", e.x, e.y)

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
