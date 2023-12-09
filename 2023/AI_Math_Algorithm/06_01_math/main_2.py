# coding: utf-8

"""
"プログラミング時代の数学との付き合い方"より
2, n乗の差の因数分解
"""

import numpy as np
import random
import matplotlib.pyplot as plt

# (a^n - b^n)を因数分解した式を表す関数
# ex: n=3の時
# 	(a^3 - b^3) = (a-b)(a^2*b^0 + a^1*b^1 + a^0*b^2)
def factorization_n(a, b, n):
	f = 0
	for i in range(1, n+1):
		ab = a**(n-i) * b**(i-1)
		f = f + ab
	return (a - b) * f

# Test
print(factorization_n(3, 2, 3))# 27-8  =19
print(factorization_n(4, 3, 3))# 64-27 =37
print(factorization_n(5, 4, 3))# 125-64=61
