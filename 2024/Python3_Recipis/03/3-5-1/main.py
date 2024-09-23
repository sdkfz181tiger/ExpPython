# coding: utf-8

"""
内包表記
"""

#==========
# Main

# 0 ~ 10までのリスト
nums = [i for i in range(10)]
print(nums)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 偶数のみ
evens = [i for i in range(10) if i%2==0]
print(evens)
# [0, 2, 4, 6, 8]

# 奇数のみ
odds = [i for i in range(10) if i%2!=0]
print(odds)
# [1, 3, 5, 7, 9]

# ネスト1(九九表をリストで取得)
kuku = [a*b for a in range(1,10) for b in range(1,10)]
print(kuku)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, ...45, 54, 63, 72, 81]

# ネスト2(九九表をセットで取得)
kuku = {a*b for a in range(1,10) for b in range(1,10)}
print(kuku)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, ...56, 63, 64, 72, 81}

# ネスト3(九九表をジェネレーターで取得)
kuku = (a*b for a in range(1,10) for b in range(1,10))
print(kuku)
# <generator object <genexpr> at 0x10bfd4ba0>

# ジェネレーターからデータを取り出す時に作成される
for i in kuku:
    print(i)
# 0 1 2 3...

# ネスト4(リスト同士の組み合わせ)
drinks = ["Coffe", "Tea", "Miso"]
sizes = ["S", "M", "L"]
menu = [(drink, size) for drink in drinks for size in sizes]
print(menu)
# [('Coffe', 'S'), ('Coffe', 'M'), ('Coffe', 'L'), 
# ('Tea', 'S'), ('Tea', 'M'), ('Tea', 'L'), 
# ('Miso', 'S'), ('Miso', 'M'), ('Miso', 'L')]

# ネスト5(辞書で取得)
drinks = ["Coffe", "Tea", "Miso"]
sizes = ["S", "M", "L"]
menu = {drink: size for drink in drinks for size in sizes}
print(menu)
# {'Coffe': 'L', 'Tea': 'L', 'Miso': 'L'}
