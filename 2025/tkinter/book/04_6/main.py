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
c_red = "red"
c_green = "green"
c_blue = "blue"

# 円の中心座標
cx = W / 2
cy = H / 2
cr = 60

mx = 0
my = 0
mr = 40

def on_mouse_moved(e):
    global mx, my
    mx = e.x
    my = e.y

def update():
    cvs.delete("all")
    cvs.create_oval(cx-cr, cy-cr,
                    cx+cr, cy+cr,
                    fill=c_green, width=0)
    dist = ((mx-cx)**2 + (my-cy)**2)**0.5
    if dist < (mr+cr):
        cvs.create_oval(mx-mr, my-mr,
                        mx+mr, my+mr,
                        fill=c_red, width=0)
    else:
        cvs.create_oval(mx-mr, my-mr,
                        mx+mr, my+mr,
                        fill=c_blue, width=0)
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
