# coding: utf-8

"""
ジェネレーター
"""

#==========
# Main

import re

# 等差数列の和
# 初項:1, 等差:1

# 1 + 2 + 3 + ...
def my_gen1():
    num = 1
    total = num
    while True:
        yield total # 結果を返し一時停止
        num += 1
        total += num # 次の呼び出しで実行

# ジェネレーターオブジェクト
gen = my_gen1()
print(gen)
# <generator object my_gen1 at 0x1092347c0>

# イテレーション
print(next(gen))
# 1
print(next(gen))
# 3
print(next(gen))
# 6

# 等比数列の和
# 初項:1, 公比:2

# 1 + 2 + 4 + ...
def my_gen2():
    num = 1
    total = num
    while True:
        yield total
        num *= 2
        total += num

gen = my_gen2()
print(gen)
# <generator object my_gen2 at 0x104534a00>

# イテレーション
print(next(gen))
# 1
print(next(gen))
# 3
print(next(gen))
# 7

#==========
# ジェネレーターで大きなファイルを扱う

# 1行づつ取り出す
def search_text(path, pattern):
    with open(path, mode="r") as f:
        for row in f:
            if re.match(pattern, row):
                yield row.strip()

# "吾輩は...。"のパターンで始まる行のみを取り出す
for row in search_text("./story.txt", "^(\s*吾輩は).*\n$"):
    print(row)

# 吾輩は猫である。
# 吾輩はここで始めて人間というものを見た。
# ...(省略)
# 吾輩は死ぬ。
