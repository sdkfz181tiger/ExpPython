# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-1: 
	リストを使って一気に処理しよう
"""

print("Hello, Python!!")

# 成績表
scores = [80, 20, 65, 70, 10]

total = 0# 合計値
for score in scores:
	total += score

print("合計値:{0}".format(total))
print("平均値:{0}".format(total/len(scores)))

# 赤点リスト
akaten = []
for score in scores:
	if score < 30: akaten.append(score)

print("赤点:{0}".format(akaten))