# coding: utf-8

"""
Wine学習データ
	https://archive.ics.uci.edu/ml/datasets/wine+quality
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# RandomForest
print("Hello RandomForest!!")

# CSVファイル
csv_wine = pd.read_csv("./winequality-white.csv", sep=";", encoding="utf-8")

# 入力データとラベルに分離
x = csv_wine.drop("quality", axis=1)
y = csv_wine["quality"]

# テスト用20%、学習用80%に分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 学習
clf = RandomForestClassifier()
clf.fit(x_train, y_train)

# 評価
y_pred = clf.predict(x_test)
print(classification_report(y_test, y_pred))
print("正解率:", accuracy_score(y_test, y_pred))