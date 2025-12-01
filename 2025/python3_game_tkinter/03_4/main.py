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

# 文字を表示する
cvs.create_text(300, 50, text="Hello, Tkinter!!")

# 直線
cvs.create_line(0, 0, 580, 380, fill="red", width=1)

# 四角形
cvs.create_rectangle(50, 50, 100, 100, fill="green")

# 三角形
cvs.create_polygon(120, 100, 220, 140, 160, 200, fill="blue")

# 円
cvs.create_arc(300, 200, 400, 300, start=60, extent=90, fill="yellow")

# 楕円
cvs.create_oval(400, 200, 500, 300, fill="purple")

cvs.pack()
root.mainloop()
