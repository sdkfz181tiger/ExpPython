# coding: utf-8

"""
深層学習を使った学習_円の内側と外側
"""

from modules.SimpleDL import MyModel
from modules.Utility import is_inside, to_categorical, save_model
import numpy as np

"""
メイン処理
"""

# 教師データとなる座標を作成
points = 0.1
X = np.arange(-3, 3, points)
Y = np.arange(-3, 3, points)

x_train = [] # 座標
y_train = [] # 正解ラベル(0:内側, 1:外側)

# 正解データを生成する
cor_data = []
for x in X:
	for y in Y:
		x_train.append([x, y])
		if is_inside(x, y, 2):
			cor_data.append([0]) # 内側
		else:
			cor_data.append([1]) # 外側

# 座標から教師データを生成する
in_data = np.array(x_train)

# DNNのモデルを生成する
model = MyModel()
model.add(2, 6, "ReLU")
model.add(6, 4, "ReLU")
model.add(4, 2, "softmax")

model.summary()

# 正解データをonehot表現にする
truth_train = to_categorical(cor_data, 2)

# 学習には教師データの98%を使用する
total_train = int(len(in_data) * 0.98)
total_test = total_train + 1

# 学習の実行
history = model.fit(in_train=in_data[:total_train],
					cor_train=truth_train[:total_train],
					batch_size=40, epochs=100,
					loss="cross_entropy_error",
					lr=0.01,
					in_test=in_data[total_test:],
					cor_test=truth_train[total_test:])

# 学習モデルの保存(シリアライズ)
save_model("circle.model", model)
