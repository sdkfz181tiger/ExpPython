# coding: utf-8

"""
誤差逆伝播法
	XOR回路の検証
"""

import numpy as np

# 学習した結果の値
w11 = 7.104769271865116
w12 = 5.312102266464121
w21 = 7.104769271865116
w22 = 5.312102266464121
b1  = -3.2369981943545425
b2  = -8.137731083422592
w1  = 11.781068368474742
w2  = -12.4464312925285
b3  = -5.557094821829347

# 活性化関数(ステップ関数)
def step(x):
	return (0<x).astype(np.int64)

# 多層パーセプトロン(XOR回路)
def multi_perceptron(x):
	w = np.array([[w11, w12], [w21, w22]])
	b = np.array([b1, b2])
	w1w2 = np.array([w1, w2])
	z = step(np.dot(x, w) + b)
	return step(np.dot(z, w1w2) + np.array([b3]))

print("== Checking ==")

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