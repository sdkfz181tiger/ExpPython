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
	print(df["japanese"].head(3))
	print(df[["japanese", "math"]].head(3))

	# 特徴量を準備
	col_x = ["japanese", "math", "english", "science", "social"]
	x = df[col_x]
	print(x.head(3))
	print(type(x)) # DataFrame

	# 教師データを準備
	col_t = "animal"
	t = df[col_t]
	print(t.head(3))
	print(type(t)) # Series

	# モデルを準備し、学習を実行
	model = tree.DecisionTreeClassifier(random_state=0)
	model.fit(x, t)
	
	# 推論を実行(推論時もDataFrameにする)
	# animalの答え: 理系は犬派, 文系は猫派
	# teaの答え: 平均90以上は玉露、80以上は抹茶、それ以外は煎茶
	yamada = pd.DataFrame([[30, 80, 20, 80, 20]], columns=col_x)
	print("山田:", model.predict(yamada)) # 犬派

	# モデルを評価
	print("正解率:", model.score(x, t))

if __name__ == "__main__":
	main()