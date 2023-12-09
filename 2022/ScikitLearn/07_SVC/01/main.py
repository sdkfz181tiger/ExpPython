# coding: utf-8

"""
手書き数字データ
	https://archive.ics.uci.edu/ml/datasets/optical+recognition+of+handwritten+digits
"""

import matplotlib.pyplot as plt
from sklearn import datasets

# SVC
print("Hello SVC!!")

# 手書き数字を出力
digits = datasets.load_digits()
for i in range(15):
	plt.subplot(3, 5, i+1)# 3x5に複数のデータをプロット
	plt.axis("off")
	plt.title(str(digits.target[i]))
	plt.imshow(digits.images[i], cmap="gray")

plt.show()
