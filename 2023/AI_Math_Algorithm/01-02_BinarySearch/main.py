# coding: utf-8

"""
AIx数学xアルゴリズム
"""

import random

n_min = 1
n_max = 1000
data = [random.randint(n_min, n_max) for n in range(n_max)]
data.sort()

key = 213

def binary_search(data, key):
	l = 0
	r = len(data) - 1

	while l <= r:
		c = (l + r) // 2
		if(data[c] == key): 
			return c
		elif data[c] < key:
			l = c + 1
		else:
			r = c - 1
	return -1

result = binary_search(data, key)

if(result == -1):
	print("データはありません")
else:
	print("データをみつけました", result)


