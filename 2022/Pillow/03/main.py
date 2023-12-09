# coding: utf-8

"""
ラムダ式でソート
"""

from functools import cmp_to_key

# 例1
def sample01():

	list1 = [("しょうゆ", 580), ("みそ", 750), ("とんこつ", 400)]

	def cmp(a, b):
		return a[1] - b[1]

	list2 = sorted(list1, key=cmp_to_key(cmp))
	print(list2)

sample01()

# 例2
def sample02():
	
	list1 = [("しょうゆ", 580), ("みそ", 750), ("とんこつ", 400)]

	list2 = sorted(list1, key=cmp_to_key(lambda a,b: a[1]-b[1]))
	print(list2)
	
sample02()
