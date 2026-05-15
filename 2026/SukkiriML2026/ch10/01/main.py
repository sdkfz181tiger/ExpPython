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

MY_BIKE    = "my_bike.tsv"
MY_WEATHER = "my_weather.csv"
MY_TEMP    = "my_temp.json"

def main():
	""" Main """
	print("main!!")

	df_bike = pd.read_csv(MY_BIKE, sep="\t") # Tab区切り対応
	print(df_bike.head(3))
	print(df_bike.tail(3))

	df_weather = pd.read_csv(MY_WEATHER, encoding="shift-jis") # Shitt-JIS対応
	print(df_weather.head(3))
	print(df_weather.tail(3))

	# df_bikeと、df_weatherを内部結合する
	df = df_bike.merge(df_weather, how="inner", on="weather_id")
	print(df.head(3))
	print(df.tail(3))

	# weatherごとのcnt平均値
	print(df.groupby("weather")["cnt"].mean())

	df_temp = pd.read_json(MY_TEMP).T # 転置して行と列を入れ替え
	#print(df_temp.head(3))
	#print(df_temp.tail(3))

	# df_tempの、dtedayが、2011-07-20のデータが欠損している...
	print(df_temp.loc[199:201])

	# dfの、2011-07-20のデータは存在する...
	print(df[df["dteday"] == "2011-07-20"])

	# dfと、df_tempを外部結合する
	df = df.merge(df_temp, how="left", on="dteday")

	# dfの、dtedayが、2011-07-20のデータはNaNとして残る
	print(df[df["dteday"] == "2011-07-20"])


if __name__ == "__main__":
	main()