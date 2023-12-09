# coding: utf-8

"""
リスト内包表記_1
"""

# 例1
def sample01():

	# 0から9までの2乗を配列に格納
	square1 = []
	for i in range(10):
		square1.append(i**2)
	print(square1)

	# リスト内包表記
	square2 = [i**2 for i in range(10)]
	print(square2)

sample01()

# 例2
def sample02():

	# 0から9まで偶数のみ2乗
	square1 = []
	for i in range(10):
		if i%2 == 0:
			square1.append(i**2)
	print(square1)

	# リスト内包表記 if
	square2 = [i**2 for i in range(10) if i%2 == 0]
	print(square2)

	# 0から9まで偶数のみ2乗
	square3 = []
	for i in range(10):
		if i%2 == 0:
			square3.append(i**2)
		else:
			square3.append(i)
	print(square3)

	# リスト内包表記 if - else
	square4 = [i**2 if i%2 == 0 else i for i in range(10)]
	print(square4)

sample02()

# 例3
def sample03():

	# 2重ループ
	list1 = []
	for r in range(10):
		for c in range(10):
			list1.append((r, c))
	print(list1)

	# リスト内包表記
	list2 = [(r, c) for r in range(10) for c in range(10)]
	print(list2)

sample03()
