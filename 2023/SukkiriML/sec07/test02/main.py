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

FILE_CSV = "./data.csv"
FILE_PKL = "./data.pkl"

#==========
# Main

def main():
	print("main!!")

	# CSVデータの読込
	df = pd.read_csv(FILE_CSV)
	#print(df.head(3))

	# 男女比を計算する
	print("男女比:", df["Sex"].mean())

	# 役職ごとの平均評価値
	print(df.groupby("Class")["Score"].mean())

	# 縦軸にSurvived,横軸にPclassとして平均値を集計
	# 	最も平均値が高いグループは、役職が
	print(pd.pivot_table(df, index="Class", columns="Sex", values="Score"))

	# 特徴量と正解データに分割
	col = ["Class", "Sex"]
	x = df[col]
	t = df["Score"]

	# Dept_idをダミー変数に置き換えて特徴量xに追加する
	dept = pd.get_dummies(df["Dept_id"], drop_first=True)
	x = pd.concat([x, dept], axis=1)
	print(x.head(3))

if __name__ == "__main__":
	main()