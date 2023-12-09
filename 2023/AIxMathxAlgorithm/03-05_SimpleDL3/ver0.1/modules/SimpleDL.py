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
		self.wb_width = 0.1 # 重みとバイアスの広がり具合
		# 重み行列を乱数で初期化
		self.w = self.wb_width * np.random.randn(self.in_node, self.out_node)
		# バイアス行列を乱数で初期化
		self.b = self.wb_width * np.random.randn(self.out_node)
		# 活性化関数を設定
		self.activation_func = activation_func

	# 順伝播
	def forward(self, x):
		self.x = x # 逆伝播の計算で使うので、変数に保存
		self.z = np.dot(x, self.w) + self.b # ノードの値を求める
		# 活性化関数を使って出力値を決定する
		if self.activation_func == "sigmoid":
			y = 1 / (1 + np.exp(-self.z)) # シグモイド関数
		elif self.activation_func == "ReLU":
			y = np.where(self.z <= 0, 0, self.z) # ReLU関数
		elif self.activation_func == "softmax":
			y = np.exp(self.z) / np.sum(np.exp(self.z), axis=1, keepdims=True) # ソフトマックス関数
		elif self.activation_func == "identity":
			y = self.z # 恒等関数の場合はそのまま
		return y

	# 逆伝播
	# y: 予測データ
	# 	softmax, identityの時は出力層とみなす
	# 	sigmoid, ReLUの時は中間層とみなす
	# grad_y: 正解データ
	# 	softmax, identityの時は出力層とみなす
	# 	sigmoid, ReLUの時は中間層とみなす
	def backward(self, y, grad_y):
		if self.activation_func == "sigmoid":
			sy = 1 / (1 + np.exp(-self.z)) # シグモイド関数の導関数
			delta = grad_y * sy * (1 - sy)
		elif self.activation_func == "ReLU":
			delta = grad_y * np.where(self.z <= 0, 0, 1) # ReLU関数
		elif self.activation_func == "softmax":
			delta = y - grad_y # ソフトマックス関数の場合は誤差
		elif self.activation_func == "identity":
			delta = y - grad_y # 恒等関数の場合は誤差

		self.grad_w = np.dot(self.x.T, delta) # 重み
		self.grad_b = np.sum(delta, axis=0)   # バイアス
		self.grad_x = np.dot(delta, self.w.T) # 逆伝播で前の層に渡す値
		return self.grad_x

	# 重みとバイアスを更新する関数
	# eta: 学習率
	def update(self, eta):
		self.w -= eta * self.grad_w
		self.b -= eta * self.grad_b

"""
MyModelクラス
"""

class MyModel:

	# コンストラクタ
	def __init__(self):
		print("MyModel")
		self.layers = []    # 層を保持するリスト
		self.batch_size = 0 # バッチサイズ
		self.epochs = 0     # 学習回数
		self.lr = 0.01      # 学習係数
		self.interval = 10  # 学習の経過を定期的に表示する為の値

	# 層を追加する
	def add(self, in_node, out_node, activation_func):
		layer = MyLayer(in_node, out_node, activation_func)
		self.layers.append(layer)

	# サマリー
	def summary(self):
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
	def backwards(self, y, x):
		for layer in self.layers[::-1]:
			x = layer.backward(y, x)
		return x

	# 誤差の計算(交差エントロピー誤差or二乗和誤差)
	def get_error(self, y, t, data_count):
		if self.loss == "cross_entropy_error":
			return -np.sum(t * np.log(y+1e-7)) / data_count
		elif self.loss == "squared_error":
			return 1.0 / 2.0 * np.sum(np.square(y-t)) / data_count

	# 重みとバイアスの更新
	def update_wb(self):
		for layer in self.layers:
			layer.update(self.lr)

	# 学習
	def fit(self, in_train, cor_train, batch_size,
			epochs, loss, lr, in_test, cor_test):

		self.batch_size = batch_size
		self.epochs = epochs
		self.lr = lr
		self.loss = loss

		total_train = in_train.shape[0] # 教師データの数
		total_test = in_test.shape[0]   # テストデータの数

		# 誤差の記録用
		train_error_x = []
		train_error_y = []
		test_error_x = []
		test_error_y = []

		# 学習と経過の記録
		total_batch = total_train // self.batch_size

		# 学習
		for i in range(self.epochs):

			index_random = np.arange(total_train)
			np.random.shuffle(index_random) # シャッフル
			print("Epoch:{}/{}".format(i+1 , self.epochs), end="")

			for j in range(total_batch):
				if j % 100 == 0: print(".", end="")

				# ミニバッチ
				index_mb = index_random[j * batch_size:(j+1) * batch_size]
				x = in_train[index_mb, :]
				t = cor_train[index_mb, :]

				# 順伝播と逆伝播
				y = self.forwards(x)
				self.backwards(y, t)

				# 重みとバイアスの更新
				self.update_wb()

			y = self.forwards(in_train)
			error_train = self.get_error(y, cor_train, total_train)
			y = self.forwards(in_test)
			error_test = self.get_error(y, cor_test, total_test)

			# 誤差の記録
			test_error_x.append(i)
			test_error_y.append(error_test)
			train_error_x.append(i)
			train_error_y.append(error_train)

			# 経過の表示
			print("Error_train:{:.5f} Error_test:{:.5f}".format(error_train, error_test))

		return {"train_error_x": train_error_x,
				"train_error_y": train_error_y,
				"test_error_x": test_error_x,
				"test_error_y": test_error_y}

	# 推論
	def predict(self, x):
		return self.forwards(x)