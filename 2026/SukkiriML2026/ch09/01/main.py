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
from sklearn.preprocessing import StandardScaler
from sklearn.tree import plot_tree

MY_CSV   = "my_bank.csv"
MY_MODEL = "my_model.pkl"

def main():
    """ Main """
    print("main!!")

    df = pd.read_csv(MY_CSV)
    print(df.head(3))
    print(df.tail(3))

if __name__ == "__main__":
    main()