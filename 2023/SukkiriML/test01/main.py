# coding: utf-8

"""
スッキリわかる機械学習入門より
1, Install
	$ python3 -m pip install pandas
"""

import pandas as pd

#==========
# Data(Dictionary)
data = {
	"Ariel":[160, 160, 160],
	"Becky":[150, 175, 125]
}

# Pandas
df = pd.DataFrame(data)
print(df)# 表
print(df.shape)# 列数と行数

# インデックス名の変更
df.index = ["Jan", "Feb", "Mar"]
print(df)

# カラム名の変更
df.columns = ["Alex", "Boby"]
print(df)

#==========
# Data(Matrix)
data = [
	[160, 150],
	[160, 175],
	[160, 125]
]

# 2次元リストからデータフレームを作る
df = pd.DataFrame(data, 
	index=["Jan", "Feb", "Mar"],
	columns=["Alex", "Boby"])
print(df)
