# coding: utf-8

"""
コンテナ
"""

#==========
# Main

from collections import Counter, defaultdict, OrderedDict
import random


#==========
# Counter
my_cnt1 = Counter("spamhamegg")
print(my_cnt1)
# Counter({'a': 2, 'm': 2, 'g': 2, 's': 1, 'p': 1, 'h': 1, 'e': 1})

# 合計300個の配列を作る
my_list = ["spam"]*110 + ["ham"]*100 + ["egg"]*90
print(len(my_list))# 合計数300
random.shuffle(my_list)# Shuffle
print(Counter(my_list))# 出現回数を確認
# Counter({'spam': 110, 'ham': 100, 'egg': 90})

# Counter(内容は空)
my_cnt2 = Counter()
for num in [1, 3, 2, 1, 1, 3, 2, 1]:
	my_cnt2[num] += 1# 初期化しなくても+1でカウント可能
print(my_cnt2)
# Counter({1: 4, 3: 2, 2: 2})

print(my_cnt2[4])# デフォルト値は0
print(1 in my_cnt2) # True
print(5 in my_cnt2) # False

# 要素のキーを値の数だけ繰り返す
my_cnt3 = Counter(a=1, b=2, c=3, d=4)
print(list(my_cnt3.elements()))
# ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd']

# 値が大きい順に2件
print(my_cnt3.most_common(2))
# [('d', 4), ('c', 3)]

# 減算する
my_cnt4 = Counter(b=2, d=1)
my_cnt3.subtract(my_cnt4)
print(my_cnt3)
# Counter({'c': 3, 'd': 3, 'a': 1, 'b': 0})

# 加算する
my_cnt5 = Counter(a=3, e=5)
my_cnt3.update(my_cnt5)
print(my_cnt3)
# Counter({'e': 5, 'a': 4, 'c': 3, 'd': 3, 'b': 0})


#==========
# DefaultDict

def value():
	return "no_data"

# デフォルト値にvalue関数を指定
d_dic1 = defaultdict(value, spam=100, ham=200)
print(d_dic1["spam"])# 100
print(d_dic1["ham"])# 200
print(d_dic1["egg"])# no_data <- デフォルト値

# デフォルト値を0に
d_dic2 = defaultdict(int)
d_dic2["spam"] += 1
d_dic2["ham"] += 2
d_dic2["egg"] += 3
print(list(d_dic2))
# ['spam', 'ham', 'egg']

# デフォルト値を空のリストに
d_dic3 = defaultdict(list)
print(d_dic3["spam"])
# []
d_dic3["spam"].append("ham")
d_dic3["spam"].append("egg")
print(d_dic3["spam"])
# ['ham', 'egg']


#==========
# OrderedDict

o_dict = OrderedDict(one=1, two=2, three=3)
print(list(o_dict))
# ['one', 'two', 'three']

o_dict.move_to_end("two")# twoを末尾に移動
print(list(o_dict))
# ['one', 'three', 'two']

o_dict.move_to_end("two", last=False)# twoを先頭に移動
print(list(o_dict))
# ['two', 'one', 'three']

print(o_dict.popitem())# 末尾の要素を取り出す
# ('three', 3)

print(o_dict.popitem(last=False))# 先頭の要素を取り出す
# ('two', 2)

