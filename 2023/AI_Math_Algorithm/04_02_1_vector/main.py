# coding: utf-8

"""
ベクトルを描く
"""

import numpy as np
import matplotlib.pyplot as plt

vec_a = np.array([4, 3])
vec_b = np.array([3, -2])

plt.axes().set_aspect("equal")

plt.quiver(0, 0, vec_a[0], vec_a[1], angles="xy", scale_units="xy", color="red", scale=1)
plt.quiver(3, 1, vec_a[0], vec_a[1], angles="xy", scale_units="xy", color="red", scale=1)
plt.quiver(0, 0, vec_b[0], vec_b[1], angles="xy", scale_units="xy", color="blue", scale=1)

plt.xlim([0, 7])
plt.ylim([-2, 4])
plt.grid()
plt.show()