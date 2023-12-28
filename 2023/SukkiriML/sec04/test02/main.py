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
print("先頭3件:", df.head(3))
print("末尾3件:", df.tail(3))

# cm(Series)
print(df["cm"].head(3))
# kg and era(DataFrame)
print(df[["kg", "era"]].head(3))

# Split
x = df[["cm", "kg", "era"]]
t = df["group"]
print(x.head(3))
print(t.head(3))