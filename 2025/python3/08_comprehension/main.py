# coding: utf-8

"""
Hello World
"""

#==========
# Main

# Comprehension

# 0 ~ 9までの値を2乗したリストを作る内包表記
squares = [x**2 for x in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 0 ~ 9までの値を3乗したリストを作る内包表記
cubes = [x**3 for x in range(10)]
print(cubes)
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


# 0 ~ 9までの値で、4の倍数を除外したリストを作る内包表記
nums1 = [x for x in range(10) if x % 4 != 0]
print(nums1)
# [1, 2, 3, 5, 6, 7, 9]


# 0 ~ 9までの値で、3の倍数を除外したリストを作る内包表記
nums1 = [x for x in range(10) if x % 3 != 0]
print(nums1)
# [1, 2, 4, 5, 7, 8]


# 内包表記で九九表を作る
kuku = [((x, y), x*y) for x in range(1, 10) for y in range(1, 10)]
#print(kuku)
# [((1, 1), 1), ((1, 2), 2), ... ,((9, 8), 72), ((9, 9), 81)]


