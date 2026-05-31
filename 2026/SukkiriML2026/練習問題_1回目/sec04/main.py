# coding: utf-8

"""
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
	$ python3 -m pip install matplotlib
"""

import pandas as pd
import pickle
import os.path
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

COL_X    = ["sns1", "sns2", "actor", "original"]
COL_Y    = "sales"
MY_CSV   = "ex1.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")
	
	df = pd.read_csv(MY_CSV)
	#print(df.head(3))
	#print(df.tail(3))

	# 行
	#print(df.index)

	# 列
	#print(df.columns)

	# 特定の列のみ
	print(df[["x0", "x2"]])


if __name__ == "__main__":
	main()