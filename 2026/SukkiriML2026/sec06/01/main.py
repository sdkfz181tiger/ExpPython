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

COL_X    = ["SNS1", "SNS2", "actor", "original"]
COL_Y    = "sales"
MY_CSV   = "my_cinema.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")
	
	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	# 欠損値の確認
	print(df.isnull().any(axis=0))
	
	# 欠損値を平均値で穴埋め
	df2 = df.fillna(df.mean())
	# 欠損値の確認
	print(df2.isnull().any(axis=0))

	# 外れ値の存在を確認する(xを特徴量に...)
	# SNS1と、SNS2に外れ値が存在する
	# df2.plot(kind="scatter", x="SNS1", y="sales")
	# df2.plot(kind="scatter", x="SNS2", y="sales")
	# df2.plot(kind="scatter", x="actor", y="sales")
	# df2.plot(kind="scatter", x="original", y="sales")
	# plt.show()

	# 外れ値を探してインデックスを得る
	# データフレームに判定条件を直接指定する事が可能
	# and や or　は使えないので注意
	no = df2[(1100 < df2["SNS2"]) & (df2["sales"] < 8500)].index
	df3 = df2.drop(no, axis=0) # 該当行を削除
	df3.plot(kind="scatter", x="SNS2", y="sales")
	plt.show()



if __name__ == "__main__":
	main()