# coding: utf-8

"""
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
"""

import pandas as pd
import pickle
import os.path
from sklearn import tree

COL_X    = ["gaku_nagasa", "gaku_haba", "kaben_nagasa", "kaben_haba"]
COL_Y    = "type"
MY_CSV   = "my_iris.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")
	
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
	df3 = df.fillna(col_mean) # 置き換え
	print(df3.isnull().any(axis=0)) # 欠損値確認


if __name__ == "__main__":
	main()