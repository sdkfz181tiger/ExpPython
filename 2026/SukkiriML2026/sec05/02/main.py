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
from sklearn.tree import plot_tree

COL_X    = ["gaku_nagasa", "gaku_haba", "kaben_nagasa", "kaben_haba"]
COL_Y    = "type"
MY_CSV   = "my_iris.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")

	if os.path.isfile(MY_MODEL):
		print("Let's load model!!")
		# Open model
		with open(MY_MODEL, "rb") as f:
			model = pickle.load(f)
	else:
		print("Let's fit model!!")
		# Fit
		model = fit_model()
		# Dump model
		with open(MY_MODEL, "wb") as f:
			pickle.dump(model, f)

	# 分岐条件を確認する
	# 分岐に利用した、特徴量の列番号を示す(-2は葉を示す)
	print(model.tree_.feature)
	# 分岐条件のしきい値を示す
	print(model.tree_.threshold)

	# 決定木を描画する(日本語フォントに対応していないので注意!!)
	plot_tree(model, feature_names=COL_X, filled=True)
	plt.show()


def fit_model():
	""" Fit """
	global COL_X, COL_Y
	print("fit_model")
	
	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	# 値の種類
	print(df["type"].unique())

	# 値の種類の総数
	print(df["type"].value_counts())

	# 欠損値の有無を確認
	print(df.isnull())

	# 各列に欠損値がいくつあるか集計
	# (Trueを1, Falseを0として集計)
	print(df.isnull().sum())

	# 列単位で欠損値の有無を確認
	# axis=0で列方向、axis=1行方向
	print(df.isnull().any(axis=0))

	# 欠損値が1つでもある行を削除
	# how="all" は、全てが欠損値となっている行/列の削除
	# how="any" は、どれか1つ欠損値となっている行/列の削除
	# axis=0 は、欠損値がある行を削除
	# axis=1 は、欠損値がある列を削除
	#df2 = df.dropna(how="any", axis=0)
	#print(df2.tail(3))

	# 欠損値を指定した値(0)に置き換える
	#df["花弁長さ"] = df["花弁長さ"].fillna(0)
	#print(df.tail(3))

	# 欠損値を何に置き換えるか考える

	# 平均値
	print(df.mean(numeric_only=True))
	# 中央値
	print(df.median(numeric_only=True))
	# 最頻値
	print(df.mode(numeric_only=True))
	# 最大値
	print(df.max(numeric_only=True))
	# 最小値
	print(df.min(numeric_only=True))

	# 欠損値を"平均値"で一括置き換え
	col_mean = df.mean(numeric_only=True) # 平均値
	df = df.fillna(col_mean) # 置き換え
	print(df.isnull().any(axis=0)) # 欠損値確認

	# 特徴量を準備
	x = df[COL_X]
	print(x.head(3))
	print(type(x)) # DataFrame(複数列の場合)

	# 教師データを準備
	y = df[COL_Y]
	print(y.head(3))
	print(type(y)) # Series(1列の場合)

	# ホールドアウト法で、学習用と検証用とにデータを分割する
	# test_size: 検証用データの割合
	x_train, x_test, y_train, y_test = train_test_split(x, y,
		random_state=0, test_size=0.3)

	print(x_train.shape) # x_trainの行数と列数
	print(x_test.shape) # x_testの行数と列数

	# モデルを準備し、学習を実行
	# random_state: 乱数の固定(再現率を上げて調整しやすくする為)
	# max_depth: 決定木の深さ
	model = tree.DecisionTreeClassifier(
		random_state=0, max_depth=3)
	model.fit(x_train, y_train)

	# 正解率
	print("Score:", model.score(x_test, y_test))

	return model


if __name__ == "__main__":
	main()