# coding: utf-8

"""
TensorFlow学習

TensorFlow, Keras:(相性に注意)
	pip install --upgrade tensorflow-cpu==2.9.2
	pip install --upgrade keras==2.9.0

epoch: 繰り返し回数
accuracy: 正確さ
loss: 損失
"""

import pickle, random
import numpy as np
import tensorflow as tf

# TensorFlow
print("Hello TensorFlow!!")

FILE_PICKLE = "./janken.pickle"# 学習用データ
FILE_MODEL = "./janken.model"# 学習済データ

# ジャンケンの手
hands = {"Gu":0, "Ch":1, "Pa":2}
results = ["Even", "Lose", "Win"]

def create_pickle():
	print("create_pickle")

	# ランダムで手を選ぶ
	hand = lambda: random.randint(0, 2)

	# ジャンケンの公式
	judge = lambda a, b: (a-b+3) % 3

	x = []
	y = []
	for i in range(3000):
		a = hand()
		b = hand()
		result = judge(a, b)
		x.append([a, b])# 手
		y.append(result)# 結果

	# データを学習用とテスト用に分割
	x_train = x[0:2000]
	y_train = y[0:2000]
	x_test = x[2000:]
	y_test = y[2000:]

	# データの保存
	data = [[x_train, y_train], [x_test, y_test]]
	pickle.dump(data, open(FILE_PICKLE, "wb"))

def create_model():
	print("create_model")

	# データの読込
	data = pickle.load(open(FILE_PICKLE, "rb"))
	(x_train, y_train), (x_test, y_test) = data

	# 学習モデルを構築
	clf = tf.keras.models.Sequential([
		tf.keras.layers.Dense(30, activation="relu", input_dim=2),
		tf.keras.layers.Dense(3, activation="softmax")
	])
	clf.compile(
		optimizer="adam", 
		loss="sparse_categorical_crossentropy",
		metrics=["accuracy"])

	# 学習モデルの概要を表示
	clf.summary()

	# 学習モデルを画像に出力
	tf.keras.utils.plot_model(clf, to_file="janken-model.png")

	# 学習
	clf.fit(x_train, y_train, epochs=20)

	# 評価
	clf.evaluate(x_test, y_test, verbose=2)

	# 保存
	pickle.dump(clf, open(FILE_MODEL, "wb"))

def check_janken():

	# 学習済モデル
	clf = pickle.load(open(FILE_MODEL, "rb"))

	def janken(a, b):
		x = np.array([[hands[a], hands[b]]])
		y = clf.predict(x)
		print("y:", y)
		print(a, b, "->", results[y[0].argmax()])

	janken("Gu", "Gu")
	janken("Ch", "Pa")
	janken("Pa", "Ch")

#==========
# 学習用データを作る
create_pickle()

#==========
# 学習済データを作る
create_model()

#==========
# ジャンケン判定
check_janken()