# coding: utf-8

"""
スッキリわかる機械学習入門より
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
"""

import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn import tree
from sklearn.model_selection import train_test_split

FILE_CSV = "./survived.csv"
FILE_PKL = "./survived.pkl"

#==========
# Main

def main():
	print("main!!")

	# CSVデータの読込
	df = pd.read_csv(FILE_CSV)
	print(df.head(2))

	# Survived列にあるデータ種類を確認
	print(df["Survived"].value_counts())

	# 欠損値を確認する(処理前)
	#print(df.isnull().sum())

	# Ageを平均値で穴埋め
	df["Age"] = df["Age"].fillna(df["Age"].mean())
	# Embarkedを最頻値で穴埋め
	df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

	# 欠損値を確認する(処理後)
	#print(df.isnull().sum())

	# 特徴量と正解データに分割
	col = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
	x = df[col]
	t = df["Survived"]
	"""
	# 訓練データとテストデータに分割
	x_train, x_test, y_train, y_test = train_test_split(
		x, t, test_size=0.2, random_state=0)

	print("x_train:", x_train.shape)
	print("x_test:", x_test.shape)

	# Model(balanced:不均衡データに対応)
	model = tree.DecisionTreeClassifier(
		max_depth=5, random_state=0, class_weight="balanced")
	model.fit(x_train, y_train)

	# 決定木モデルの正解率
	print(model.score(x_test, y_test))
	"""
	# x:特徴量, t:正解データ, depth:木の深さ
	def learn(x, t, depth=3):
		x_train, x_test, y_train, y_test = train_test_split(
			x, t, test_size=0.2, random_state=0)
		model = tree.DecisionTreeClassifier(
			max_depth=depth, random_state=0, class_weight="balanced")
		model.fit(x_train, y_train)
		score_train = model.score(x_train, y_train)
		score_test = model.score(x_test, y_test)
		return round(score_train, 3), round(score_test, 3), model

	# 木の深さによる正解率の変化を確認する
	for d in range(1, 5):
		score_train, score_test, model = learn(x, t, depth=d)
		text = "深さ:{}, 訓練データ正解率:{}, テストデータ正解率:{}"
		print(text.format(d, score_train, score_test))

if __name__ == "__main__":
	main()