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

COL_X    = ["pclass", "age", "sib_sp", "parch", "fare", "male"]
COL_Y    = "survived"
MY_CSV   = "my_survived.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")

	# 決定木モデルの深さを調整しながらモデルを比較する
	# 決定木の深さを増していくと、過学習が起きてしまう
	#    (訓練データのスコアは上がり、検証データのスコアが下がる)
	# 過学習への対処として、様々な方法を検討する必要がある
	#    データの数を増やす
	#    データの前処理を見直す
	#    学習時の設定を変える
	#    分析手法から見直す
	for i in range(3, 10):
		model, score_train, score_test = fit_model(depth=i)
		print("深さ:", i, "訓練データ:", score_train, "検証データ:", score_test)
	

def fit_model(depth):
	""" Fit """
	global COL_X, COL_Y
	#print("fit_model:", depth)

	df = pd.read_csv(MY_CSV)
	#print(df.head(3))
	#print(df.tail(3))

	# 教師データの種類をカウント
	# 不均衡データ(種類の個数にバラツキがある)だとわかる
	# 決定木モデルにとって、不均衡すぎると悪影響が出る
	# 0: 549, 1: 342
	#print(df["survived"].value_counts())

	# 欠損値の総数
	#print(df.isnull().sum())
	
	# 欠損値を穴埋め
	# 穴埋めを何で行うかを検討
	# print("Ageの平均値:", df["age"].mean())
	# print("Ageの中央値:", df["age"].median())
	# print("Ageの最頻値:", df["age"].mode()[0])
	# df["age"] = df["age"].fillna(df["age"].mean()) # 平均値
	# df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0]) # 最頻値

	# グループ集計
	print("survivedごとの平均年齢:")
	print(df.groupby("survived")["age"].mean())

	print("sexごとの平均年齢:")
	print(df.groupby("sex")["age"].mean())

	print("pclassごとの平均年齢:")
	print(df.groupby("pclass")["age"].mean())

	# クロス集計
	#    デフォルトで平均値が集計される
	print("行をsurvive, 列をpclassとして平均値で集計")
	print(pd.pivot_table(df, 
		index="survived", # 行
		columns="pclass", # 列
		values="age")) # 集計対象

	print("中央値で集計")
	print(pd.pivot_table(df, 
		index="survived", # 行
		columns="pclass", # 列
		values="age", # 集計対象
		aggfunc="median")) # 中央値

	# 集計を元に検討し、欠損値を補完
	print("欠損値の個数(Before):", df["age"].isnull().sum())

	# 欠損している行かどうか(補完対象行かどうか)
	is_null = df["age"].isnull()

	# pclass=1に関する埋め込み(andは使えないので注意!!)
	df.loc[(df["pclass"]==1) & (df["survived"]==0) & is_null, "age"] = 43
	df.loc[(df["pclass"]==1) & (df["survived"]==1) & is_null, "age"] = 35

	print("欠損値の個数(After):", df["age"].isnull().sum())

	# pclass=2に関する埋め込み(andは使えないので注意!!)
	df.loc[(df["pclass"]==2) & (df["survived"]==0) & is_null, "age"] = 33
	df.loc[(df["pclass"]==2) & (df["survived"]==1) & is_null, "age"] = 25

	print("欠損値の個数(After):", df["age"].isnull().sum())

	# pclass=2に関する埋め込み(andは使えないので注意!!)
	df.loc[(df["pclass"]==3) & (df["survived"]==0) & is_null, "age"] = 26
	df.loc[(df["pclass"]==3) & (df["survived"]==1) & is_null, "age"] = 20

	print("欠損値の個数(After):", df["age"].isnull().sum())

	# ダミー変数化(ワンホットエンコーディング)
	# sex列は、"male"と、"female"の文字列となっている為、これらをダミー変数とする
	#    drop_first=Trueで、1つ減らした1列のデータフレームとして取得される
	#    drop_first=Falseで、減らさず2列のデータフレームとして取得される
	male = pd.get_dummies(df["sex"], drop_first=True, dtype=int)
	print(male)
	df = pd.concat([df, male], axis=1) # データフレームに連結(列方向)

	# ホールドアウト法で、訓練用と検証用とにデータを分割する
	# test_size: 検証用データの割合
	x = df[COL_X]
	y = df[COL_Y]
	x_train, x_test, y_train, y_test = train_test_split(x, y,
		random_state=0, test_size=0.3)
	
	# 決定木モデルを準備し、学習を実行
	# random_state: 乱数の固定(再現率を上げて調整しやすくする為)
	# max_depth: 決定木の深さ
	# class_weight: 不均衡データに対処
	#    比率の大きいデータの影響を小さく、比率の小さいデータの影響を大きく
	#    これにより、予測性能の良いモデルが出来る可能性がある
	model = tree.DecisionTreeClassifier(
		random_state=0, max_depth=depth, class_weight="balanced")
	model.fit(x_train, y_train)

	# Score
	score_train = model.score(x_train, y_train)
	score_test  = model.score(x_test, y_test)

	return model, round(score_train, 3), round(score_test, 3)


if __name__ == "__main__":
	main()