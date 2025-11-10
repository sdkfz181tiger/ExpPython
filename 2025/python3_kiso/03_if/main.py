# coding: utf-8

"""
Python3認定基礎試験サンプルコード
"""

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

for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

for i in range(len(member)):
    print(i, member[i], len(member[i]))