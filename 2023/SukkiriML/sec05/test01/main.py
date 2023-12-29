# coding: utf-8

"""
スッキリわかる機械学習入門より
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
"""

import pandas as pd
import pickle
from sklearn import tree

#==========
# Main

def main():
	print("main!!")

	# DataFrame
	df = pd.read_csv("iris.csv")
	print(df.head(3))	

	# Unique
	print(df["種類"].unique())

	# Count
	print(df["種類"].value_counts())

	# Check lost data
	print(df.isnull().any(axis=0))

	# Count up all columns
	print(df.sum())

	# Count up lost data
	print(df.isnull().sum())

	# Drop rows that has lost data
	# how: all 全てが欠損値となっている行/列を削除
	#      any どれか1つが欠損値となっている行/列を削除
	# axis: 0 欠損値がある行を削除
	#       1 欠損値がある列を削除
	print(df.dropna(how="any", axis=0))

	# Fill lost data
	print(df["花弁長さ"].fillna(0))

	# min, max, mean, median...
	print("最小値:", df["がく片長さ"].min())
	print("最大値:", df["がく片長さ"].max())
	print("合計値:", df["がく片長さ"].sum())
	print("平均値:", df["がく片長さ"].mean())
	print("中央値:", df["がく片長さ"].median())
	print("最頻値:", df["がく片長さ"].mode())
	print("分散値:", df["がく片長さ"].var())
	print("標準偏差値:", df["がく片長さ"].std())

	# Fill lost data with average point
	mean = df.mean(numeric_only=True)# 欠損値を除外して計算
	print(df.fillna(mean))

	# 特徴量xと正解データtに分割
	x = df[["がく片長さ", "がく片幅", "花弁長さ", "花弁幅"]]
	t = df["種類"]
	print("特徴量x", x)
	print("正解データt", t)

if __name__ == "__main__":
	main()