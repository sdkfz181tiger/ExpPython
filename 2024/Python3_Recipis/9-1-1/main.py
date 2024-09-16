# coding: utf-8

"""
ソート
"""

#==========
# Main

# ソート(数値)
nums = [0, 4, 1, 2, 3, 5]
print(sorted(nums))
# [0, 1, 2, 3, 4, 5]
print(sorted(nums, reverse=True))
# [5, 4, 3, 2, 1, 0]

# ソート(文字列)
foods = ["spam", "ham", "egg"]
print(sorted(foods))
# ['egg', 'ham', 'spam']
print(sorted(foods, reverse=True))
# ['spam', 'ham', 'egg']

# ソート(タプル型) -> リスト型で返る
nums = (0, 4, 1, 2, 3, 5)
print(sorted(nums))
# [0, 1, 2, 3, 4, 5]
print(sorted(nums, reverse=True))
# [5, 4, 3, 2, 1, 0]

# ソート(辞書型) -> キーのリストで返る
nums = {"a": 1, "c": 3, "b": 2}
print(sorted(nums))
# ['a', 'b', 'c']
print(sorted(nums.items()))
# [('a', 1), ('b', 2), ('c', 3)]

# リバース -> リストではなく、イテレーターが返る
nums = [0, 4, 1, 2, 3, 5]
print(reversed(nums))
# <list_reverseiterator object at 0x10a4f9f30>
print(list(reversed(nums)))# 並び順を逆にする
# [5, 3, 2, 1, 4, 0]