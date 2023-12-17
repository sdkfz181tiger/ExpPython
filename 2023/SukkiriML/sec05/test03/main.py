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

FILE_CSV = "./ex2.csv"
FILE_PKL = "./ex2.pkl"

#==========
# Data

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

	

	"""
	# Fill lost data with average point
	mean = df.mean(numeric_only=True)# 欠損値を除外して計算
	df = df.fillna(mean)

	# 説明変数xと目的変数tに分割
	x = df[["GakuLen", "GakuWidth", "KabeLen", "KabeWidth"]]
	t = df["Type"]
	print("説明変数x", x)
	print("目的変数t", t)

	# Model
	# max_depth: 決定木の深さ
	# random_state: 乱数のシード
	model = tree.DecisionTreeClassifier(
		max_depth=2, random_state=0)

	# テストデータと訓練データに分ける
	# 3割をテストデータ、7割を訓練データ
	x_train, x_test, y_train, y_test = train_test_split(
		x, t, test_size=0.3, random_state=0)

	print("x_train:", x_train.shape)
	print("x_test:", x_test.shape)

	# 訓練データを使って学習
	model.fit(x_train, y_train)

	# テストデータを使って評価
	print("Score:", model.score(x_test, y_test))

	# Save
	pickle.dump(model, open(FILE_PKL, "wb"))

	# 決定木の分岐条件の列
	print("分岐条件の列:", model.tree_.feature)
	# 決定木の分岐条件の閾値
	print("分岐条件の閾値:", model.tree_.threshold)

	# アヤメの種類とグループ番号の対応
	print(model.classes_)

	# リーフに到達したデータの数
	print("ノード1への到達数:", model.tree_.value[1])# ノード番号1に到達した数
	print("ノード3への到達数:", model.tree_.value[3])# ノード番号3に到達した数
	print("ノード4への到達数:", model.tree_.value[4])# ノード番号4に到達した数

	# 決定木を描画する(日本語フォントに対応していないので注意!!)
	plot_tree(model, feature_names=x_train.columns, filled=True)
	plt.show()
	"""

if __name__ == "__main__":
	main()