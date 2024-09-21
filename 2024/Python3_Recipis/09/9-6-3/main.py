# coding: utf-8

"""
イテレーターから範囲を指定して取得
"""

#==========
# Main

import itertools

# 利点: 
# ジェネレーターオブジェクトや、
# メモリに乗らない巨大なファイルの一部を
# 取り出す場面で特に有効

li_nums = list(range(10))
print(list(li_nums))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

li_slice1 = itertools.islice(li_nums, 5)
print(list(li_slice1))
# [0, 1, 2, 3, 4]

li_slice2 = itertools.islice(li_nums, 3, 8)
print(list(li_slice2))
# [3, 4, 5, 6, 7]

# 複数のイテレーターオブジェクトからタプルを作成

it1 = (1, 2, 3)
it2 = ["abc", "def", "ghi", "jkl"]
it3 = "ABCDE"

for value in zip(it1, it2, it3):
	print(value)

"""
(1, 'abc', 'A')
(2, 'def', 'B')
(3, 'ghi', 'C')
"""

# 最も多い要素に合わせてタプルを作成
for value in itertools.zip_longest(it1, it2, it3):
	print(value)

"""
(1, 'abc', 'A')
(2, 'def', 'B')
(3, 'ghi', 'C')
(1, 'abc', 'A')
(2, 'def', 'B')
(3, 'ghi', 'C')
(None, 'jkl', 'D')
(None, None, 'E')
"""