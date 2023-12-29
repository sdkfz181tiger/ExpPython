# coding: utf-8

"""
スッキリわかる機械学習入門より
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
"""

import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree

FILE_CSV = "./test.csv"
FILE_PKL = "./test.pkl"

#==========
# Main

def main():
	print("main!!")

	# DataFrame
	df = pd.read_csv(FILE_CSV)
	
	# 先頭の3件
	print(df.head(3))

	# カラム一覧
	print(df.columns)

	# 行数
	print("行数:", df.shape[0])
	# 列数
	print("列数:", df.shape[1])

	# target列にあるデータ種類
	print("データ種類:", df["target"].unique())

	# 各データがいくつあるか
	print("x0:", df["x0"].size)
	print("x1:", df["x1"].size)
	print("x2:", df["x2"].size)
	print("x3:", df["x3"].size)

	# 各データに欠損数がいくつあるか
	print("欠損数x0:", df["x0"].isnull().sum())
	print("欠損数x1:", df["x1"].isnull().sum())
	print("欠損数x2:", df["x2"].isnull().sum())
	print("欠損数x3:", df["x3"].isnull().sum())

	# 欠損がある場合、各列の中央値で埋める
	colmedian = df.median()
	df = df.fillna(colmedian)

	# 欠損値の存在を確認
	print("isnull:", df.isnull().any(axis=0))

	# 特徴量xと正解データtに分割
	x = df[["x0", "x1", "x2", "x3"]]
	t = df["target"]

	# 訓練データとテストデータに分ける
	# 8割を訓練データ、2割をテストデータ
	x_train, x_test, y_train, y_test = train_test_split(
		x, t, test_size=0.2, random_state=0)

	print("x_train:", x_train.shape)
	print("x_test:", x_test.shape)

	# Model
	# max_depth: 決定木の深さ
	# random_state: 乱数のシード
	model = tree.DecisionTreeClassifier(
		max_depth=3, random_state=0)

	# 訓練データを使って訓練
	model.fit(x_train, y_train)

	# テストデータを使って評価
	print("Score:", model.score(x_test, y_test))

	# 新規データ
	new_data = [[1.56, 0.23, -1.1, 2.8]]
	new_result = model.predict(new_data)
	print(new_result)

if __name__ == "__main__":
	main()