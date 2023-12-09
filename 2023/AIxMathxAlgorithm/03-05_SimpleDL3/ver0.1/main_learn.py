# coding: utf-8

"""
深層学習を使った学習_MNIST
"""

from modules.SimpleDL import MyModel
from modules.Utility import to_categorical, save_model

import numpy as np
import gzip

"""
メイン処理
"""

# MNISTのデータセット読込
with gzip.open("./mnist/train-images-idx3-ubyte.gz", "rb") as f:
	train_data = np.frombuffer(f.read(), np.uint8, offset=16)

with gzip.open("./mnist/train-labels-idx1-ubyte.gz", "rb") as f:
	train_truth = np.frombuffer(f.read(), np.uint8, offset=8)

with gzip.open("./mnist/t10k-images-idx3-ubyte.gz", "rb") as f:
	validation_data = np.frombuffer(f.read(), np.uint8, offset=16)

with gzip.open("./mnist/t10k-labels-idx1-ubyte.gz", "rb") as f:
	validation_truth = np.frombuffer(f.read(), np.uint8, offset=8)

# データ前処理

# データ形状を変更
train_data = train_data.reshape(60000, -1)
validation_data = validation_data.reshape(10000, -1)

# データ正規化(画像ピクセルデータを、0~255の範囲->0~1の範囲に正規化)
train_data = train_data / 255.0
validation_data = validation_data / 255.0

# 教師データの正解ラベルをohehot表現に変更
train_truth = to_categorical(train_truth, 10)
# 検証データの正解ラベルをohehot表現に変更
validation_truth = to_categorical(validation_truth, 10)

# DNN
model = MyModel()
model.add(784, 512, "ReLU")   # ReLU関数
model.add(512, 10, "softmax") # softmax関数

model.summary() # サマリー

history = model.fit(
	in_train=train_data,       # 教師データの画像
	cor_train=train_truth,     # 教師データの正解ラベル
	batch_size=30, epochs=30,  # バッチサイズ、エポック数
	loss="cross_entropy_error",# 損失関数の指定
	lr=0.01,                   # 学習率
	in_test=validation_data,   # 検証データの画像
	cor_test=validation_truth) # 検証データのラベル

# モデルの保存(シリアライズ)
save_model("mnist.model", model)
