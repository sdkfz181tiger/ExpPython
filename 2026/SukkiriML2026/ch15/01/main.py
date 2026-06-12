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
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

MY_CSV = "my_wholesales.csv"

def main():
    """ Main """
    print("main!!")

    # クラスタリング

    # 推敲中...

    df = pd.read_csv(MY_CSV)
    print(df.head(3))

    


if __name__ == "__main__":
    main()