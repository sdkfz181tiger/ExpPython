# coding: utf-8

"""
アンパック
"""

#==========
# Main

# タプルのアンパック
a, b, c = (1, 2, 3)
print(f"{a}, {b}, {c}")
# 1, 2, 3

# タプルの"()"は省略可能
a, b, c = 1, 2, 3
print(f"{a}, {b}, {c}")
# 1, 2, 3

# リストのアンパック
a, b, c = [1, 2, 3]
print(f"{a}, {b}, {c}")
# 1, 2, 3

# ディクショナリ(キー)
key1, key2, key3 = {"a": 1, "b": 2, "c": 3}
print(f"{key1}, {key2}, {key3}")

# ディクショナリ(値)
val1, val2, val3 = {"a": 1, "b": 2, "c": 3}.values()
print(f"{val1}, {val2}, {val3}")

#==========
# ネストしたタプル、リスト

# 変数とタプルにアンパック
a, b, c = (0, 1, (2, 3, 4))
print(f"{a}, {b}, {c}")
# 0, 1, (2, 3, 4)

# それぞれの変数にアンパック
a, b, (c, d, e) = (0, 1, (2, 3, 4))
print(f"{a}, {b}, {c}, {d}, {e}")
# 0, 1, 2, 3, 4

#==========
# *を使ったアンパック

a, b, *c = (0, 1, 2, 3, 4)
print(f"{a}, {b}, {c}")
# 0, 1, [2, 3, 4]

a, *b, c = (0, 1, 2, 3, 4)
print(f"{a}, {b}, {c}")
# 0, [1, 2, 3], 4

*a, b, c = (0, 1, 2, 3, 4)
print(f"{a}, {b}, {c}")
# [0, 1, 2], 3, 4

# *を2つ使うとエラー
#*a, *b, c = (0, 1, 2, 3, 4)

#==========
# リスト, 辞書のアンパック

def my_func(a, b, c):
	print(f"{a}, {b}, {c}")

# リストを位置引数にアンパック
commands = ["Punch", "Kick", "Chop"]
my_func(*commands)
# Punch, Kick, Chop

# 辞書をキーワード引数にアンパック
commands = {"a": "Punch", "b": "Kick", "c": "Chop"}
my_func(**commands)
# Punch, Kick, Chop

