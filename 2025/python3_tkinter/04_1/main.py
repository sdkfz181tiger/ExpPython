# coding: utf-8

"""
Python3_Zenn
"""

import tkinter

# キャンバスの幅と高さ
W = 600
H = 400

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")

n = 0 # カウンター

def count():
    global n
    n = n + 1
    cvs.delete("all")
    cvs.create_text(W/2, H/2, text=n, font=("Arial", 80))
    root.after(1000, count)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
count()
root.mainloop()
