# coding: utf-8

"""
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
	$ python3 -m pip install matplotlib
"""

import pandas as pd
import pickle
import os.path
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

COL_X    = ["x0", "x1", "x2", "x3"]
COL_Y    = "target"
MY_CSV   = "ex2.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")
	
	df = pd.read_csv(MY_CSV)
	print(df.head(3)) # 先頭3行
	print(df.tail(3)) # 末端3行
	print(df.shape)   # 行列数

	# target列
	print(df["target"].unique()) # target列の種類
	print(df["target"].value_counts()) # target列の種類ごとの総数

	# 欠損値
	print(df.isnull()) # 欠損値を確認
	print("Before:", df.isnull().sum()) # 各列の欠損値の総数
	df = df.fillna(df.median(numeric_only=True)) # 中央値で穴埋め
	print("After:", df.isnull().sum()) # 各列の欠損値の総数

	# 80%を訓練データ、20%を検証データに
	x = df[COL_X] # 特徴量
	y = df[COL_Y] # 正解データ
	x_train, x_test, y_train, y_test = train_test_split(
		x, y, random_state=0, test_size=0.2)

	# モデルを準備
	model = tree.DecisionTreeClassifier(
		random_state=0, max_depth=3)
	model.fit(x_train, y_train)

	# 正解率
	print("Score:", model.score(x_test, y_test))

	# テスト
	x_test = pd.DataFrame([[1.56, 0.23, -1.1, -2.8]], columns=COL_X)
	print("Test:", model.predict(x_test))


if __name__ == "__main__":
	main()