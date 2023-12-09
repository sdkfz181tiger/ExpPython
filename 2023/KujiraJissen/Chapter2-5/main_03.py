# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter2-5: 
	うるう年を判定してみよう
"""

print("Hello, Python!!")

# うるう年を判定する関数
def is_leap(year):
	if year % 4 == 0:
		if year % 400 == 0: return True
		if year % 100 == 0: return False
		return True
	return False

for i in range(1979, 2023):
	if is_leap(i):
		print("うるう年:{0}".format(i))
