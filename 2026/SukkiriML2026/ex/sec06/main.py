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
MY_CSV   = "ex3.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")
	
	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	#print(df.tail(3))

	# 行数と列数
	print(df.shape)

	# 欠損値の存在を確認
	print(df[COL_X].isnull().sum())

	# 欠損値がある場合は、中央値で補完
	col_median = df[COL_X].median(numeric_only=True)
	df[COL_X] = df[COL_X].fillna(col_median)

	# 欠損値の存在を確認
	print(df[COL_X].isnull().sum())

	

	"""
	# 欠損値がある場合は、中央値で補完
	col_median = df[COL_X].median(numeric_only=True)
	df[COL_X] = df[COL_X].fillna(col_median)

	#print(df[COL_X].isnull().sum()) # 欠損値の存在を確認

	# ホールドアウト法で、訓練用データと検証用データに分割
	x = df[COL_X]
	y = df[COL_Y]
	x_train, x_test, y_train, y_test = train_test_split(x, y,
		random_state=0, test_size=0.2)

	# 決定木モデルを準備し、学習を実行
	# random_state: 乱数の固定(再現率を上げて調整しやすくする為)
	# max_depth: 決定木の深さ
	model = tree.DecisionTreeClassifier(
		random_state=0, max_depth=3)
	model.fit(x_train, y_train)

	# 正解率
	print("Score:", model.score(x_test, y_test))

	# Test
	x_test = pd.DataFrame([[1.56, 0.23, -1.1, -2.8]], columns=COL_X)
	print("Predict:", model.predict(x_test))
	"""

if __name__ == "__main__":
	main()