# coding: utf-8

"""
深層学習を使った学習と予測_XOR
"""

from modules.SimpleDL import MyModel
import numpy as np

# 入力データ
in_data = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])

# 正解データ
cor_data = np.array([0, 1, 1, 0])

epochs = 5000 # 学習回数
eta    = 0.1  # 学習率

# MyModelクラス
model = MyModel()

model.add(2, 2, "sigmoid")  # 入力ノードx2、出力ノードx2
model.add(2, 1, "identity") # 入力ノードx2、出力ノードx1
model.summry() # サマリー表示

# 学習の実行
model.fit(in_data, cor_data, epochs, eta)

# 学習後の評価
# XORデータと正解データ、予測結果を表示
for i, t in zip(in_data, cor_data):
	y = model.predict(i)
	print("入力:", i, "-> 正解:", t, "予測={:.5f}".format(y[0]))