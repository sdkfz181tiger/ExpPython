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
from sklearn.metrics import mean_absolute_error

COL_X    = ["x0", "x1", "x2", "x3"]
COL_Y    = "target"
MY_CSV   = "ex3.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")
	
	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	# 欠損値の確認
	print(df.isnull().any(axis=0))

	# 欠損値を中央値で穴埋め
	df = df.fillna(df.median())
	# 欠損値の確認
	print(df.isnull().any(axis=0))

	# x0の外れ値を除去
	no = df[df["x0"] < -2.5].index
	df = df.drop(no, axis=0)

	# x1の外れ値を除去
	no = df[(df["x1"] < -2.0) | (2.5 < df["x1"])].index
	df = df.drop(no, axis=0)

	# x2の外れ値を除去
	no = df[(df["x2"] < -2.0) | (2.0 < df["x2"])].index
	df = df.drop(no, axis=0)

	# x3の外れ値を除去
	no = df[(df["x3"] < -2.0) | (2.0 < df["x3"])].index
	df = df.drop(no, axis=0)

	# x0, x1, x2, x3列とtarget列の散布図
	# df.plot(kind="scatter", x="x0", y="target")
	# df.plot(kind="scatter", x="x1", y="target")
	# df.plot(kind="scatter", x="x2", y="target")
	# df.plot(kind="scatter", x="x3", y="target")
	# plt.show()

	# 特徴量と正解データに分割
	x = df.loc[:, :"x3"] # 全ての行、x0~x3の列
	y = df["target"]
	print("x:", x.shape)
	print("y:", y.shape)

	# 訓練データ、検証データに分割
	x_train, x_test, y_train, y_test = train_test_split(x, y,
		random_state=1, test_size=0.2)

	# 訓練データでモデルを作成
	model = LinearRegression()
	model.fit(x_train, y_train)

	# 検証データでモデルを評価
	pred = model.predict(x_test) # 予測結果

	# 平均絶対誤差(判定には専門的知識が必要)
	mae = mean_absolute_error(y_pred=pred, y_true=y_test)
	print("MAE:", mae) # 4.293...

	# 決定係数(0.8以上であれば高い予測性能とされる)
	print("Score:", model.score(x_test, y_test)) # 0.993...


if __name__ == "__main__":
	main()