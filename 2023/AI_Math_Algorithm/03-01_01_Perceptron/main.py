# coding: utf-8

"""
単純パーセプトロン
	AND, OR, NAND回路の学習
"""

# 活性化関数(ステップ関数)
def step(x):
	return 0 if x <= 0 else 1

# 単純パーセプトロン
def perceptron(x1, x2, w1, w2, b):
	return step(x1*w1 + x2*w2 + b)

# 更新 x1,t2:入力, y:結果, t:正解, w1,w2:重み, b:バイアス
def update(x1, x2, y, t, w1, w2, b):
	eta = 0.01 # 学習率

	# w1の更新量を計算
	update_w1 = (eta * (t-y)) * x1
	# w2の更新量を計算
	update_w2 = (eta * (t-y)) * x2
	# bの更新量を計算
	update_b = eta * (t-y)

	w1 += update_w1 # w1を更新
	w2 += update_w2 # w2を更新
	b  += update_b  # bを更新

	return w1, w2, b

# 学習
def learn(T):

	# 重みとバイアス
	w1 = 0.0
	w2 = 0.0
	b  = 0.0

	n = 0
	while True:
		for i in range(len(T)):
			y = perceptron(T[i][0], T[i][1], w1, w2, b)
			print("{},{},{},{:0<5},{:0<5},{:0<5},{},{}".format(
				i+1, T[i][0], T[i][1], w1, w2, b, y, T[i][2]))
			if y == T[i][2]:
				n += 1
			else:
				w1, w2, b = update(T[i][0], T[i][1], y, T[i][2], w1, w2, b)

		if 4 <= n: # 4回正解なら学習終了
			break
		else: # 不正解の場合は再学習
			n = 0

	# 学習結果
	print("w1: {}, w2: {}, b: {}".format(w1, w2, b))

	return w1, w2, b

#==========
# 学習処理(AND, OR, NAND回路の学習)

# 教師データ
# [x1(入力), x2(入力), y(出力=正解)]
T_AND  = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]]
T_OR   = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
T_NAND = [[0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 0]]

# 学習
w1, w2, b = learn(T_NAND)

# 検証(AND, OR, NAND回路の検証)
y = perceptron(0, 0, w1, w2, b)
print("0, 0 ->", y)
y = perceptron(1, 0, w1, w2, b)
print("1, 0 ->", y)
y = perceptron(0, 1, w1, w2, b)
print("0, 1 ->", y)
y = perceptron(1, 1, w1, w2, b)
print("1, 1 ->", y)