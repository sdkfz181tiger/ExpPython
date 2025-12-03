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

# カラーパレット
RAINBOW = ["red", "orange", "yellow", "green",
           "blue", "indigo", "violet"] 

def on_key_pressed(e):
    cvs.delete("all")
    k = e.keysym
    if "1" <= k and k <="7":
        size = 100
        cvs.create_rectangle(W/2-size/2, H/2-size/2,
                             W/2+size/2, H/2+size/2,
                             fill=RAINBOW[int(k)-1], width=0)

    msg = "key: {}".format(k)
    cvs.create_text(W/2, 50, text=msg, font=FONT)

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Key>", on_key_pressed)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
root.mainloop()
