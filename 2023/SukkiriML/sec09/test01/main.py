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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

FILE_CSV = "./bank.csv"
FILE_PKL = "./bank.pkl"

#==========
# Main

def main():
	print("main!!")

	# CSVデータの読込
	df = pd.read_csv(FILE_CSV)
	print(df.head(5))

	"""
	# CRIME列の種類を確認
	#print(df["CRIME"].value_counts())

	# CRIME列をダミー化(low, very_lowのみに)
	crime = pd.get_dummies(df["CRIME"], drop_first=True)
	df = pd.concat([df, crime], axis=1)# Concat
	df = df.drop(["CRIME"], axis=1)# Drop

	# 訓練データ&検証データ,テストデータに分割
	train_valid, test = train_test_split(df, 
		test_size=0.2, random_state=0)

	# 訓練データ&検証データの欠損値を確認
	print(train_valid.isnull().sum())

	# NOXを平均値で穴埋め
	train_valid_mean = train_valid.mean()
	train_valid = train_valid.fillna(train_valid_mean)

	# PRICEとの関係を散布図で確認
	#train_valid.plot(kind="scatter", x="RM", y="PRICE")
	#train_valid.plot(kind="scatter", x="PTRATIO", y="PRICE")
	#plt.show()

	# RMの外れ値
	out_rm = train_valid[(train_valid["RM"]<6)&(40<train_valid["PRICE"])].index
	print(out_rm)
	# PTRATIOの外れ値
	out_ptratio = train_valid[(18<train_valid["PTRATIO"])&(40<train_valid["PRICE"])].index
	print(out_ptratio)
	# 外れ値を取り除く(76が共通だった為)
	train_valid = train_valid.drop([76], axis=0)

	# 各列同士の相関係数を調べる(相関行列)
	#print(train_valid.corr())# 各列同士
	#print(train_valid.corr()["PRICE"])# 特定の列

	# PRICE列との相関を絶対値に
	cor_train_valid = train_valid.corr()
	cor_abs = cor_train_valid.map(abs)
	# PRICE列を基準として降順に
	cor_abs = cor_abs.sort_values(by="PRICE", ascending=False)
	print(cor_abs["PRICE"])

	# PRICE列との相関の強いRM,LSTAT,PTRATIO列を特徴量として利用する
	x = train_valid[["RM", "LSTAT", "PTRATIO"]]
	t = train_valid[["PRICE"]]

	# 2乗を特徴量に追加(特徴量エンジニアリング)
	# 追加する特徴量や、3乗にしたり4乗にしたり試行錯誤を繰り返す!!
	x["RM2"] = x["RM"] ** 2
	x["LSTAT2"] = x["LSTAT"] ** 2
	x["PTRATIO2"] = x["PTRATIO"] ** 2

	# 2つの特徴量を掛け合わせた特徴量を用意する(相互作用特徴量)
	x["RM*LSTAT*PTRATIO"] = x["RM"] * x["LSTAT"] * x["PTRATIO"]

	# 訓練データと検証データに分割
	x_train, x_valid, y_train, y_valid = train_test_split(
		x, t, test_size=0.2, random_state=0)

	# 特徴量列の標準偏差を調べて格納
	sc_model_x = StandardScaler()
	sc_model_x.fit(x_train)
	sc_x = sc_model_x.transform(x_train)# 各列のデータを標準化
	print(sc_x)

	# 正解データ列の標準偏差を調べて格納
	sc_model_y = StandardScaler()
	sc_model_y.fit(y_train)# あらかじめデータフレーム形式にしておくのがポイント!!
	sc_y = sc_model_y.transform(y_train)
	print(sc_y)

	# 標準偏差を確認する
	tmp_x = pd.DataFrame(sc_x, columns=x_train.columns)
	print(tmp_x.mean())# 平均値は0になる筈(e-16となっているのでほぼ0)
	print(tmp_x.std())# 標準偏差1を確認する

	# Model
	model = LinearRegression()
	model.fit(sc_x, sc_y)

	# モデルを評価する(こちらも標準化したデータを使う事)
	sc_x_valid = sc_model_x.transform(x_valid)
	sc_y_valid = sc_model_y.transform(y_valid)
	print("評価:", model.score(sc_x_valid, sc_y_valid))

	# Learn関数
	def learn(x, t):
		x_train, x_valid, y_train, y_valid = train_test_split(
			x, t, test_size=0.2, random_state=0)
		# 訓練データを標準化
		sc_model_x = StandardScaler()
		sc_model_x.fit(x_train)
		sc_x_train = sc_model_x.transform(x_train)
		sc_model_y = StandardScaler()
		sc_model_y.fit(y_train)
		sc_y_train = sc_model_y.transform(y_train)
		# Model
		model = LinearRegression()
		model.fit(sc_x_train, sc_y_train)
		# モデルを評価
		sc_x_valid = sc_model_x.transform(x_valid)
		sc_y_valid = sc_model_y.transform(y_valid)
		# 訓練データと検証データの決定係数計算
		score_train = model.score(sc_x_train, sc_y_train)
		score_valid = model.score(sc_x_valid, sc_y_valid)
		return score_train, score_valid

	# 訓練データと検証データでLearn関数を実行
	score_train, score_valid = learn(x, t)
	print("Learn関数(訓練データと検証データ):", score_train, score_valid)

	#==========
	# チューニング後に訓練データとテストデータで評価
	test = test.fillna(train_valid_mean)# 欠損値を平均値で穴埋め
	x_test = test.loc[:, ["RM", "LSTAT", "PTRATIO"]]
	y_test = test[["PRICE"]]
	x_test["RM2"] = x_test["RM"] ** 2
	x_test["LSTAT2"] = x_test["LSTAT"] ** 2
	x_test["PTRATIO2"] = x_test["PTRATIO"] ** 2
	x_test["RM*LSTAT*PTRATIO"] = x_test["RM"] * x_test["LSTAT"] * x_test["PTRATIO"]
	sc_x_test = sc_model_x.transform(x_test)
	sc_y_test = sc_model_y.transform(y_test)
	score_test = model.score(sc_x_test, sc_y_test)# 決定係数
	print("訓練データ&検証データとテストデータ:", score_test)

	#==========
	# Save(Model)
	pickle.dump(model, open(FILE_PKL, "wb"))# Model
	
	# Save(標準化を行う為)
	pickle.dump(sc_model_x, open("sc_model_x.pkl", "wb"))
	pickle.dump(sc_model_y, open("sc_model_y.pkl", "wb"))
	"""

if __name__ == "__main__":
	main()