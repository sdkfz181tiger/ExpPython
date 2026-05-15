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

COL_X    = ["japanese", "math", "english", "science", "social"]
COL_Y    = "tea"
MY_CSV   = "my_data.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	global COL_X, COL_Y
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
	# animalの答え: 理系は犬派, 文系は猫派
	# teaの答え: 平均90以上は玉露、80以上は抹茶、それ以外は煎茶
	yamada = pd.DataFrame([[30, 80, 20, 80, 20]], columns=COL_X)
	print("山田:", model.predict(yamada)) # 煎茶

	kawasaki = pd.DataFrame([[80, 20, 70, 30, 60]], columns=COL_X)
	print("川崎:", model.predict(kawasaki)) # 抹茶

	ito = pd.DataFrame([[90, 90, 70, 90, 70]], columns=COL_X)
	print("伊藤:", model.predict(ito)) # 玉露

def fit_model():
	""" Fit """
	global COL_X, COL_Y
	print("fit_model")
	
	# CSV
	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	# 特定の列のみ
	print(df["japanese"].head(3))
	print(df[["japanese", "math"]].head(3))

	# 特徴量を準備
	x = df[COL_X]
	print(x.head(3))
	print(type(x)) # DataFrame(複数列の場合)

	# 教師データを準備
	y = df[COL_Y]
	print(y.head(3))
	print(type(y)) # Series(1列の場合)

	# モデルを準備し、学習を実行
	model = tree.DecisionTreeClassifier(random_state=0)
	model.fit(x, y)

	# モデルを評価
	print("正解率:", model.score(x, y))

	return model
	

if __name__ == "__main__":
	main()