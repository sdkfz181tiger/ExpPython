# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter2-4: 
	宝石の重さをカラットからグラムに変換しよう
"""

print("Hello, Python!!")

# ユーザーからの入力
user = input("何カラットですかっ!?")

# 浮動小数に変換する
n_ct = float(user)

# カラットに変換する単位
p_ct = 0.2

# 計算する
n_g = n_ct * p_ct

# 結果を表示
msg = "{0}カラット = {1}グラム".format(n_ct, n_g)
print(msg)
