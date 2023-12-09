# coding: utf-8

"""
MeCab:
	https://taku910.github.io/mecab/
1, インストール:
	brew install mecab mecab-ipadic git curl xz
	pip install mecab-python3
2, mecab-ipadic-NEllogd(最新の単語辞書):
	git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
	cd mecab-ipadic-neologd
	./bin/install-mecab-ipadic-neologd -n -p /var/lib/mecab/dic/mecab-ipadic-neologd
"""

import MeCab
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# MeCab
print("Hello MeCab!!")

# Mecabオブジェクト(辞書を指定)
tagger = MeCab.Tagger("-d /var/lib/mecab/dic/mecab-ipadic-neologd")
tagger.parse("")

txt = "近所の公園で平将門が恋ダンスを死霊の盆踊りスタイルで踊っている。"

# 形態素解析
# result = tagger.parse(txt)
# print(result)

# 形態素解析結果をリストで取得
node = tagger.parseToNode(txt)
result = []

while node is not None:
	# 品詞
	hinshi = node.feature.split(",")[0]
	if hinshi in ["名詞"]:
		# 表層形の取得
		result.append(node.surface)
	elif hinshi in ["動詞", "形容詞"]:
		# 形態素情報から原形情報を取得
		result.append(node.feature.split(",")[6])
	node = node.next

print(result)