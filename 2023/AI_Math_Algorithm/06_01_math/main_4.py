# coding: utf-8

"""
"プログラミング時代の数学との付き合い方"より
グラフを描く
"""

import numpy as np
import random
import matplotlib.pyplot as plt

x = np.ar ange(-10, 10, 0.1)
y = x**2 + 2*x - 3

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x, y, c="blue")