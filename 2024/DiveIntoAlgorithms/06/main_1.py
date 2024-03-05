# coding: utf-8

"""
処理時間を計測する
"""

#==========
# Main

import math, random
import matplotlib.pyplot as plt
import time

def main():
	print("main!!")

	# Numbers
	nums = [i for i in range(30)]

	# Shuffle
	random.seed(0)
	random.shuffle(nums)

	# Insertion sort
	t_start = time.time()
	arr, steps = insertion_sort(nums)
	t_end = time.time()
	t_diff = t_end - t_start
	print("arr:", arr, " steps:", steps, " diff:", t_diff)

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
