# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-2: 
	テストの点数を集計してみよう
"""

import math

print("Hello, Python!!")

# 成績データ
scores = {
	"Amery": 80, "Beck": 50, "Chan": 70, "Dave": 60, "Elen": 30,
	"Felix": 40, "Godon": 60, "Hanna": 90, "Ian": 50, "Jean": 60
}

# 合計値
n_total = 0
for v in scores.values(): n_total += v
print("合計値:{0}".format(n_total))

# 平均値
n_avg = n_total / len(scores)
print("平均値:{0}".format(n_avg))

# 分散
n_dis = 0
for v in scores.values():
	n_dis += (v - n_avg)**2
n_dis /= len(scores)
print("分散:{0}".format(n_dis))

# 標準偏差
n_dev = math.sqrt(n_dis)
print("標準偏差:{0}".format(n_dev))

# 字寄せ(<左寄せ、>右寄せ)
fmt = "|{0:<6}|{1:>5}|{2:>5}|"

print("| Name | Scr | Dev |")
for k, v in scores.items():
	# 個人の偏差値
	p_dev = ((v-n_avg)*10) / n_dev + 50
	print(fmt.format(k, v, math.floor(p_dev)))