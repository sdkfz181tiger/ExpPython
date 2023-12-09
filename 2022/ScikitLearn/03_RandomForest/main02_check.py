# coding: utf-8

"""
Wine学習データ
	https://archive.ics.uci.edu/ml/datasets/wine+quality
"""

import matplotlib.pyplot as plt
import pandas as pd

# RandomForest
print("Hello RandomForest!!")

# CSVファイル
csv_wine = pd.read_csv("./winequality-white.csv", sep=";", encoding="utf-8")

# 品質データごとにグループ分けして数を数える
count_wine = csv_wine.groupby("quality")["quality"].count()
count_wine.plot()# グラフに描画
print(count_wine)

# 画像に出力
plt.savefig("graph.png")
plt.show()