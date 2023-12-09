# coding: utf-8

"""
重回帰分析(説明変数が複数)
"""

import numpy as np
import matplotlib.pyplot as plt

# 説明変数(身長, 足のサイズ)
x1_data = np.array([165,170,172,175,170,172,183,187,180,185])
x2_data = np.array([ 23, 24, 25, 27, 25, 24, 28, 29, 28, 29])
# 目的変数(体重)
y_data  = np.array([ 52, 60, 63, 65, 78, 70, 72, 85, 90, 94])

ones = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

X = np.array([ones, x1_data, x2_data]).T
theta = np.linalg.inv(X.T @ X) @ X.T @ y_data

print(f"θ0 = {theta[0]}")
print(f"θ1 = {theta[1]}")
print(f"θ2 = {theta[2]}")
print(f"y = {theta[0]} + {theta[1]} * x1 + {theta[2]} * x2")

# グラフ描画
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# データをプロット
ax.scatter3D(x1_data, x2_data, y_data, color="Blue")
ax.set_xlabel("x1(cm)")
ax.set_ylabel("x2(cm)")
ax.set_zlabel("y(kg)")

# x1_dataとx2_dataの範囲
mesh_size = 1
margin = 0.01
x1_min, x1_max = x1_data.min() - margin, x1_data.max() + margin
x2_min, x2_max = x2_data.min() - margin, x2_data.max() + margin
x1_range = np.arange(x1_min, x1_max, mesh_size)
x2_range = np.arange(x2_min, x2_max, mesh_size)
xx1, xx2 = np.meshgrid(x1_range, x2_range)

# 回帰平面
yy = (theta[0] + theta[1] * xx1 + theta[2] * xx2)
ax.plot_surface(xx1, xx2, yy, color="Red", alpha=0.5)
plt.show()