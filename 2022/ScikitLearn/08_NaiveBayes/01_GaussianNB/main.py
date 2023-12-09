# coding: utf-8

"""
言語判定処理
"""

import glob
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Unicode 0 ~ FFFF
UNICODE_MIN = 0
UNICODE_MAX = 65535

# NaiveBayes
print("Hello NaiveBayes!!")

# Unicodeコードポイント頻度測定
def cnt_cp(txt):
	# Unicodeコードポイントをカウントする配列
	counter = np.zeros(UNICODE_MAX)
	for i in range(len(txt)):
		code_point = ord(txt[i])
		if code_point > UNICODE_MAX: continue
		counter[code_point] += 1
	# 各要素を文字数で割って正規化
	counter = counter / len(txt)
	return counter

# 学習用データ
str_ja = "こんにちは、これは日本語です。ご機嫌はいかがですか?"
str_en = "Hello, this is Japanese. how are you doing today?"
str_la = "Salve, haec Iaponica. quid agis hodie?"

x_train = [cnt_cp(str_ja), cnt_cp(str_en), cnt_cp(str_la)]
y_train = ["ja", "en", "la"]

# 学習
clf = GaussianNB()
clf.fit(x_train, y_train)

# 評価用データ
str_ja_test = "こんにちは"
str_en_test = "Hello"
str_la_test = "Salve"

x_test = [cnt_cp(str_ja_test), cnt_cp(str_en_test), cnt_cp(str_la_test)]
y_test = ["ja", "en", "la"]

# 評価
y_pred = clf.predict(x_test)
print(y_pred)
print("正解率:", accuracy_score(y_test, y_pred))
