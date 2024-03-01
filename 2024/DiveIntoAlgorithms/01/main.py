# coding: utf-8

"""
Dive Into Algorithms
"""

#==========
# Main

import matplotlib.pyplot as plt

def main():
	print("main!!")

	# Title, Label
	plt.title("The Trajectory of Thrown Ball")
	plt.xlabel("Horizontal Position of Ball")
	plt.ylabel("Vertical Position of Ball")

	# 自由落下での放物線を描画(0.1m単位)
	xs0 = [x/100 for x in list(range(201))]
	ys0 = [trajectory(x) for x in xs0]

	# 着地点からの視線(x座標が0.1)
	xs1 = [0.1, 2]
	ys1 = [trajectory(0.1), 0]

	# 着地点からの視線(x座標が0.2)
	xs2 = [0.2, 2]
	ys2 = [trajectory(0.2), 0]

	# 着地点からの視線(x座標が0.3)
	xs3 = [0.3, 2]
	ys3 = [trajectory(0.3), 0]

	plt.plot(xs0, ys0, xs1, ys1, xs2, ys2, xs3, ys3)
	plt.show()

# 自由落下での放物線の関数
#	ここでは仮に、
# 		v1: x方向の初速 -> 0.9
# 		v2: y方向の初速 -> 10.0
#   	a:  重力 -> 10
#	として、次の2つの方程式から求める
# 		x = v1t
# 		y = v2t + (at^2)/2
def trajectory(x):
	return 10*x - 5*(x**2)

if __name__ == "__main__":
	main()
