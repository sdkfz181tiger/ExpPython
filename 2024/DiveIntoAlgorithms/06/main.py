# coding: utf-8

"""
ソートアルゴリズムにおける処理回数を比較
"""

#==========
# Main

import math, random
import matplotlib.pyplot as plt

def main():
	print("main!!")

	# Insertion sort
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	new = insertion_sort(arr)
	print("new:", new)

# 挿入ソート
def insertion_sort(arr):

	new = []
	while 0 < len(arr):
		new.insert(0, arr.pop(0))
	return new

def insert_num(arr, num):
	return arr.insert(num)

if __name__ == "__main__":
	main()
