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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree

COL_X    = ["pclass", "age", "sib_sp", "parch", "fare"]
COL_Y    = "survived"
MY_CSV   = "my_boston.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")

	fit_model()
	

def fit_model():
	""" Fit """
	global COL_X, COL_Y
	#print("fit_model:", depth)

	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	# crime列にデータが何種類あるか
	print(df["crime"].value_counts())

	# crime列をダミー変数化
	# 訓練データ&検証データ、テスト用データに分割する前に行っておく
	crime = pd.get_dummies(df["crime"], 
		drop_first=True, dtype=int)

	# データフレームに連結し、crime列を削除
	df = pd.concat([df, crime], axis=1)
	df = df.drop(["crime"], axis=1)
	print(df.head(3))
	print(df.tail(3))

	# 訓練データ&検証データ、テスト用データに分割
	train_val, test = train_test_split(df, 
		test_size=0.2, random_state=0)

	# 訓練データ&検証データの欠損値を確認
	print(train_val.isnull().sum())






if __name__ == "__main__":
	main()