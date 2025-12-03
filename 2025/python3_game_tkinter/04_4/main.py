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

# メッセージ
msg = "xxx"

def on_key_pressed(e):
    global msg
    msg = "key: {}".format(e.keysym)

def update():
    global msg
    cvs.delete("all")
    cvs.create_text(W/2, H/2, text=msg, font=FONT)
    root.after(50, update)

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Key>", on_key_pressed)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
update()
root.mainloop()
