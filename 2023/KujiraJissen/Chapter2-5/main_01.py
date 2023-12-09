# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter2-5: 
	チケット売り場のレジシステムを作ろう
"""

print("Hello, Python!!")

# ユーザーからの入力
n_child = int(input("子供(13歳未満)は何人!?"))
n_adult = int(input("大人(13歳-64歳)は何人!?"))
n_elder = int(input("年配(65歳以上)は何人!?"))

# 集計
n_total = n_child + n_adult + n_elder

# 料金表
f_child = 500
f_adult = 1000
f_elder = 700

# 料金
p_child = n_child * f_child
p_adult = n_adult * f_adult
p_elder = n_elder * f_elder

# 合計
p_total = p_child + p_adult + p_elder

# 結果を表示
print("子供料金:{0}人 x {1}円 = {2}円".format(n_child, f_child, p_child))
print("大人料金:{0}人 x {1}円 = {2}円".format(n_adult, f_adult, p_adult))
print("年配料金:{0}人 x {1}円 = {2}円".format(n_elder, f_elder, p_elder))

# 割引処理
if 9 < n_total:
	print("団体割引を適用します")
	p_total = p_total * 0.8
else:
	print("割引はありません")

print("合計: {0}人, {1}円".format(n_total, p_total))
