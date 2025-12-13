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

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")

# カラーパレット
colors = [
    ["brown", "red", "orange", "gold"],
    ["darkgreen", "green", "limegreen", "lime"],
    ["navy", "blue", "skyblue", "cyan"]
]

s = H / len(colors)

rows = len(colors)
cols = len(colors[0])
for r in range(rows):
    for c in range(cols):
        x = c * s
        y = r * s
        color = colors[r][c]
        cvs.create_oval(x, y, x+s, y+s, fill=color, width=0)

cvs.pack()
root.mainloop()
