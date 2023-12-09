# coding: utf-8

"""
MyModelクラス
"""

from modules.MyLayer import MyLayer
import numpy as np

class MyModel:

	# コンストラクタ
	def __init__(self):
		print("MyModel")
		self.layers = []

	# 層を追加する
	def add(self, in_node, out_node, activation_func):
		layer = MyLayer(in_node, out_node, activation_func)
		self.layers.append(layer)

	# サマリー
	def summry(self):
		for layer in self.layers:
			print("==========")
			print("I:{}".format(layer.in_node))
			print("O:{}".format(layer.out_node))
			print("A:{}".format(layer.activation_func))

	# 順伝播
	def forwards(self, x):
		for layer in self.layers:
			x = layer.forward(x)
		return x

	# 逆伝播
	def backwards(self, t):
		for layer in self.layers[::-1]:
			t = layer.backward(t)

	# 誤差の計算
	def get_error(self, y, t):
		return 1.0 / 2.0 * np.sum(np.square(y-t))

	# 学習
	def fit(self, in_data, cor_data, epochs, eta):

		total_data = len(cor_data) # データ数

		# 学習
		for i in range(epochs):
			random_index = np.arange(total_data)
			np.random.shuffle(random_index)

			total_error = 0

			for index in random_index:

				# データを取り出す
				x = in_data[index:index+1] # 入力データ
				t = cor_data[index:index+1] # 正解データ

				# 順伝播
				y = self.forwards(x)

				# 逆伝播
				self.backwards(t)

				# 重みとバイアスの更新
				for layer in self.layers:
					layer.update(eta)

				if i % 100 == 0:
					y = y.reshape(-1) # 行列をベクトルに戻す
					total_error += self.get_error(y, t) # 誤算の計算

			if i % 100 == 0:
				print("==========")
				print("Epoch:{}/{}, Error:{}".format(str(i), str(epochs), total_error/total_data))

	# 予測
	def predict(self, in_data):
		return self.forwards(in_data)
