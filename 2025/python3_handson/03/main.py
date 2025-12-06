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

# Ballの座標と大きさ、速度
ball_x = W / 2
ball_y = H / 2
ball_r = 30
ball_vx = 1
ball_vy = 1

mx = 0
my = 0

def on_mouse_moved(e):
    global mx, my
    mx = e.x
    my = e.y

def update():
    global ball_x, ball_y, ball_vx, ball_vy

    # Ballの座標、速度
    ball_x = ball_x + ball_vx
    ball_y = ball_y + ball_vy
    if ball_x < 0: ball_x = W
    if ball_y < 0: ball_y = H
    if W < ball_x: ball_x = 0
    if H < ball_y: ball_y = 0
    
    cvs.delete("all")
    cvs.create_oval(ball_x, ball_y,
                    ball_x+ball_r, ball_y+ball_r,
                    fill=c_green, width=0)
    
    root.after(50, update)

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
