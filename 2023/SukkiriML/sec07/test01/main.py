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

	# Ageを穴埋め
	#df["Age"] = df["Age"].fillna(df["Age"].mean())# 平均値
	#df["Age"] = df["Age"].fillna(df["Age"].median())# 中央値

	# Survivedでグループした平均値
	#print(df.groupby("Survived")["Age"].mean())

	# 縦軸にSurvived,横軸にPclassとして平均値を集計
	#print(pd.pivot_table(df, index="Survived", columns="Pclass", values="Age"))

	# 縦軸にSurvived,横軸にPclassとして最大値/最小値を集計
	#print(pd.pivot_table(df, index="Survived", columns="Pclass", values="Age", aggfunc="max"))
	#print(pd.pivot_table(df, index="Survived", columns="Pclass", values="Age", aggfunc="min"))

	# Age列の欠損値の行を抜き出す
	is_null = df["Age"].isnull()
	# Pclass1に関する埋め込み
	df.loc[(df["Pclass"]==1)&(df["Survived"]==0)&is_null, "Age"] = 43
	df.loc[(df["Pclass"]==1)&(df["Survived"]==1)&is_null, "Age"] = 35
	# Pclass2に関する埋め込み
	df.loc[(df["Pclass"]==2)&(df["Survived"]==0)&is_null, "Age"] = 33
	df.loc[(df["Pclass"]==2)&(df["Survived"]==1)&is_null, "Age"] = 25
	# Pclass2に関する埋め込み
	df.loc[(df["Pclass"]==3)&(df["Survived"]==0)&is_null, "Age"] = 26
	df.loc[(df["Pclass"]==3)&(df["Survived"]==1)&is_null, "Age"] = 20

	# Embarkedを最頻値で穴埋め
	df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

	# 欠損値を確認する(処理後)
	#print(df.isnull().sum())

	# 特徴量と正解データに分割
	col = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
	x = df[col]
	t = df["Survived"]

	# 男性/女性での生存率を比較
	sex_mean = df.groupby("Sex")["Survived"].mean()
	print(sex_mean)

	# 棒グラフで確認
	#sex_mean.plot(kind="bar")
	#plt.show()

	# Sexをダミー変数に置き換えて特徴量xに追加する
	sex_male = pd.get_dummies(df["Sex"], drop_first=True)
	x = pd.concat([x, sex_male], axis=1)

	# x:特徴量, t:正解データ, depth:木の深さ
	def learn(x, t, depth=3):
		# 訓練データとテストデータに分割
		x_train, x_test, y_train, y_test = train_test_split(
			x, t, test_size=0.2, random_state=0)
		# Model(balanced:不均衡データに対応)
		model = tree.DecisionTreeClassifier(
			max_depth=depth, random_state=0, class_weight="balanced")
		model.fit(x_train, y_train)
		# 決定木モデルの正解率
		score_train = model.score(x_train, y_train)
		score_test = model.score(x_test, y_test)
		return round(score_train, 3), round(score_test, 3), model
	
	# 木の深さによる正解率の変化を確認(過学習を確認)
	#for d in range(1, 8):
	#	score_train, score_test, model = learn(x, t, depth=d)
	#	text = "深さ:{:02d}, 訓練データ正解率:{:01f}, テストデータ正解率:{:01f}"
	#	print(text.format(d, score_train, score_test))

	# 木の深さ8にして学習をする
	d = 8
	score_train, score_test, model = learn(x, t, depth=d)
	text = "深さ:{:02d}, 訓練データ正解率:{:01f}, テストデータ正解率:{:01f}"
	print(text.format(d, score_train, score_test))

	# 特徴量重要度を確認する
	print("特徴量縦横度:", model.feature_importances_)
	print(pd.DataFrame(model.feature_importances_, index=x.columns))

	# Save
	pickle.dump(model, open(FILE_PKL, "wb"))

if __name__ == "__main__":
	main()