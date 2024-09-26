# coding: utf-8

"""
copyモジュール
"""

#==========
# Main

import copy

# 参照を使ったコピー(参照する)
values = ["a", "b", "c", "d"]# リセット
copied = values
copied[1] = "B"
print(f"copied: {copied}")
# copied: ['a', 'B', 'c', 'd']
print(f"values: {values}")# 元のオブジェクトも変更されている
# values: ['a', 'B', 'c', 'd']

# copy関数を使ったコピー(クローン)
values = ["a", "b", "c", "d"]# リセット
copied = copy.copy(values)
copied[1] = "B"
print(f"copied: {copied}")
# copied: ['a', 'B', 'c', 'd']
print(f"values: {values}")# 元のオブジェクトは変更されない(成功)
# values: ['a', 'b', 'c', 'd']

# 2階層先の場合は参照になってしまう
values = [["a", "b"], ["c", "d"], ["e", "f"]]# リセット
copied = copy.copy(values)
copied[1][1] = "D"
print(f"copied: {copied}")
# copied: [['a', 'b'], ['c', 'x'], ['e', 'f']]
print(f"values: {values}")# 元のオブジェクトも変更されている(失敗)
# values: [['a', 'b'], ['c', 'D'], ['e', 'f']]

# deepcopy関数を使って再帰的にコピー(完全なクローン)
values = [["a", "b"], ["c", "d"], ["e", "f"]]# リセット
copied = copy.deepcopy(values)
copied[1][1] = "D"
print(f"copied: {copied}")
# copied: [['a', 'b'], ['c', 'D'], ['e', 'f']]
print(f"values: {values}")# 元のオブジェクトは変更されない(成功)
# values: [['a', 'b'], ['c', 'd'], ['e', 'f']]
