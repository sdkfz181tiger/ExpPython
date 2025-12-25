# coding: utf-8

"""
Python3認定基礎試験サンプルコード
"""

import math

# if文
x = 2
if x < 0:
    x = 0
    print("負数は0にする")
elif x == 0:
    print("0である")
elif x == 1:
    print("1である")
else:
    print("もっと上である")
# もっと上である

# for文

member = ["承太郎", "ジョセフ", "アブドゥル", "花京院", "ポルナレフ"]
for person in member:
    print(person, len(person))

# 承太郎 3
# ジョセフ 4
# アブドゥル 5
# 花京院 3
# ポルナレフ 5

# for
for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

for i in range(len(member)):
    print(i, member[i], len(member[i]))

# 承太郎 3
# ジョセフ 4
# アブドゥル 5
# 花京院 3
# ポルナレフ 5

# for-else: 素数を判定する
limit = 30
for n in range(2, limit):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(str(n) + " is prime number!!")

# while
i = 0
while i < 5:
    print(i)
    i = i + 1

# while: フィボナッチ数(次の数は直前2つの数値の和になる数列の事)
a, b = 0, 1
while a < limit:
    a, b = b, a + b
    print(a)






