# coding: utf-8

"""
ソートアルゴリズムをグラフで比較
InsertionSort vs MergeSort vs QuickSort vs HeapSort
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
	random.seed(0)# Seed

	# Title
	plt.title("Steps required for various Sort Algorithm")
	plt.xlabel("Total numbers")
	plt.ylabel("Steps required to Sort")
	xs = [i * 10 for i in range(30)]

	# Insertion Sort
	ys_insertion = [test_insertion(x) for x in xs]
	plt.plot(xs, ys_insertion, "r-", label="Insertion Sort")

	# Merge Sort
	ys_merge = [test_merge(x) for x in xs]
	plt.plot(xs, ys_merge, "g-", label="Merge Sort")

	# Quick Sort
	ys_quick = [test_quick(x) for x in xs]
	plt.plot(xs, ys_quick, "b-", label="Quick Sort")

	# Heap Sort
	ys_heap = [test_heap(x) for x in xs]
	plt.plot(xs, ys_heap, "y-", label="Heap Sort")

	plt.legend()
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

def test_heap(size):
	global steps; steps = 0# Reset
	if size <= 0: return 0# Important
	nums = [i for i in range(size)]# Numbers
	random.shuffle(nums)# Shuffle
	for i in reversed(range(len(nums)//2)):
		heap_heapify(nums, i)
	for i in reversed(range(len(nums))):
		nums[0], nums[i] = nums[i], nums[0]
		heap_sort(nums, 0, i-1)
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
	global steps; steps += 1
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
def quick_sort(nums, top, last):
	global steps; steps += 1
	p = quick_find(nums, top, last)
	if p < 0: return
	pivot = nums[p]# Pivot
	r = quick_arrange(nums, top, last, pivot)
	l = r - 1
	quick_sort(nums, top, l)
	quick_sort(nums, r, last)

def quick_find(nums, top, last):
	pivot = nums[top]# Pivot
	k = top + 1
	while k <= last:
		global steps; steps += 1
		if pivot == nums[k]: k += 1; continue
		if pivot < nums[k]: return k
		return top
	return -1

def quick_arrange(nums, top, last, pivot):
	while top <= last:
		global steps; steps += 1
		nums[top], nums[last] = nums[last], nums[top]# Swap
		if nums[top] < pivot: top += 1
		if pivot <= nums[last]: last -= 1
	return top

# Heap Sort
def heap_heapify(nums, i):
	global steps; steps += 1
	m = i# Max
	l = i * 2 + 1
	r = l + 1
	if l < len(nums) and nums[i] < nums[l]: m = l
	if r < len(nums) and nums[m] < nums[r]: m = r
	if m != i:
		nums[m], nums[i] = nums[i], nums[m]
		heap_heapify(nums, m)

def heap_sort(nums, top, last):
	global steps; steps += 1
	l = (top+1) * 2 - 1
	r = l + 1
	if r <= last:
		if nums[l] < nums[r]:
			if nums[top] < nums[r]:
				nums[top], nums[r] = nums[r], nums[top]
				heap_sort(nums, r, last)
		else:
			if nums[top] < nums[l]:
				nums[top], nums[l] = nums[l], nums[top]
				heap_sort(nums, l, last)
	else:
		if l <= last:
			if nums[top] < nums[l]:
				nums[top], nums[l] = nums[l], nums[top]
				heap_sort(nums, l, last)

if __name__ == "__main__":
	main()
