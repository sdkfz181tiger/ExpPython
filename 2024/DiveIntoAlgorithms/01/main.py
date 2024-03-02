# coding: utf-8

"""
チャップマンアルゴリズムによる弾道計算
"""

#==========
# Main

import math
import matplotlib.pyplot as plt
import numpy as np

# 打者の弾の初速と重力
vx = 0.99  # x方向の初速
vy = 9.9   # y方向の初速
gy = -9.81 # y方向の重力

# 野手の位置(2.0がほぼ着地位置である)
px = 1.9
py = 0.0

def main():
	print("main!!")

	# Title, Label
	plt.title("The Trajectory of Thrown Ball")
	plt.xlabel("Horizontal Position of Ball")
	plt.ylabel("Vertical Position of Ball")

	# 打者の弾道の軌跡(解答)
	xs0 = [x/100 for x in list(range(201))]
	ys0 = [calc_x2y(x) for x in xs0]
	plt.plot(xs0, ys0)

	# 0.1秒間隔で4つだけ弾道計算(予測)
	xs1 = [pos_x(t/10) for t in list(range(4))]
	ys1 = [pos_y(t/10) for t in list(range(4))]
	plt.plot(xs1, ys1)

	# 0.1秒間隔でタンジェント値を求める
	tans = [(y-py)/(px-x) for x, y in zip(xs1, ys1)]

	# タンジェント値の速度
	diff_v = np.diff(tans)

	# タンジェント値の加速度
	diff_a = np.diff(diff_v)

	# 加速度が+なら後ろに下がり、-なら前に進む指示を出す
	if 0.0 < diff_a[0]:
		print("後ろに下がってください!!")
	else:
		print("前に進んでください!!")

	# 野手の位置
	plt.plot(px, py, "ro")
	plt.show()

# 自由落下での放物線の関数
#	ここでは仮に、
# 		vx: x方向の初速 -> 0.99
# 		vy: y方向の初速 -> 9.9
#   	gy: y方向の重力 -> -9.81
#	として、次の2つの方程式から求める
# 		x = vx*t
# 		y = vy*t + (gy*t^2)/2

# 打者の弾道の軌跡を計算する関数
def calc_x2y(x):
	return vy*(x/vx) + gy/2*(x/vx)**2

# 経過時間からx座標を求める関数
def pos_x(t):
	return vx*t

# 経過時間からy座標を求める関数
def pos_y(t):
	return vy*t + gy/2 * t**2

if __name__ == "__main__":
	main()
