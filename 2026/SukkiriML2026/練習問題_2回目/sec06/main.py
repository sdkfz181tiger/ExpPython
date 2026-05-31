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
from sklearn.metrics import mean_absolute_error

COL_X    = ["x0", "x1", "x2", "x3"]
COL_Y    = "target"
MY_CSV   = "ex3.csv"
MY_MODEL = "my_model.pkl"

def main():
	""" Main """
	print("main!!")
	
	

if __name__ == "__main__":
	main()