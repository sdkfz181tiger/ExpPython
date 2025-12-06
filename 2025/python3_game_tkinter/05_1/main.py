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

# 四角の中心座標
bx = W / 2
by = H / 2
bw = 60
bh = 40

mx = 0
my = 0
mw = 40
mh = 20

def on_mouse_moved(e):
    global mx, my
    mx = e.x
    my = e.y

def update():
    cvs.delete("all")
    cvs.create_rectangle(bx-bw, by-bh,
                         bx+bw, by+bh,
                         fill=c_green, width=0)
    dx = abs(bx - mx)
    dy = abs(by - my)
    if dx < (bw + mw) and dy < (bh + mh):
        cvs.create_rectangle(mx-mw, my-mh,
                             mx+mw, my+mh,
                             fill=c_red, width=0)
    else:
        cvs.create_rectangle(mx-mw, my-mh,
                             mx+mw, my+mh,
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
