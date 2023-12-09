# coding: utf-8

"""
ベクトルの描画
"""

import numpy as np
import matplotlib.pyplot as plt

# ベクトル
vec_a = np.array([4, 3])
vec_b = np.array([3, -2])

# グラフの準備
plt.axes().set_aspect("equal")

# ベクトルを矢印で描く
plt.quiver(0, 0, vec_a[0], vec_a[1], 
	angles="xy", scale_units="xy", color="red", scale=1)
plt.quiver(3, 1, vec_a[0], vec_a[1],
	angles="xy", scale_units="xy", color="red", scale=1)
plt.quiver(0, 0, vec_b[0], vec_b[1],
	angles="xy", scale_units="xy", color="blue", scale=1)

# グラフを描画
plt.xlim([0, 7]);
plt.ylim([-2, 4])
plt.grid()
plt.show()