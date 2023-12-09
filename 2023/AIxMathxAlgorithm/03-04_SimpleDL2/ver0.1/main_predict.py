# coding: utf-8

"""
深層学習を使った予測_円の内側と外側
"""

from modules.SimpleDL import MyModel
from modules.Utility import load_model
import numpy as np

from matplotlib import patches
import matplotlib.pyplot as plt

"""
メイン処理
"""

# テスト用座標の作成
X = np.random.uniform(-5.0, 5.0, 200)
Y = np.random.uniform(-5.0, 5.0, 200)

# 座標データを作る
xy_data = []
for x, y in zip(X, Y):
	xy_data.append([x, y])

# 座標データからテストデータを作る
in_data = np.array(xy_data)

# 学習済モデルの読込(デシリアライズ)
model = load_model("circle.model")

# 読込んだモデルにテストデータを与えて予測
pred = model.predict(in_data)

# 予測結果を円の内側/外側に分ける
inside_x = []
inside_y = []
outside_x = []
outside_y = []

for p, xy, in zip(pred, in_data):
	# 0: 内側, 1: 外側
	if np.argmax(p) == 0:
		inside_x.append(xy[0])
		inside_y.append(xy[1])
	else:
		outside_x.append(xy[0])
		outside_y.append(xy[1])

# 分類結果をプロット
patch = patches.Circle(xy=(0, 0), radius=2, alpha=0.3)
fig, ax = plt.subplots(figsize=(6, 6))

ax.add_patch(patch)
ax.autoscale()
ax.grid()
ax.set_xticks(range(-5, 6))
ax.set_yticks(range(-5, 6))

plt.scatter(inside_x, inside_y, marker="o", c="blue")
plt.scatter(outside_x, outside_y, marker="x", c="red")
plt.show()
