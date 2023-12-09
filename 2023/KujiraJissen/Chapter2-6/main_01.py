# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter2-6: 
	繰り返し処理1:1から10まで足すといくつになるか
"""

print("Hello, Python!!")

cnt = 0

for i in range(10):
	cnt = cnt + i

print("合計:{0}".format(cnt))