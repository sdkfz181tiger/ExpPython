# coding: utf-8

"""
勾配上昇法を使った最適化
"""

#==========
# Main

import math, random
import matplotlib.pyplot as plt

def main():
	print("main!!")

	# 税率と税収
	plt.title("Tax Rates and Revenue")
	plt.xlabel("Tax Rate")
	plt.ylabel("Revenue")

	# 二次曲線を描画
	xs = [x/1000 for x in range(1001)]
	ys = [revenue(x) for x in xs]
	plt.plot(xs, ys)

	# 初期状態
	current_rate = 0.7
	plt.plot(current_rate, revenue(current_rate), "ro")
	print(current_rate, revenue_delivative(current_rate))

	# 勾配上昇法
	threshould = 0.0001
	iterations = 0
	iterations_max = 10000

	# 導関数の傾きがthreshould以下になるまで繰り返す
	step_size = 0.001
	while True:
		diff = step_size * revenue_delivative(current_rate)
		current_rate = current_rate + diff
		if abs(diff) < threshould: break
		if iterations_max < iterations: break
		iterations += 1

	# 結果
	plt.plot(current_rate, revenue(current_rate), "ro")
	print(current_rate, revenue_delivative(current_rate))

	plt.show()

# 二次関数
def revenue(tax):
	return 100 * (math.log(tax+1) - (tax-0.2)**2 + 0.04)

# 導関数
def revenue_delivative(tax):
	return 100 * (1/(tax+1) - 2*(tax-0.2))

if __name__ == "__main__":
	main()
