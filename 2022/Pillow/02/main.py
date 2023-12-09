# coding: utf-8

"""
リスト内包表記_2
"""

# 例1
def sample01():

	# keyとvalue
	codes = {}
	for c in range(65, 91):
		codes[chr(c)] = c
	print(codes)

sample01()

# 例2
def sample02():

	# keyとvalue
	codes = {chr(c):c for c in range(65, 91)}
	print(codes)

	# keyとvalueを反転
	reverse = {v:k for k, v in codes.items()}
	print(reverse)

sample02()

# 例3
def sample03():
	
	# 2つのリストから辞書を生成
	list1 = ["A", "B", "C", "D"]
	list2 = ["a", "b", "c", "d"]
	codes = {k:v for k, v in zip(list1, list2)}
	print(codes)

sample03()

# 例4
def sample04():
	
	# 16進数 -> 10進数
	color16 = "#F0F8FF"
	color255 = ([int(color16[i:i+2], 16) for i in range(1, len(color16), 2)])
	print(color255)

	# 10進数 -> 16進数
	str16 = "#"+"".join([f"{n:02X}" for n in color255])
	print(str16)

sample04()