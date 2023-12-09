# coding: utf-8

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# KNeighbors
print("Hello KNeighbors!!")

# 学習用データ(X, Y)
learn_input = [[0, 0], [1, 0], [0, 1], [1, 1]]

# 結果データ
#learn_output = [0, 0, 0, 1]# (X and Y)  -> 1.0
#learn_output = [0, 1, 1, 1]# (X or Y)  -> 1.0
learn_output = [0, 1, 1, 0]# (X xor Y) -> 1.0

# アルゴリズム
clf = KNeighborsClassifier(n_neighbors = 1)

# 学習
clf.fit(learn_input, learn_output)

# 予測
test_input = [[0, 0], [1, 0], [0, 1], [1, 1]]
test_output = clf.predict(test_input)

# 評価
print(test_input, "の予測結果", test_output)
print("正解率:", accuracy_score(learn_output, test_output))

