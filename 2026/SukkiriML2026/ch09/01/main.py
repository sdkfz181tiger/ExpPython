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

MY_CSV   = "my_bank.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")

	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	

	"""
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
	"""

if __name__ == "__main__":
	main()