# coding: utf-8

"""
単回帰分析(説明変数が1つ)
polyfitで回帰式(2次式)の回帰係数を求める
"""

import numpy as np
import matplotlib.pyplot as plt

# 10人分の身長、足のサイズと体重のデータ

# 説明変数(身長, 足のサイズ)
x1_data = np.array([165,170,172,175,170,172,183,187,180,185])
# x2_data = np.array([ 23, 24, 25, 27, 25, 24, 28, 29, 28, 29])
# 目的変数(体重)
y_data  = np.array([ 52, 60, 63, 65, 78, 70, 72, 85, 90, 94])

# polyfitで回帰式の回帰係数を求める
a, b, c = np.polyfit(x1_data, y_data, 2)
print("回帰式: a =", a, "b =", b, "c =", c)

# グラフを描画
margin = 10
x_min, x_max = x1_data.min() - margin, x1_data.max() + margin

# 回帰式(2次式)
X1 = np.arange(x_min, x_max, 2)
Y  = a * X1**2 + b * X1 + c

plt.figure(dpi=200)
plt.scatter(x1_data, y_data, c="Blue")
plt.plot(X1, Y, c="Red")
plt.xlabel("x: height(cm)")
plt.ylabel("y: weight(kg)")
plt.show()