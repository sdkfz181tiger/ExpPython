# coding: utf-8

"""
ソート
"""

#==========
# Main

from operator import itemgetter, attrgetter
from datetime import date
from dataclasses import dataclass

# ソート(数値)
nums = [0, 4, 1, 2, 3, 5]

nums.sort()
print(nums)
# [0, 1, 2, 3, 4, 5]

nums.sort(reverse=True)
print(nums)
# [5, 4, 3, 2, 1, 0]

# リバース
nums.reverse()
print(nums)
# [0, 1, 2, 3, 4, 5]

# key引数(引数無し)
strs = ["c", "D", "B", "a"]
print(sorted(strs))
# ['B', 'D', 'a', 'c']

# keys引数(小文字にして比較)
print(sorted(strs, key=str.lower))
# ['a', 'B', 'c', 'D']

#==========
# itemgetter関数
data = [(1, 40, 200), (3, 10, 100), (2, 20, 300), (1, 30, 300)]

# indexを順番に比較してソート
print(sorted(data))
# [(1, 30, 300), (1, 40, 200), (2, 20, 300), (3, 10, 100)]

# indexの2でソートし、それ以外は元の順番
print(sorted(data, key=itemgetter(2)))
# [(3, 10, 100), (1, 40, 200), (2, 20, 300), (1, 30, 300)]

# indexの2でソートし、次に0でソートしそれ以外は元の順番
print(sorted(data, key=itemgetter(2, 0)))
# [(3, 10, 100), (1, 40, 200), (1, 30, 300), (2, 20, 300)]

# 辞書の値でソート
dic = {"a": 2, "c": 1, "b": 3}
print(sorted(dic.items(), key=itemgetter(1)))# 値なので1
# [('c', 1), ('a', 2), ('b', 3)]

# 辞書のキーを指定してソート
member = [
	{"name": "yusha", "gold": 300},
	{"name": "senshi", "gold": 400},
	{"name": "soryo", "gold": 200},
	{"name": "maho", "gold": 100}
]
# 所持金でソート
print(sorted(member, key=itemgetter("gold")))
# [{'name': 'maho', 'gold': 100}, 
# {'name': 'soryo', 'gold': 200}, 
# {'name': 'yusha', 'gold': 300}, 
# {'name': 'senshi', 'gold': 400}]

#==========
# attrgetter関数
dates = [
	date(2024, 5, 8),
	date(2022, 2, 13),
	date(2023, 2, 9),
	date(2021, 12, 1)
]

# .monthでソート
print(sorted(dates, key=attrgetter("month")))

# .monthと.dayの値でソート
print(sorted(dates, key=attrgetter("month", "day")))

# クラス(dataclass)
@dataclass
class User:
	name: str
	gold: int

users = [
	User("yusha", 300),
	User("senshi", 400),
	User("sorho", 200),
	User("maho", 100)
]
# 所持金でソート
print(sorted(users, key=attrgetter("gold")))
# [User(name='maho', gold=100), 
#  User(name='sorho', gold=200), 
#  User(name='yusha', gold=300), 
#  User(name='senshi', gold=400)]


