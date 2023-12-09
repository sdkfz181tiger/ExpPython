# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter2-4: 
	時給計算プログラムを作ってみよう
"""

print("Hello, Python!!")

# ユーザーからの入力
user = input("時給はいくらですか!?")

# 整数に変換する
n_jikyuu = int(user)

# ユーザーからの入力
user = input("何時間働きましたか!?")
n_jikan = int(user)

# 計算する
n_kyuryo = n_jikyuu * n_jikan

# 結果を表示
fmt = """
あなたの給料は...
時給{0}円 * {1}時間 = 給料{2}円
です!!
"""

msg = fmt.format(n_jikyuu, n_jikan, n_kyuryo)
print(msg)
