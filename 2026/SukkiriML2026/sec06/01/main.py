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
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree

COL_X    = ["gaku_nagasa", "gaku_haba", "kaben_nagasa", "kaben_haba"]
COL_Y    = "type"
MY_CSV   = "my_iris.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")
	
	df = pd.read_csv(MY_CSV)
	print(df.head(3))
	print(df.tail(3))

	


if __name__ == "__main__":
	main()