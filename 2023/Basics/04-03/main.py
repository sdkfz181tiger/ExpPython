# coding: utf-8

# 04-03: Scikit-Learn

import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets
import pandas as pd

print("sklearn:", sklearn.__version__)
print("pandas:", pd.__version__)

# アヤメデータを取り込み
iris = datasets.load_iris()
# print(iris.feature_names)
# print(iris.data)

# Pandasを使う
#dataset = ["a1", "a2", "a3"]
#print(pd.DataFrame(dataset))

# Pandasで表形式にして確認
print(pd.DataFrame(iris.data, columns=iris.feature_names))

# 最初の1つの特徴量(length)を確認 -> 萼片の長さ
first_one_feature = iris.data[:, :1]
print(pd.DataFrame(first_one_feature, columns=iris.feature_names[:1]))

# 最初の2つの特徴量(length, width)を確認 -> 萼片の長さと幅
first_two_feature = iris.data[:, :2]
print(pd.DataFrame(first_two_feature, columns=iris.feature_names[:2]))

# 最後の2つの特徴量(length, width)を確認 -> 花弁の長さと幅
last_two_feature = iris.data[:, 2:]
print(pd.DataFrame(last_two_feature, columns=iris.feature_names[2:]))

# 教師ラベルデータ(0: Setosa, 1: Versicolour, 2: Virginica)
teacher_labels = iris.target
print(teacher_labels)

# 全てのアヤメデータ
all_features = iris.data

#=====
# 1, 2列目のデータ(萼片)を使う
# x_min, x_max = all_features[:, 0].min(), all_features[:, 0].max()
# y_min, y_max = all_features[:, 1].min(), all_features[:, 1].max()
# plt.figure(2, figsize=(12, 9))
# plt.clf()

# 散布図
# plt.scatter(all_features[:, 0], all_features[:, 1], 
# 	s=300, c=teacher_labels, cmap=plt.cm.Set2, edgecolor="darkgray")
# plt.xlabel("Sepal length")
# plt.ylabel("Sepal width")
# plt.grid(True)
# plt.show()

##=====
# 3, 4列目のデータ(花弁)を使う
x_min, x_max = all_features[:, 2].min(), all_features[:, 3].max()
y_min, y_max = all_features[:, 2].min(), all_features[:, 3].max()
plt.figure(2, figsize=(12, 9))
plt.clf()

# 散布図
plt.scatter(all_features[:, 2], all_features[:, 3], 
	s=300, c=teacher_labels, cmap=plt.cm.Set2, edgecolor="darkgray")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.grid(True)
plt.show()

