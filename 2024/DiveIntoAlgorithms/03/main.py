# coding: utf-8

"""
チャップマンアルゴリズムによる弾道計算
"""

#==========
# Main

import math
import matplotlib.pyplot as plt
import numpy as np

def main():
	print("main!!")

	# Title, Label
	plt.title("The Trajectory of Thrown Ball")
	plt.xlabel("Horizontal Position of Ball")
	plt.ylabel("Vertical Position of Ball")

	# 自由落下での放物線を描画(0.1m単位)
	xs0 = [x/100 for x in list(range(201))]
	ys0 = [trajectory(x) for x in xs0]

	# 0.1秒間隔で点を打つ
	xs1 = [pos_x(t/10) for t in list(range(5))]
	ys1 = [pos_y(t/10) for t in list(range(5))]

	# 野手の位置(ほぼ着地位置である)
	xp = 1.99
	yp = 0.0

	# 0.1秒間隔でタンジェント値を求める
	tans = [(y-yp)/(xp-x) for x, y in zip(xs1, ys1)]
	#print(tans)

	# タンジェント値の速度
	diff_v = np.diff(tans)
	#print(diff_v)

	# タンジェント値の加速度
	diff_a = np.diff(diff_v)
	print(diff_a)

	# 加速度が+なら後ろに下がり、-なら前に進む指示を出す
	if 0.0 < diff_a[0]:
		print("後ろに下がってください!!")
	else:
		print("前に進んでください!!")

	#plt.plot(xs0, ys0, xs1, ys1)
	#plt.show()

# 自由落下での放物線の関数
#	ここでは仮に、
# 		vx: x方向の初速 -> 0.99
# 		vy: y方向の初速 -> 9.9
#   	gy: y方向の重力 -> -9.81
#	として、次の2つの方程式から求める
# 		x = vx*t
# 		y = vy*t + (gy*t^2)/2

vx = 0.99  # x方向の初速
vy = 9.9   # y方向の初速
gy = -9.81 # y方向の重力

def calc_x2y(x):
	return vy*(x/vx) + gy/2*(x/vx)**2

def pos_x(t):
	return vx*t

def pos_y(t):
	return vy*t + gy/2 * t**2

def calc_v(x, y, t):
	return math.sqrt(x**2 + y**2) / t

if __name__ == "__main__":
	main()
