# coding: utf-8

import numpy as np

"""
MyLayerクラス
"""

class MyLayer:

	# コンストラクタ
	# in_node: 入力ノード数
	# out_node: 出力ノード数
	# activation_func: 活性化関数
	def __init__(self, in_node, out_node, activation_func="sigmoid"):
		print("MyLayer")
		self.in_node  = in_node  # 入力ノード数
		self.out_node = out_node # 出力ノード数
		self.w = np.random.randn(self.in_node, self.out_node) # 重み行列を乱数で初期化
		self.b = np.random.randn(self.out_node) # バイアス行列を乱数で初期化
		self.activation_func = activation_func # 活性化関数を設定

	# 順伝播
	def forward(self, x):
		self.x = x # 逆伝播の計算で使うので、変数に保存
		self.z = np.dot(x, self.w) + self.b # ノードの値を求める
		# 活性化関数を使って出力値を決定する
		if self.activation_func == "sigmoid":
			self.y = self.sigmoid(self.z)
		elif self.activation_func == "identity":
			self.y = self.z # 恒等関数の場合はそのまま
		return self.y

	# 逆伝播
	def backward(self, t):
		if self.activation_func == "sigmoid":
			delta = self.sigmoid_drv(self.z) * t # シグモイド関数の導関数
		elif self.activation_func == "identity":
			delta = self.y - t # 恒等関数の場合は誤差

		self.grad_w = np.dot(self.x.T, delta) # 重みの勾配
		self.grad_b = np.sum(delta, axis=0)   # バイアスの勾配
		self.grad_x = np.dot(delta, self.w.T) # 逆伝播で前の層に渡す値

		return self.grad_x

	# 重みとバイアスを更新する関数
	# eta: 学習率
	def update(self, eta):
		self.w -= eta * self.grad_w
		self.b -= eta * self.grad_b

	# シグモイド関数
	def sigmoid(self, x):
		return 1 / (1 + np.exp(-x))

	# シグモイド関数の導関数
	def sigmoid_drv(self, x):
		return self.sigmoid(x) * (1-self.sigmoid(x))

"""
MyModelクラス
"""

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

	# 誤差の計算(二乗和誤差)
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

