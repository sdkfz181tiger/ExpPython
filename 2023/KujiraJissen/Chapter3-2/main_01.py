# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-2: 
	辞書型
"""

import math

print("Hello, Python!!")

# 辞書型
foods = {"Ramen":100, "Soba": 200, "Curry": 300, "Humburg": 400}

# キーが存在するか
print("Soba" in foods)# True
print("Udon" in foods)# False

# キーの一覧(dict_keys型)
print(foods.keys())

# 値の一覧(dict_values型)
print(foods.values())

# 辞書型をリストに変換
print(list(foods.keys()))

# アルファベット順にソート
print(sorted(foods.keys()))

# for文と組み合わせる1
for key in foods.keys():
	print("{0}:{1}yen".format(key, foods[key]))

# for文と組み合わせる2
for k, v in foods.items():
	print("{0}:{1}yen".format(k, v))