# coding: utf-8

"""
Python3_Zenn
"""

import tkinter

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")

# キャンバス
cvs = tkinter.Canvas(width=600, height=400, bg="black")

# 画像データ(霊夢)
img_reimu = tkinter.PhotoImage(file="images/reimu.png")
cvs.create_image(200, 200, image=img_reimu)

# 画像データ(魔理沙)
img_marisa = tkinter.PhotoImage(file="images/marisa.png")
cvs.create_image(400, 200, image=img_marisa)

cvs.pack()
root.mainloop()
