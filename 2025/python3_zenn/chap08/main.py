# coding: utf-8

"""
Python3_Zenn
"""

print(100 / 0)

"""
# リスト
squares = [1, 4, 9, 16, 25]
print(squares)# [1, 4, 9, 16, 25]
print(squares[0])# 25
print(squares[-3:])# [9, 16, 25]

# 連結
squares = [1, 4, 9, 16, 25]
squares = squares + [36, 49, 64, 81, 100]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 内容の変更
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)# [1, 8, 27, 64, 125]

# 内容の追加
cubes.append(6 ** 3)# 6の3乗
cubes.append(7 ** 3)# 7の3乗
print(cubes)# [1, 8, 27, 64, 125, 216, 343]

# スライスを使った代入
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 一部の範囲を置き換える
letters[2:5] = ["C", "D", "E"]
print(letters)# ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# 一部の範囲を削除する
letters[2:5] = []
print(letters)# ['a', 'b', 'f', 'g']

# 全てを削除する
letters[:] = []
print(letters)# []
"""