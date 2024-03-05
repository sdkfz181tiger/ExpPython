# coding: utf-8

"""
処理回数をグラフにする
"""

#==========
# Main

import math, random
import matplotlib.pyplot as plt
import numpy as np

def main():
	print("main!!")

	# Title
	plt.title("Steps requred for Insertion Sort")
	plt.xlabel("Total numbers")
	plt.ylabel("Steps required to sort")

	# Points
	xs = [i * 2 for i in range(50)]
	ys = [test_sort(x) for x in xs]
	plt.plot(xs, ys)

	# 表示範囲を限定
	plt.gca().set_ylim([np.min(ys), np.max(ys)])

	# 指数関数的増加の曲線
	ys_exp = [math.exp(x) for x in xs]
	plt.plot(xs, ys_exp)

	# x^2の曲線
	ys_squared = [x**2 for x in xs]
	plt.plot(xs, ys_squared)

	# x^3の曲線
	ys_cubed = [x**3 for x in xs]
	plt.plot(xs, ys_cubed)

	# x^1.5の曲線
	ys_threehalves = [x**1.5 for x in xs]
	plt.plot(xs, ys_threehalves)

	plt.show()

def test_sort(size):
	# Numbers
	nums = [i for i in range(size)]
	# Shuffle
	random.seed(0)
	random.shuffle(nums)
	# Insertion sort
	arr, steps = insertion_sort(nums)
	#print("arr:", arr, " steps:", steps)
	return steps

# 挿入ソート
def insertion_sort(nums):
	arr = []
	steps = 0
	while 0 < len(nums):
		n = nums.pop(0)
		i = 0
		while i < len(arr):
			steps += 1
			if n < arr[i]: break
			i += 1
		arr.insert(i, n)
	return arr, steps

if __name__ == "__main__":
	main()
