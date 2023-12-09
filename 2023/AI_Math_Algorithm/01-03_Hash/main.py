# coding: utf-8

"""
AIx数学xアルゴリズム
"""

import hashlib

# Hash値を扱う組み込み関数
t_def = "Ogaki".encode()
t_hash = hashlib.sha256(t_def).hexdigest()
print(t_hash)

data = ["Sendai", "Tokyo", "Nagoya", "Osaka", "Fukuoka"]

# Hash値(自作)を返す関数
def get_hash(text):
	h = 0
	for t in text:
		h = h * 104683 + ord(t) # 適当な素数にコードポイントを加算
	return h % 103451 # 素数を使うと衝突しにくい

# Hashテーブル
table = [-1] * 103451 # -1が格納された配列
for d in data:
	table[get_hash(d)] = d

# Test
print(table[get_hash("Atami")])