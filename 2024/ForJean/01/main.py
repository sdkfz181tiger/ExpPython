# coding: utf-8

"""
継承先のクラスで演算子オーバーロードを使う
"""

#==========
# Main

# 基底クラス
class Vector:

	def __init__(self, x, y):
		print("Vector")
		self.x = x
		self.y = y

	# 演算子オーバーロード
	def __add__(self, other):
		return self.__class__(self.x + other.x, self.y + other.y)

	def __str__(self):
		return f'{self.__class__} ({self.x}, {self.y})'

# 継承クラス
class MyVector(Vector):

	def __init__(self, x, y):
		print("MyVector")
		super().__init__(x, y)

def main():

	# Test
	vecA = MyVector(1, 2)
	vecB = MyVector(3, 4)
	vecC = vecA + vecB
	print(vecC)

if __name__ == "__main__":
	main()
