# coding: utf-8

"""
気象データ
	https://www.data.jma.go.jp/gmd/risk/obsdl/
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# LinearRegression
print("Hello LinearRegression!!")

# CSV
CSV_IN = "./ogaki_in.csv"
CSV_OUT = "./ogaki_out.csv"
INTERVAL = 6

def copy_file():
	if os.path.isfile(CSV_OUT): return
	# ファイル入力
	with open(CSV_IN, "rt", encoding="Shift_JIS") as fr:
		lines = fr.readlines()

	lines = ["年,月,日,気温,品質,均質\n"] + lines[5:]
	lines = map(lambda v: v.replace("/", ","), lines)# 年/月/日を変換
	result = "".join(lines).strip()# 

	# ファイル出力
	with open(CSV_OUT, "wt", encoding="utf-8") as fw:
		fw.write(result)

# 過去INTERVAL日分のデータに整える
def make_data(data):
	x = [] # 学習データ
	y = [] # 結果データ
	temps = list(data["気温"])
	for i in range(len(temps)):
		if i < INTERVAL: continue # Interval
		a = [] # INTERVAL日分の学習データ
		y.append(temps[i]) # 結果データ
		for p in range(INTERVAL):
			d = i + p - INTERVAL
			a.append(temps[d])
		x.append(a)
	return (x, y)

# 気温を予測する
def prediction():
	if not os.path.isfile(CSV_OUT): return
	print("= Prediction =")
	# CSVファイル
	csv_weather = pd.read_csv(CSV_OUT, encoding="utf-8")

	# 学習用データ
	flg_train = csv_weather["年"] <= 2015
	x_train, y_train = make_data(csv_weather[flg_train])

	# テスト用データ
	flg_test = 2016 <= csv_weather["年"]
	x_test, y_test = make_data(csv_weather[flg_test])

	# 線形回帰分析
	clf = LinearRegression(normalize=True)
	clf.fit(x_train, y_train) # 学習
	y_pred = clf.predict(x_test) # 予測データ

	# 結果を図にプロット
	plt.figure(figsize=(10, 6), dpi=100)
	plt.plot(y_test, c="r")# テストデータ
	plt.plot(y_pred, c="b")# 予測データ
	plt.savefig("./prediction.png")
	plt.show()

# Main
copy_file()
prediction()
