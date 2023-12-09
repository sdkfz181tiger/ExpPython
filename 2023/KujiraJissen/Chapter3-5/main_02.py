# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-5: 
	ラムダ式2: map,filter,sortと組み合わせる
"""

import math

print("Hello, Python!!")

# 数値リスト
nums = [10, 17, 11, 16, 19, 13, 18, 14]

# map(各項目をx倍にする)
print(list(map(lambda x:x*2, nums)))
print(list(map(lambda x:x*3, nums)))
print(list(map(lambda x:x*4, nums)))

# filter(偶数、奇数)
print(list(filter(lambda x: x%2==0, nums)))# 偶数のみ
print(list(filter(lambda x: x%2!=0, nums)))# 奇数のみ

# 所持金リスト
h_list = [
	("Alex", 3000), ("Beck", 8000), ("Charlie", 4000), 
	("David", 6000), ("Elen", 2000), ("Felix", 9000)
]

# sorted(所持金の多い順)
print(sorted(h_list, key=lambda x: x[1], reverse=True))

# 所持金ディクショナリ
h_dict = {
	"Alex":3000, "Beck":8000, "Charlie":4000,
	"David":6000, "Elen":2000, "Felix":9000
}

# sorted
print(sorted(h_dict.items(), key=lambda x:x[1], reverse=True))