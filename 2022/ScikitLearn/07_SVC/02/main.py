# coding: utf-8

"""
手書き数字データ
	https://archive.ics.uci.edu/ml/datasets/optical+recognition+of+handwritten+digits
"""

import os, pickle
from sklearn import datasets, svm, metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# SVC
print("Hello SVC!!")

PATH_PKL = "./digits.pkl"

# 手書き数字の読込
digits = datasets.load_digits()
x = digits.images
y = digits.target
# 二次元配列から一次元配列に変換
x = x.reshape(-1, 64)
# データを学習用とテスト用に分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 学習済データを保存
def save_clf(clf):
	with open(PATH_PKL, "wb") as fp: 
		pickle.dump(clf, fp)

# 学習済データの読込
def load_clf():
	if os.path.isfile(PATH_PKL): 
		with open("digits.pkl", "rb") as fp: 
			return pickle.load(fp)
	# 学習
	clf = svm.SVC()
	clf.fit(x_train, y_train)
	save_clf(clf)# Save
	return clf

# 予測
clf = load_clf()
y_pred = clf.predict(x_test)
print("正解率:", accuracy_score(y_test, y_pred))