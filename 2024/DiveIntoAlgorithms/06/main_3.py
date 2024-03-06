# coding: utf-8

"""
ソートアルゴリズムの処理回数をグラフにする
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
	xs = [i * 5 for i in range(50)]

	# Insertion Sort
	ys_insertion = [test_insertion(x) for x in xs]
	plt.plot(xs, ys_insertion)

	# Merge Sort
	ys_merge = [test_merge(x) for x in xs]
	plt.plot(xs, ys_merge)

	plt.show()

def test_insertion(size):
	# Numbers
	nums = [i for i in range(size)]
	# Shuffle
	random.seed(0)
	random.shuffle(nums)
	# Insertion sort
	steps = insertion_sort(nums)
	return steps

def test_merge(size):
	# Numbers
	nums = [i for i in range(size)]
	# Shuffle
	random.seed(0)
	random.shuffle(nums)
	# Merge sort
	steps = merge_sort(nums)
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
	return steps

# マージソート
def merge_sort(nums):
	if len(nums) < 2: return 0
	c = len(nums) // 2
	left = nums[:c]
	right = nums[c:]
	steps = 1
	steps += merge_sort(left)
	steps += merge_sort(right)
	steps += merge(left, right, nums)
	return steps

def merge(left, right, nums):
	l = r = steps = 0
	while l < len(left) and r < len(right):
		steps += 1
		if left[l] < right[r]:
			nums[l+r] = left[l]
			l += 1
		else:
			nums[l+r] = right[r]
			r += 1
	while l < len(left) or r < len(right):
		steps += 1
		if l < len(left):
			nums[l+r] = left[l]
			l += 1
		else:
			nums[l+r] = right[r]
			r += 1
	return steps

if __name__ == "__main__":
	main()
