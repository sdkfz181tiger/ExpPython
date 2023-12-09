# coding: utf-8

"""
気象データ
	https://www.data.jma.go.jp/gmd/risk/obsdl/
"""

import os
import pandas as pd

# Pandas
print("Hello Pandas!!")

# CSV
CSV_IN = "./ogaki_in.csv"
CSV_OUT = "./ogaki_out.csv"

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

# 年ごとの平均
def check_avg_y():
	if not os.path.isfile(CSV_OUT): return
	print("= Year =")
	# CSVファイル
	csv_weather = pd.read_csv(CSV_OUT, encoding="utf-8")
	# 年ごとに気温をリストにまとめる
	data = {}
	for i, row in csv_weather.iterrows():
		m, v = (int(row["年"]), float(row["気温"]))
		k = "{:02d}".format(m)# key
		if not(k in data): data[k] = []
		data[k] += [v]
	# 年ごとに平均を算出
	avg = {}
	for k in sorted(data):
		v = avg[k] = sum(data[k]) / len(data[k])# その日付の平均値
		print("{0}:{1}".format(k, v))

# 月ごとの平均
def check_avg_m():
	if not os.path.isfile(CSV_OUT): return
	print("= Month =")
	# CSVファイル
	csv_weather = pd.read_csv(CSV_OUT, encoding="utf-8")
	# 月ごとに気温をリストにまとめる
	data = {}
	for i, row in csv_weather.iterrows():
		m, v = (int(row["月"]), float(row["気温"]))
		k = "{:02d}".format(m)# key
		if not(k in data): data[k] = []
		data[k] += [v]
	# 月ごとに平均を算出
	avg = {}
	for k in sorted(data):
		v = avg[k] = sum(data[k]) / len(data[k])# その日付の平均値
		print("{0}:{1}".format(k, v))

# 日ごとの平均
def check_avg_d():
	if not os.path.isfile(CSV_OUT): return
	print("= Days =")
	# CSVファイル
	csv_weather = pd.read_csv(CSV_OUT, encoding="utf-8")
	# 日ごとに気温をリストにまとめる
	data = {}
	for i, row in csv_weather.iterrows():
		m, d, v = (int(row["月"]), int(row["日"]), float(row["気温"]))
		k = "{:02d}/{:02d}".format(m, d)# key
		if not(k in data): data[k] = []
		data[k] += [v]
	# 日ごとに平均を算出
	avg = {}
	for k in sorted(data):
		v = avg[k] = sum(data[k]) / len(data[k])# その日付の平均値
		print("{0}:{1}".format(k, v))

# d度を越えた日を年単位で集計
def check_over_deg(d):
	if not os.path.isfile(CSV_OUT): return
	print("= Over %d =" % d)
	# CSVファイル
	csv_weather = pd.read_csv(CSV_OUT, encoding="utf-8")
	csv_over30 = csv_weather[csv_weather["気温"] > d]# d度越え
	csv_years = csv_over30.groupby("年")["年"].count()# 年をグループ化して集計
	print(csv_years)

# d度を下回った日を年単位で集計
def check_under_deg(d):
	if not os.path.isfile(CSV_OUT): return
	print("= Under %d =" % d)
	# CSVファイル
	csv_weather = pd.read_csv(CSV_OUT, encoding="utf-8")
	csv_over30 = csv_weather[csv_weather["気温"] < d]# d度未満
	csv_years = csv_over30.groupby("年")["年"].count()# 年をグループ化して集計
	print(csv_years)

# Main
copy_file()
check_avg_y()
check_avg_m()
check_avg_d()
check_over_deg(30)# 30度越えた日
check_under_deg(3)# 3度未満の日










