# coding: utf-8

"""
転置ベクトル/行列の性質
"""

import numpy as np
import matplotlib.pyplot as plt

# 転置ベクトル
a = np.array([
	[1],
	[2],
	[3]])
print(a.T)

# 転置行列
A = np.array([
	[1, 2, 3],
	[4, 5, 6]])
print(A.T)

# 転置行列の性質

print("性質1: (A')' = A")
print((A.T).T)

print("性質2: (AB)' = (B'A')")

B = np.array([
	[-1, 0],
	[ 2, 3],
	[ 4, 6]])

print((A @ B).T) # (AB)'
print(B.T @ A.T) # (B'A')

print("性質3: (aC + bD)' = aC' + bD'")

C = np.array([
	[4, 5, 1],
	[2, 0, 8]])

D = np.array([
	[1, 0, 8],
	[5, 3, 4]])

print((3 * C + 5 * D).T)
print(3 * C.T + 5 * D.T)

print("性質4: 行列にその転置行列を掛けると正方行列になる")

print("4-1, mxn行列に転地したnxm行列を左から掛けると、mxmの行列になる")
print(A.T @ A)

print("4-2, mxn行列に転地したnxm行列を右から掛けると、nxnの行列になる")
print(A @ A.T)

print("性質5: ベクトルにその転置ベクトルを左から掛けると、各成分の二乗の総和になる")
print(a.T @ a)
