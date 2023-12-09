# coding: utf-8

"""
Iris学習データ(クジラ飛行机先生のGitHubから)
	https://github.com/kujirahand/book-mlearn-gyomu/blob/master/src/ch2/iris/iris.csv
"""

import pandas as pd
import warnings
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.utils import all_estimators
from sklearn.model_selection import train_test_split

# Algorithms
print("Hello Algorithms!!")

# CSVファイル
csv_iris = pd.read_csv("./iris.csv", encoding="utf-8")

# 入力データとラベルに分離
x = csv_iris.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
y = csv_iris.loc[:, "Name"]

# テスト用20%、学習用80%に分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)

# Classifierのアルゴリズム全て
algorithms = all_estimators(type_filter="classifier")
warnings.simplefilter("error")

for(name, algorithm) in algorithms:
	try:
		# 学習
		clf = algorithm()
		clf.fit(x_train, y_train)

		# 評価
		y_pred = clf.predict(x_test)
		print(name, "の正解率:", accuracy_score(y_test, y_pred))
	except Warning as w:
		print("\033[33m" + "Warning:" + "\033[0m", name, ":", w.args)
	except Exception as e:
		print("\033[33m" + "Warning:" + "\033[0m", name, ":", e.args)