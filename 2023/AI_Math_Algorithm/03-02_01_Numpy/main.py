# coding: utf-8

"""
多層パーセプトロン
	NumpyでXOR回路を使う
"""

import numpy as np

# 活性化関数(ステップ関数)
def step(x):
	return (0<x).astype(np.int64)

# 多層パーセプトロン(XOR回路)
def multi_perceptron(x):

	# 行列演算(NAND, OR)
	w = np.array([
			[-0.01, 0.01], 
			[-0.02, 0.01]])
	b = np.array([0.03, 0.0])
	z = step(np.dot(x, w) + b)

	# 行列演算(AND)
	w = np.array([0.01, 0.02])
	b = np.array([-0.02])
	return step(np.dot(z, w) + b)

# 多層パーセプトロン(単純パーセプトロンの学習済データを利用)
# def multi_perceptron(x1, x2):
# 	z1 = perceptron(x1, x2, -0.01, -0.02, 0.03)# NAND
# 	z2 = perceptron(x1, x2, 0.01, 0.01, 0.0)# OR
# 	return perceptron(z1, z2, 0.01, 0.02, -0.02)# AND

#==========
# 検証

x = np.array([0, 0])
y = multi_perceptron(x)
print(x, "->", y)

x = np.array([1, 0])
y = multi_perceptron(x)
print(x, "->", y)

x = np.array([0, 1])
y = multi_perceptron(x)
print(x, "->", y)

x = np.array([1, 1])
y = multi_perceptron(x)
print(x, "->", y)
