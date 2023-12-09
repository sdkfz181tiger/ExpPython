# coding: utf-8

"""
誤差逆伝播法
	XOR回路の学習
"""

import numpy as np

# 活性化関数(シグモイド関数)
def sigmoid(x):
	return 1 / (1 + np.exp(-x))

# 導関数(シグモイド関数)
def sigmoid_drv(x):
	return sigmoid(x) * (1 - sigmoid(x))

# 入力データ(4パターン)
x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])

# 教師データ(XOR回路正解データ)
t = np.array([[0], [1], [1], [0]])

epochs = 500000 # 学習回数
eta = 0.1       # 学習率

# 求める重みとバイアス
w11 = 0.1
w12 = 0.0
w21 = 0.1
w22 = 0.0
b1  = 0.0
b2  = 0.0
w1  = 0.0
w2  = 0.0

w = np.array([[w11, w12], [w21, w22]])
b = np.array([[b1, b2]])

w1w2 = np.array([[w1], [w2]])
b3 = np.array([[0.0]])

# 学習のループ
for epoch in range(epochs):
	# 1, 順伝播
	z = sigmoid(np.dot(x, w) + b)
	y = sigmoid(np.dot(z, w1w2) + b3)

	# 2, 誤差を計算(教師データとの差)
	error = t - y

	# 3, 誤差を使って更新量を計算
	# 	3-1, 中間層->出力層にある変数の更新量
	dy = error * sigmoid_drv(np.dot(z, w1w2) + b3)
	# 	3-2, 入力層->中間層にある変数の更新量
	dz = np.dot(dy, w1w2.T) * sigmoid_drv(np.dot(x, w) + b)

	# 4, 各変数の値の更新
	w1w2 += np.dot(z.T, dy) * eta
	b3 += np.sum(dy, axis=0, keepdims=True) * eta
	w += np.dot(x.T, dz) * eta
	b += np.sum(dz, axis=0, keepdims=True) * eta

	# 学習状況の確認
	if epoch % 1000 == 0:
		print("epoch:", epoch)
		for i in range(len(error)):
			print("   in:{} -> out:{}, t:{}, error:{}".format(x[i], y[i], t[i], error[i]))

print("== Finished ==")

# 結果を確認
print("w11:{}".format(w[0][0]))
print("w12:{}".format(w[0][1]))
print("w21:{}".format(w[1][0]))
print("w22:{}".format(w[1][1]))

print("b1:{}".format(b[0][0]))
print("b2:{}".format(b[0][1]))

print("w1:{}".format(w1w2[0][0]))
print("w2:{}".format(w1w2[1][0]))
print("b3:{}".format(b3[0][0]))
