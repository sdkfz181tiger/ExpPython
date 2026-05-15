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
from sklearn.covariance import MinCovDet

MY_BIKE    = "my_bike.tsv"
MY_WEATHER = "my_weather.csv"
MY_TEMP    = "my_temp.json"

def main():
	""" Main """
	print("main!!")

	df_bike = pd.read_csv(MY_BIKE, sep="\t") # Tab区切り対応
	#print(df_bike.head(3))
	#print(df_bike.tail(3))

	df_weather = pd.read_csv(MY_WEATHER, encoding="shift-jis") # Shitt-JIS対応
	#print(df_weather.head(3))
	#print(df_weather.tail(3))

	# df_bikeと、df_weatherを内部結合する
	df = df_bike.merge(df_weather, how="inner", on="weather_id")
	#print(df.head(3))
	#print(df.tail(3))

	# weatherごとのcnt平均値
	#print(df.groupby("weather")["cnt"].mean())

	df_temp = pd.read_json(MY_TEMP).T # 転置して行と列を入れ替え
	#print(df_temp.head(3))
	#print(df_temp.tail(3))

	# df_tempの、dtedayが、2011-07-20のデータが欠損している...
	#print(df_temp.loc[199:201])

	# dfの、2011-07-20のデータは存在する...
	#print(df[df["dteday"] == "2011-07-20"])

	# dfと、df_tempを外部結合する
	df = df.merge(df_temp, how="left", on="dteday")

	# 計算対象のデータを用意
	df = df.loc[:, "atemp":"windspeed"]
	df = df.dropna() # 欠損値を削除

	# マハラノビス距離を計算
	# 特徴量を、データのバラつきや相関係数を踏まえて計算した距離
	mcd = MinCovDet(random_state=0, support_fraction=0.7)
	mcd.fit(df)
	distance = mcd.mahalanobis(df)
	print(distance)

	# 箱ヒゲ図で外れ値を確認
	distance = pd.Series(distance)
	distance.plot(kind="box")
	#plt.show()

	# 中央値を用いて外れ値を判定する
	# IQR(四分位範囲)を求める(50%のデータが収まる範囲)
	# 下限(25%)が、2.311196
	# 上限(75%)が、6.554506だとわかる
	tmp = distance.describe()
	#print(tmp)

	# IQRを元にして、外れ値を判定する閾値を計算する
	iqr = tmp["75%"] - tmp["25%"]
	limit_upper = tmp["75%"] + 1.5 * iqr
	limit_lower = tmp["25%"] - 1.5 * iqr

	# 外れ値
	outliner = distance[(distance < limit_lower) | (limit_upper < distance)]
	print(outliner)


if __name__ == "__main__":
	main()