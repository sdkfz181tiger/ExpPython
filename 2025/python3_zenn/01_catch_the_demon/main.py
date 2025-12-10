# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import tkinter

# キャンバスの幅と高さ
W, H = 480, 320

def init():
    """ 初期化する関数 """
    pass

def update():
    """ 更新する関数 """
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
