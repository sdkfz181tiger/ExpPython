# coding: utf-8

"""
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
"""

import pandas as pd
import pickle
from sklearn import tree

COL_X    = ["japanese", "math", "english", "science"]
COL_T    = "social"
MY_CSV   = "my_data.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")

	fit_model()
	

def fit_model():
	""" Fit """
	global COL_X, COL_T
	print("fit_model")
	
	# CSV
	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	# 特定の列のみ
	print(df["japanese"].head(3))
	print(df[["japanese", "math"]].head(3))
	"""
	# 特徴量を準備
	x = df[COL_X]
	print(x.head(3))
	print(type(x)) # DataFrame(複数列の場合)

	# 教師データを準備
	t = df[COL_T]
	print(t.head(3))
	print(type(t)) # Series(1列の場合)

	# モデルを準備し、学習を実行
	model = tree.DecisionTreeClassifier(random_state=0)
	model.fit(x, t)

	# モデルを評価
	print("正解率:", model.score(x, t))

	return model
	"""
	

if __name__ == "__main__":
	main()