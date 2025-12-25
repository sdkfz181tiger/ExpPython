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
cvs.create_line(0, 0, 580, 380, fill="red", width=1)
cvs.pack()
root.mainloop()
