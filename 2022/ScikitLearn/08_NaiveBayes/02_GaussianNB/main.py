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

# 学習用データ(テキストデータから取得)
index = 0
x_train = []
y_train = []
for file in glob.glob("./train/*.txt"):
	txt = ""
	for line in open(file, "r"):
		txt = txt + line
	x_train.append(cnt_cp(txt))
	y_train.append(file[8:10])

# 学習
clf = GaussianNB()
clf.fit(x_train, y_train)

# 評価用データ
index = 0
x_test = []
y_test = []
for file in glob.glob("./test/*.txt"):
	txt = ""
	for line in open(file, "r"):
		txt = txt + line
	x_test.append(cnt_cp(txt))
	y_test.append(file[7:9])

# 評価
y_pred = clf.predict(x_test)
print(y_pred)
print("正解率:", accuracy_score(y_test, y_pred))