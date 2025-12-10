# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import random
import sprite
import tkinter

# キャンバスの幅と高さ
W, H = 480, 320

# フォント
FONT = ("Arial", 16)

# マウスの座標
mx, my = 0, 0

# 背景画像とイメージ
bg_photo, bg_image = None, None

def init():
    """ 初期化関数 """
    global bg_photo, bg_image

    # 背景
    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)
    
def update():
    """ 更新関数 """
    cvs.delete("hud")

    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 画面更新
    root.after(30, update)

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
