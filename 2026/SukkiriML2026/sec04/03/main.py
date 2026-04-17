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

COL_X    = ["cm", "kg", "era"]
COL_T    = "group"
MY_CSV   = "my_data.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	global COL_X, COL_T
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

	# 推論を実行(推論時もDataFrameにする)
	elen = pd.DataFrame([[170, 70, 20]], columns=COL_X)
	print(model.predict(elen))

def fit_model():
	""" Fit """
	global COL_X, COL_T
	print("fit_model")
	
	# CSV
	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	# 特定の列のみ
	print(df["cm"].head(3))
	print(df[["cm", "kg"]].head(3))

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

if __name__ == "__main__":
	main()