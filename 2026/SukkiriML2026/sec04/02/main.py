# coding: utf-8

"""
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
"""

import pandas as pd
from sklearn import tree

def main():
	""" Main """
	print("main!!")
	
	# CSV
	df = pd.read_csv("my_data.csv")
	print(df.head(3))
	print(df.tail(3))

	# 特定の列のみ
	print(df["cm"].head(3))
	print(df[["cm", "kg"]].head(3))

	# 特徴量を準備
	col_x = ["cm", "kg", "era"]
	x = df[col_x]
	print(x.head(3))
	print(type(x)) # DataFrame

	# 教師データを準備
	col_t = "group"
	t = df[col_t]
	print(t.head(3))
	print(type(t)) # Series

	# モデルを準備し、学習を実行
	model = tree.DecisionTreeClassifier(random_state=0)
	model.fit(x, t)
	
	# 推論を実行(推論時もDataFrameにする)
	elen = pd.DataFrame([[170, 70, 20]], columns=col_x)
	print(model.predict(elen))

	# モデルを評価
	print("正解率:", model.score(x, t))

if __name__ == "__main__":
	main()