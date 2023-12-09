# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-1: 
	リストと繰り返し処理
"""

import random

print("Hello, Python!!")

# フルーツ
fruits = ["Apple", "Berry", "Cherry", "Donuts"]

# 配列から順番に取り出す
for fruit in fruits:
	print("I like {0}!!".format(fruit))

# 配列のインデックスを含めて取り出す
for i, fruit in enumerate(fruits):
	print("{0}: I like {1}!!".format(i, fruit))

# 配列からランダムに取り出す
rdm = random.randint(0, len(fruits)-1)
print("I love {0}!!".format(fruits[rdm]))