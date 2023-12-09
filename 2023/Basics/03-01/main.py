# coding: utf-8

"""
Command
バージョン確認
	python --version
インストール済みライブラリ一覧
	pip3 list
ライブラリインストール
	pip3 install numpy
"""

# 03-01: NumPyの使い方

import numpy as np
print("numpy:", np.__version__)

# 1次元ベクトルの内積
a = np.array([1, 2, 3])
print("a:", a)
b = np.array([1, 1, 4])
print("b:", b)
# 四則演算/内積
print("a+b:", a+b)
print("a-b:", a-b)
print("a*b:", a*b)
print("a/b:", a/b)
print("a dot b:", np.dot(a, b))

# 2次元ベクトルの内積
c = np.array([[1, 2], [3, 4]])
print("c:", c)
d = np.array([[3, 4], [1, 2]])
print("d:", d)
# 内積
print("c dot d:", np.dot(c, d))

# 3次元ベクトルの内積
e = np.array([[1, 2, 3], [0.1, 0.2, 0.3], [7, 8, 9]])
print("e:", e)
f = np.array([[0.1, 0.2, 0.3], [1, 2, 3], [7, 8, 9]])
print("f:", f)
# 内積
print("e dot f:", np.dot(f, e))

# 形状変換
g = np.arange(9).reshape((3, 3))
print("g:", g)
g = g.reshape((9, 1))
print("g:", g)

# 要素が0,1,未定義の配列
zeros = np.zeros((3, 4))
print("zeros:", zeros)
ones = np.ones((3, 4))
print("ones:", ones)
emps = np.empty((2, 3))
print("emps:", emps)


