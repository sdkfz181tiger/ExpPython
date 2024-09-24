# coding: utf-8

"""
位置引数とキーワード引数
"""

#==========
# Main

# 仮引数: parameter
# 実引数: argment

# 位置引数とキーワード引数
def my_func1(one, two, three):
    print(f"{one} {two} {three}?")

# 位置引数
my_func1("Hello", "someone", "there")
# Hello someone there?

# キーワード引数
my_func1(three="serious", one="Are", two="you")
# Are you serious?

# デフォルト値付き
def my_func2(one="Hop", two="Step", three="Jump"):
    print(f"{one}, {two}, {three}!!")

my_func2()
# Hop, Step, Jump!!

#==========
# 可変長位置引数

def my_func3(*args):
    total = 0
    for num in args:
        total += num
    return total

print(my_func3(1, 2, 3, 4, 5))
# 15

# リストやタプルの要素を渡す場合は"*"を付ける
nums = [1, 2, 3, 4, 5]
print(my_func3(*nums))
# 15

nums = (1, 2, 3, 4, 5)
print(my_func3(*nums))
# 15

#==========
# 可変長キーワード引数

def my_func4(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_func4(pref="Aichi", population=300, area=100)
# pref: Aichi
# population: 300
# area: 100

# 辞書を渡す場合は"**"を付ける
dic_mie = {"pref": "Mie", "population": 100, "area": 200}
my_func4(**dic_mie)
# pref: Mie
# population: 100
# area: 200

dic_gifu = {"pref": "Gifu", "population": 100, "area": 300}
my_func4(**dic_gifu)
# pref: Gifu
# population: 200
# area: 300

#==========
# 可変長引数と可変長キーワード引数を同時に使う

# 可変長引数、可変長キーワード引数の順で宣言
def my_func5(*args, **kwargs):
    for num in args:
        print(f"{num}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_func5("My", "favorits", food="Curry", sweets="Pudding", snacks="Chips")
# My
# favorits
# food: Curry
# sweets: Pudding
# snacks: Chips

#==========
# 位置専用引数

# "/"の前は位置専用引数
def my_func6(one, /, two):
    print(f"{one}, {two}")

my_func6("Punch", "Kick")
# Punch Kick

# oneをキーワード指定できない
#my_func6(one="Punch", two="Kick")

#==========
# キーワード専用引数

# "*"の後ろはキーワード専用引数
def my_func7(one, *, two):
    print(f"{one}, {two}")

my_func7("Punch", two="Kick")
# Punch Kick

# twoを位置引数で実行できない
#my_func7("Punch", "Kick")

#==========
# 位置専用引数とキーワード専用引数を同時に使う

def my_func8(one, /, two, *, three):
    print(f"{one}, {two}, {three}")

my_func8("Hop", "Step", three="Jump")
# Hop, Step, Jump

# twoはどちらでも可能
my_func8("Hop", two="Step", three="Jump")
# Hop, Step, Jump

