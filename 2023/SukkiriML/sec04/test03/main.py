# coding: utf-8

"""
スッキリわかる機械学習入門より
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
"""

import pandas as pd
from sklearn import tree

#==========
# Main

# Read
df = pd.read_csv("data.csv")

# Split
x = df[["cm", "kg", "era"]]
t = df["group"]
print(x.head(3))
print(t.head(3))

# Model
model = tree.DecisionTreeClassifier(random_state=0)

# Learn
model.fit(x, t)

# Score
print("Score:", model.score(x, t))

# Predict
columns=["cm", "kg", "era"]
taro = [165, 60, 30]
jiro = [170, 70, 20]
sabu = [175, 75, 10]
bros = [taro, jiro, sabu]
df = pd.DataFrame(bros, columns=columns)
print(model.predict(df))