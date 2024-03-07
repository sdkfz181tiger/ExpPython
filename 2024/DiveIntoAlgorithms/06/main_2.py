# coding: utf-8

"""
処理回数のグラフ
"""

#==========
# Main

import math, random
import matplotlib.pyplot as plt
import numpy as np

# やりすぎるとコードの可読性が下がるのでグローバルにしておく
steps = 0# Steps

def main():
	print("main!!")

	# Title
	plt.title("Steps requred for Insertion Sort")
	plt.xlabel("Total numbers")
	plt.ylabel("Steps required to sort")

	# Insertion Sort
	xs = [i * 2 for i in range(50)]
	ys = [test_insertion(x) for x in xs]
	plt.plot(xs, ys, "r-", label="Insertion Sort")

	# 表示範囲を限定
	plt.gca().set_ylim([np.min(ys), np.max(ys)])

	# 指数関数的増加の曲線
	ys = [math.exp(x) for x in xs]
	plt.plot(xs, ys, "g-", label="Exp")

	# x^2の曲線
	ys = [x**2 for x in xs]
	plt.plot(xs, ys, "b-", label="Squared")

	# x^3の曲線
	ys = [x**3 for x in xs]
	plt.plot(xs, ys, "c-", label="Cubed")

	# x^1.5の曲線
	ys = [x**1.5 for x in xs]
	plt.plot(xs, ys, "m-", label="ThreeHalves")

	plt.legend()
	plt.show()

def test_insertion(size):
	global steps; steps = 0# Reset
	if size <= 0: return 0# Important
	nums = [i for i in range(size)]# Numbers
	random.shuffle(nums)# Shuffle
	insertion_sort(nums)# Insertion sort
	return steps

# Insertion Sort
def insertion_sort(nums):
	global steps
	arr = []
	while 0 < len(nums):
		n = nums.pop(0)
		i = 0
		while i < len(arr):
			steps += 1
			if n < arr[i]: break
			i += 1
		arr.insert(i, n)

if __name__ == "__main__":
	main()
