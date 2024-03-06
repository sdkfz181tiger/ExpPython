# coding: utf-8

"""
ソートアルゴリズムの処理回数を比較
InsertionSort vs MergeSort vs QuickSort
"""

#==========
# Main

import math, random
import matplotlib.pyplot as plt
import numpy as np

steps = 0# Steps

def main():
	print("main!!")
	random.seed(0)# Seed

	# Title
	plt.title("Steps required for various Sort Algorithm")
	plt.xlabel("Total numbers")
	plt.ylabel("Steps required to Sort")
	xs = [i * 5 for i in range(30)]

	# Insertion Sort
	ys_insertion = [test_insertion(x) for x in xs]
	plt.plot(xs, ys_insertion)

	# Merge Sort
	ys_merge = [test_merge(x) for x in xs]
	plt.plot(xs, ys_merge)

	# Quick Sort
	ys_quick = [test_quick(x) for x in xs]
	plt.plot(xs, ys_quick)

	plt.show()

def test_insertion(size):
	global steps; steps = 0# Reset
	if size <= 0: return 0# Important
	nums = [i for i in range(size)]# Numbers
	random.shuffle(nums)# Shuffle
	insertion_sort(nums)# Insertion sort
	return steps

def test_merge(size):
	global steps; steps = 0# Reset
	if size <= 0: return 0# Important
	nums = [i for i in range(size)]# Numbers
	random.shuffle(nums)# Shuffle
	merge_sort(nums)# Merge sort
	return steps

def test_quick(size):
	global steps; steps = 0# Reset
	if size <= 0: return 0# Important
	nums = [i for i in range(size)]# Numbers
	random.shuffle(nums)# Shuffle
	quick_sort(nums, 0, len(nums)-1)# Quick Sort
	return steps

# Insertion Sort
def insertion_sort(nums):
	arr = []
	while 0 < len(nums):
		n = nums.pop(0)
		i = 0
		while i < len(arr):
			global steps; steps += 1
			if n < arr[i]: break
			i += 1
		arr.insert(i, n)

# Merge Sort
def merge_sort(nums):
	if len(nums) < 2: return 0
	c = len(nums) // 2
	left = nums[:c]
	right = nums[c:]
	merge_sort(left)
	merge_sort(right)
	merge(left, right, nums)

def merge(left, right, nums):
	global steps
	l = r = 0
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

# Quick Sort
def quick_sort(nums, i_min, i_max):
	p = quick_find(nums, i_min, i_max)
	if p < 0: return
	pivot = nums[p]# Pivot
	r = quick_arrange(nums, i_min, i_max, pivot)
	l = r - 1
	quick_sort(nums, i_min, l)
	quick_sort(nums, r, i_max)

def quick_find(nums, i_min, i_max):
	pivot = nums[i_min]# Pivot
	k = i_min + 1
	while k <= i_max:
		global steps; steps += 1
		if pivot == nums[k]: k += 1; continue
		if pivot < nums[k]: return k
		return i_min
	return -1

def quick_arrange(nums, i_min, i_max, pivot):
	while i_min <= i_max:
		global steps; steps += 1
		nums[i_min], nums[i_max] = nums[i_max], nums[i_min]# Swap
		if nums[i_min] < pivot: i_min += 1
		if pivot <= nums[i_max]: i_max -= 1
	return i_min

if __name__ == "__main__":
	main()
