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

COL_X    = ["sns1", "sns2", "actor", "original"]
COL_Y    = "sales"
MY_CSV   = "my_cinema.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
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

	# テスト
	new = pd.DataFrame([[150, 700, 300, 0]], columns=COL_X)
	print(model.predict(new))
	

def fit_model():
	""" Fit """
	global COL_X, COL_Y
	print("fit_model")

	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	# 欠損値の確認
	print(df.isnull().any(axis=0))
	
	# 欠損値を平均値で穴埋め
	df = df.fillna(df.mean())
	# 欠損値の確認
	print(df.isnull().any(axis=0))

	# 外れ値の存在を確認する(xを特徴量に...)
	# sns1と、sns2に外れ値が存在する
	# df.plot(kind="scatter", x="sns1", y="sales")
	# df.plot(kind="scatter", x="sns2", y="sales")
	# df.plot(kind="scatter", x="actor", y="sales")
	# df.plot(kind="scatter", x="original", y="sales")
	# plt.show()

	# 外れ値を探してインデックスを得る
	# データフレームに判定条件を直接指定する事が可能
	# and や or　は使えないので注意

	no = df[(900 < df["sns1"])].index
	df = df.drop(no, axis=0) # 該当行を削除

	no = df[(750 < df["sns1"]) & (df["sales"] < 9500)].index
	df = df.drop(no, axis=0) # 該当行を削除
	
	no = df[(1100 < df["sns2"]) & (df["sales"] < 8500)].index
	df = df.drop(no, axis=0) # 該当行を削除

	#df.plot(kind="scatter", x="sns1", y="sales")
	#df.plot(kind="scatter", x="sns2", y="sales")
	#plt.show()

	# ホールドアウト法で、訓練用と検証用にデータを分ける
	x = df[COL_X]
	y = df[COL_Y]
	x_train, x_test, y_train, y_test = train_test_split(x, y,
		random_state=0, test_size=0.45)

	# 重回帰モデルで、訓練データを元に訓練する
	model = LinearRegression()
	model.fit(x_train, y_train)

	# 検証用データで性能を確認する

	# 回帰モデルの予測性能を測る指標
	#   平均二乗誤差: MSE(mean squared error)
	#      差分を二乗したデータの平均値
	#   平均絶対誤差: MAE(mean absolute error)
	#      差分の絶対値の平均値

	# 平均絶対誤差の計算
	# 学習済みモデルを使って出した予測結果と、テスト用の検証データとを比較
	# 結果として、予測と実際の値の誤差が平均356.xx万円となり、十分小さい値である。
	# (この判断には、データ自体に関する専門知識が必要となる)
	pred = model.predict(x_test) # 予測結果
	mae = mean_absolute_error(y_pred=pred, y_true=y_test)
	print("MAE:", mae) # 356.xxx

	# 決定係数を計算
	# 0~1の間をとり、値が大きくなるほど予測値と実測値の誤差が少ない計算式であると判断できる
	# 平均絶対誤差とは異なり、正解データの持つ意味に依存することはない
	# 0.8以上であれば、予測性能が高い計算式と言われる
	print("Score:", model.score(x_test, y_test))

	# 回帰式の係数と切片を確認する
	# 係数の絶対値が大きい程、影響が強い
	print("係数:", model.coef_)
	print("切片:", model.intercept_)

	return model


if __name__ == "__main__":
	main()