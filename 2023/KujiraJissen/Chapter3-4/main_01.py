# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-4: 
	関数: xxで移動したら何時間!?
"""

import math

print("Hello, Python!!")

# 都市とその距離
cities = {
	"Shizuoka": 183, "Nagoya": 350, "Osaka": 507
}

# 移動手段とその速度
choices = {
	"Walk": 3.1, "Bycycle": 15, "Car": 50,
	"Local": 50, "Rapid": 80, "Express": 100, "ShinKan": 320
}

# 時間を計算する関数
def calc_time(dist, speed):
	return round(dist/speed, 1)

# 選択した移動手段で移動した場合の結果を出力
def main():
	fmt = "| {0:<8} | {1:>4} | {2:<7} | {3:>5} | {4:>5} |"
	for city, dist in cities.items():
		for choice, speed in choices.items():
			time = calc_time(dist, speed)
			print(fmt.format(city, dist, choice, speed, time))

# メインの処理
print("+----------+------+---------+-------+-------+")
print("| City     | Dist | Choice  | Speed | Time  |")
main()
print("+----------+------+---------+-------+-------+")
