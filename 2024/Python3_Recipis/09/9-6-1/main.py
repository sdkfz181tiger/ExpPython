# coding: utf-8

"""
イテレーターを使った処理
"""

#==========
# Main

import itertools

# イテレーターを連結する
it_chain = itertools.chain(["A", "B"], "cd", range(5))
for element in it_chain:
	print(element)
# A B c d 0 1 2 3 4 の順で出力

# イテレーターで連続値ごとにまとめる
text = "aaabbcdddaabb"
it_group = itertools.groupby(text)
for value, group in it_group:
	print(f"{value}: {list(group)}")
"""
a: ['a', 'a', 'a']
b: ['b', 'b']
c: ['c']
d: ['d', 'd', 'd']
a: ['a', 'a']
b: ['b', 'b']
"""

# あらかじめソートしておく
str_sorted = "".join(sorted(text))
it_sorted = itertools.groupby(str_sorted)
for value, group in it_sorted:
	print(f"{value}: {list(group)}")
"""
a: ['a', 'a', 'a', 'a', 'a']
b: ['b', 'b', 'b', 'b']
c: ['c']
d: ['d', 'd', 'd']
"""

# 関数の結果に従ってグループを作る
def is_odd(num):
	return num%2 == 1

nums = [10, 20, 31, 45, 50, 61]
it_odd = itertools.groupby(nums, is_odd)
for value, group in it_odd:
	print(f"{value}: {list(group)}")

"""
False: [10, 20]
True: [31, 45]
False: [50]
True: [61]
"""