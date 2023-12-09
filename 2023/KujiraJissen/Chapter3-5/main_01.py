# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-5: 
	ラムダ式1: ラムダ式を関数に渡す
"""

import math

print("Hello, Python!!")

# 2倍にするラムダ式
double = lambda x: x*2
triple = lambda x: x*3

# 引数にラムダ式を指定する関数
def calc_test1(func, x):
	return func(x)

# テスト
print(calc_test1(double, 10))
print(calc_test1(triple, 10))

add = lambda x, y: x+y
sub = lambda x, y: x-y
mul = lambda x, y: x*y
div = lambda x, y: x/y

# 引数にラムダ式を指定する関数
def calc_test2(func, x, y):
	return func(x, y)

print(calc_test2(add, 10, 20))
print(calc_test2(sub, 10, 20))
print(calc_test2(mul, 10, 20))
print(calc_test2(div, 10, 20))