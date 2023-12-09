# coding: utf-8

"""
AIx数学xアルゴリズム
"""

data = [9, 6, 8, 2, 5]
key = 5

def linear_search(data, key):
	for i in range(len(data)):
		if data[i] == key: return i
	return -1

result = linear_search(data, key)
if result == -1:
	print("データはありません")
else:
	print("データをみつけました", result)