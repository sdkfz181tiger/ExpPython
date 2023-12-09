# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-2: 
	単語の出現回数を数えてみよう
"""

import math

print("Hello, Python!!")

# テキスト文章
text = """
Keep on asking, and it will be given you.
Keep on seeking, and you will find.
Keep on knocking, and it will be opened to you.
for everyone asking receives, and everyone seeking finds.
and to everyone knocking. it will be opened.
"""

# 不要な文字を削除
text = text.replace(",", "")
text = text.replace(".", "")

# 単語を区切る
words = text.split()# 空白で分割

# 辞書型
counter = {}
for word in words:
	w = word.lower()
	if w in counter:
		counter[w] += 1# カウントアップ
	else:
		counter[w] = 1# カウント初期値

# 一覧を表示
print(counter)

print("|    key    | value |")
for k, v in sorted(counter.items()):
	print("| {0:<9} | {1:>5} |".format(k, v))