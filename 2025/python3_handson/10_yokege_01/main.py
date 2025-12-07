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

# マウスの座標
mx, my = 0, 0

def init():
    pass
    
def update():
    global cnt, interval_cnt
    
    cvs.delete("hud")

    # マウス座標
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # Update
    root.after(30, update)

def on_mouse_moved(e):
    global mx, my
    mx, my = e.x, e.y

def on_mouse_clicked(e):
    print("Clicked:", e.x, e.y)

def on_key_pressed(e):
    print("Key:", e.keysym)

def on_key_released(e):
    pass

    
# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Motion>", on_mouse_moved) # マウス(Motion)
root.bind("<Button>", on_mouse_clicked) # マウス(Click)
root.bind("<KeyPress>", on_key_pressed) # キーボード(Press)
root.bind("<KeyRelease>", on_key_released) # キーボード(Release)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
