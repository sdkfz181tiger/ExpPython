# coding: utf-8

# 03-01: Matplotlibの使い方

import numpy as np
import matplotlib.pyplot as plt
print("numpy:", np.__version__)

# 1次関数
# plt.plot([1, 2, 3, 4])
# plt.plot([4, 3, 2, 1])

# 折れ線グラフ
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([10, 15, 35, 45, 30])
# plt.plot(x, y)

# リスト内包表記
# volume = 30
# x = np.arange(volume)
# y = [i + np.random.randn(1) for i in x]
# plt.plot(x, y)

# 近似直線を求める。o:点、-:線
# a, b = np.polyfit(x, y, 1)
# plt.plot(x, y, "o", np.arange(volume), a*np.arange(volume)+b, "-")

# sin, cos, arctan
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))
# plt.plot(x, np.arctan(x))

# 散布図
# x = np.random.rand(100)
# y = np.random.rand(100)
# plt.scatter(x, y, s=600, c="orange", 
# 	alpha=0.5, linewidth=1, edgecolors="red")

plt.show()