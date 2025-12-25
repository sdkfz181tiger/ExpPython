# coding: utf-8

"""
Python3_Zenn
"""

import tkinter

# キャンバスの幅と高さ
W = 600
H = 400

# Font
FONT = ("Arial", 24)

# カラー
c_red = "tomato"
c_green = "lime"
c_blue = "aqua"

# Ballの座標と大きさ
ball_x = W / 2
ball_y = H / 2
ball_r = 30

def on_mouse_moved(e):
    global ball_x, ball_y
    ball_x = e.x
    ball_y = e.y

def update():
    global ball_x, ball_y, ball_r
    cvs.delete("all")
    cvs.create_oval(ball_x, ball_y,
                    ball_x+ball_r, ball_y+ball_r,
                    fill=c_blue, width=0)
    root.after(30, update)

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
