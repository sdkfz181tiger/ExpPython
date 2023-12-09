# coding: utf-8

"""
"プログラミング時代の数学との付き合い方"より
1, 相加相乗平均
"""

import numpy as np
import random
import matplotlib.pyplot as plt

# 相加相乗平均(項目数が2)
def ag_avg_2_test(a, b):
	print("相加平均:", arithmetic_avg := (a+b) / 2)
	print("相乗平均:", geometric_avg := (a*b)**(1/2))
	return geometric_avg <= arithmetic_avg

# 相加相乗平均(項目数がn)
def ag_avg_n_test(*arr):
	ta, tg = arr[0], arr[0]
	for n in arr[1:]:
		ta = ta + n# 相加
		tg = tg * n# 相乗
	# 平均
	print("相加平均:", arithmetic_avg := ta / len(arr))
	print("相乗平均:", geometric_avg := tg**(1/len(arr)))
	return geometric_avg <= arithmetic_avg

# Test1
# print(ag_avg_2_test(101, 3))
# print(ag_avg_n_test(17, 59, 103, 71, 68, 31))

# Test2: 0 ~ 100の範囲の数値を2 ~ 10個用意する
for i in range(100):
	total = random.randint(2, 10)# 用意する数
	arr = [random.randint(0, 100) for j in range(total)]
	print(ag_avg_n_test(*arr))