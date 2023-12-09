# coding: utf-8

"""
回転行列を利用した回転
"""

import numpy as np
import tkinter

# Window
root = tkinter.Tk()
root.title("Rotate")
root.geometry("200x200")

# Canvas
cv = tkinter.Canvas(root, width=200, height=200)
cv.place(x=0, y=0)

# 4つの頂点
p1 = np.array([50, 50])
p2 = np.array([150, 50])
p3 = np.array([150, 150])
p4 = np.array([50, 150])

# 回転の中心
c = np.array([100, 100])

# 角度
angle = 0

# 更新処理
def update():
	global angle

	# 回転行列
	r = np.array([
		[np.cos(angle), -np.sin(angle)],
		[np.sin(angle), np.cos(angle)]])

	# 4つの頂点
	r1 = r @ (p1 - c) + c
	r2 = r @ (p2 - c) + c
	r3 = r @ (p3 - c) + c
	r4 = r @ (p4 - c) + c

	# 正方形を描画
	cv.delete("all") # 画面を消去
	cv.create_line(
		r1[0], r1[1], r2[0], r2[1], r3[0], r3[1],
		r4[0], r4[1], r1[0], r1[1], fill="#00ff00")

	angle = angle + 0.05
	root.after(33, update) # 更新処理

update()
root.mainloop()



