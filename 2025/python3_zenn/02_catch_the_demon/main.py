# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import tkinter

# キャンバスの幅と高さ
W, H = 480, 320

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
    pass

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
