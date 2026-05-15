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
from sklearn.preprocessing import StandardScaler
from sklearn.tree import plot_tree

MY_CSV   = "my_boston.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")

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

	# 欠損値を平均値で補完する
	train_val_mean = train_val.mean()
	train_val = train_val.fillna(train_val_mean)

	# 回帰モデルの場合、外れ値の影響が大きいので外れ値を除去する
	# 散布図を元にして、モデルに大きな影響を与えそうな列を考える
	# 正の相関、負の相関、無相関から検討
	# col_names = train_val.columns
	# for name in col_names:
	# 	train_val.plot(kind="scatter", x=name, y="price")
	# plt.show()

	# "rm"列の外れ値を特定
	out_rm = train_val[
		(train_val["rm"] < 6) & 
		(40 < train_val["price"])].index

	# "ptratio"列の外れ値を特定
	out_ptratio = train_val[
		(18 < train_val["ptratio"]) &
		(40 < train_val["price"])].index

	print(out_rm, out_ptratio)

	# 76のデータが対象になるので除外
	train_val = train_val.drop([76], axis=0)

	# 一旦、次の列のみに絞る
	# indus, nox, rm, ptratio, lstat, price
	train_val = train_val[["indus", "nox", "rm", "ptratio", "lstat", "price"]]
	print(train_val.head(3))

	# 列同士の相関係数を調べる(相関行列)
	print(train_val.corr())

	# 各列と、"price"列との相関係数を調べる(Series)
	print(train_val.corr()["price"])

	# 更に、値を絶対値にする
	print(train_val.corr()["price"].map(abs))

	# 更に、降順に並び替える
	print(train_val.corr()["price"].map(abs).sort_values(ascending=False))

	# 相関係数が高い、"rm"列、"lstat"列、"ptratio"列を特徴量として採用
	x = train_val[["rm", "ptratio", "lstat"]]
	# y = train_val["price"] # x
	y = train_val[["price"]] # o: 後ほど標準化する為

	# 特徴量エンジニアリング(新しく列を独自に追加)
	# 新たに二乗した値を格納した列を作成
	x["rm2"]      = x["rm"] ** 2 # 0.83
	x["lstat2"]   = x["lstat"] ** 2 # 0.84
	x["ptratio2"] = x["ptratio"] ** 2 # 0.86

	# 相互作用特徴量
	# 2つの列を掛け合わせ、新しい列として追加する
	x["rm*lstat"] = x["rm"] * x["lstat"] # 0.87

	# Model, Score
	model, sc_model_x, sc_model_y, score_train, score_val = fit_model(x, y)
	print("score_train:", score_train)
	print("score_val:", score_val)

	# テストデータでテスト(同じ前処理をする)
	test = test.fillna(train_val.mean()) #平均値で補完
	x_test = test[["rm", "ptratio", "lstat"]]
	y_test = test[["price"]]
	x_test["rm2"]      = x_test["rm"] ** 2
	x_test["lstat2"]   = x_test["lstat"] ** 2
	x_test["ptratio2"] = x_test["ptratio"] ** 2
	x_test["rm*lstat"] = x_test["rm"] * x_test["lstat"]
	sc_x_test = sc_model_x.transform(x_test)
	sc_y_test = sc_model_y.transform(y_test)
	score_test = model.score(sc_x_test, sc_y_test)
	print("score_test:", score_test) # 0.78


def fit_model(x, y):
	""" Fit """

	x_train, x_val, y_train, y_val = train_test_split(x, y, 
		test_size=0.2, random_state=0)

	# データの標準化
	# それぞれの特徴量の平均や分布が大きく異なる為、比較が難しい。。。
	# そこで、標準化を行い特徴量の平均値と分布を統一させる。
	# 標準化を行うと、元のデータ集合がどの様な分布でも、
	# 標準化後のデータ集合は「平均値が0、標準偏差が1」の分布となる。
	# これにより、適切な比較と分析が可能になる。

	# 訓練データを標準化
	sc_model_x = StandardScaler()
	sc_model_x.fit(x_train) # 各列の平均値と標準偏差を調べ格納
	sc_x_train = sc_model_x.transform(x_train)
	print(sc_x_train) # array型

	# データフレーム型に変換
	df_tmp = pd.DataFrame(sc_x_train, columns=x_train.columns)
	print(df_tmp.mean()) # 平均値を確認(ほぼ0である)
	print(df_tmp.std()) # 標準偏差(ほぼ1である)

	# 正解データを標準化
	sc_model_y = StandardScaler()
	sc_model_y.fit(y_train)
	sc_y_train = sc_model_y.transform(y_train)
	print(sc_y_train) # array型

	# 重回帰モデルで、標準化済み訓練データを元に訓練する
	model = LinearRegression()
	model.fit(sc_x_train, sc_y_train)

	# モデルの評価を行う("訓練データ"のStandardScalerで行う事!!)
	sc_x_val = sc_model_x.transform(x_val)
	sc_y_val = sc_model_y.transform(y_val)

	# Score
	score_train = model.score(sc_x_train, sc_y_train)
	score_val = model.score(sc_x_val, sc_y_val)

	return model, sc_model_x, sc_model_y, score_train, score_val

if __name__ == "__main__":
	main()