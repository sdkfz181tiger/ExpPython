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
from sklearn.metrics import mean_absolute_error

FILE_CSV = "./cinema.csv"
FILE_PKL = "./cinema.pkl"

#==========
# Main

def main():
	print("main!!")

	# CSVデータの読込
	df = pd.read_csv(FILE_CSV)
	print(df.head(3))

	# 欠損値の確認(処理前)
	print(df.isnull().any(axis=0))

	# 欠損値を平均値で埋める
	df = df.fillna(df.mean())

	# 欠損値の確認(処理後)
	print(df.isnull().any(axis=0))

	# 散布図で確認(処理前)
	# 	それぞれの列と正解データ"sales"で確認すると良い
	#df.plot(kind="scatter", x="SNS1",  y="sales")
	#df.plot(kind="scatter", x="SNS2",  y="sales")
	#df.plot(kind="scatter", x="actor", y="sales")
	#plt.show()

	# 外れ値を特定しデータから削除
	index = df[(1000<df["SNS2"])&(df["sales"]<8500)].index
	# axis_0:行を削除/1:列を削除
	df = df.drop(index, axis=0)

	# 散布図で確認(処理後)
	#df.plot(kind="scatter", x="SNS2", y="sales")
	#plt.show()

	# 特徴量xと正解データtに分割
	x = df[["SNS1", "SNS2", "actor", "original"]]
	t = df["sales"]

	# 特定の行、列の値を確認
	#index = [0, 1, 2]
	#col = ["SNS1", "SNS2"]
	#print(df.loc[index, col])

	# 0~5の行, SNS1~originalまで
	#print(df.loc[0:5, "SNS1":"original"])

	# 訓練データとテストデータに分割
	x_train, x_test, y_train, y_test = train_test_split(
		x, t, test_size=0.2, random_state=0)

	# 訓練
	model = LinearRegression()
	print(model.fit(x_train, y_train))

	# 予測
	data = [[150, 700, 300, 0]]
	print(model.predict(data))# 6874.109753

	# 平均絶対誤差で評価(MAE)
	pred = model.predict(x_test)
	# y_pred=予測結果データ, y_true=実際のデータ
	print(mean_absolute_error(y_pred=pred, y_true=y_test))# 277.12236964086276

	# 決定係数を求めて評価(0.0 ~ 1.0)
	print(model.score(x_test, y_test))

	# 回帰の計算式における係数と切片
	print("係数:", model.coef_)# 係数
	print("切片:", model.intercept_)# 切片

	# DataFrameで見やすく...
	# 計算式: 1.1*SNS1 + 0.5*SNS2 + 0.3*actor + 214*original + 6253.4
	tmp = pd.DataFrame(model.coef_)
	tmp.index = x_train.columns
	print(tmp)

	# Save
	pickle.dump(model, open(FILE_PKL, "wb"))

if __name__ == "__main__":
	main()