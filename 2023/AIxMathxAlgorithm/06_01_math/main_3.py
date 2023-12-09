# coding: utf-8

"""
"プログラミング時代の数学との付き合い方"より
3, 自然数の2乗の総和
"""

import numpy as np
import random
import matplotlib.pyplot as plt

# 2乗の総和を計算する関数(計算する)
def sum_of_squares1(n):
	return sum(map(lambda x: x**2, range(1, n+1)))

# 2乗の総和を計算する関数(公式を使う)
def sum_of_squares2(n):
	return (1/6) * n * (n+1) * (2*n+1)

# Test1
print(sum_of_squares1(10))# 385
print(sum_of_squares2(10))# 385

# 自然数の2乗の逆数の総和を計算する関数(バーゼル問題)
def basel_problem(n):
	return sum(map(lambda x: 1/x**2, range(1, n+1)))

# Test2: 3.14の2乗を6で割った数に近づく(ほんまや!!)
print(basel_problem(1000))# 1.643...
print((3.14**2) / 6)# 1.643...