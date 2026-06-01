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

MY_CSV = "my_iris.csv"

def main():
    """ Main """
    print("main!!")

    df_iris = pd.read_csv(MY_CSV)
    #print(df_iris.head(3))
    #print(df_iris.tail(3))

    # 学習用データを用意(欠損値を含む行を削除)
    df_train = df_iris.dropna()
    x = df_train.loc[:, "gaku_haba":"kaben_haba"]
    y = df_train["gaku_nagasa"]

    # モデルを学習
    model = LinearRegression()
    model.fit(x, y)

    # 欠損値を含む行を用意
    condition = df_iris["gaku_nagasa"].isnull()
    df_none = df_iris.loc[condition]
    print(df_none.head(3)) # 61行目、137行目が欠損

    # モデルで予測
    x = df_none.loc[:, "gaku_haba":"kaben_haba"]
    y = model.predict(x)

    # 欠損値を補完
    df_iris.loc[condition, "gaku_nagasa"] = y
    print("61行目", df_iris.loc[61, "gaku_nagasa"]) # 61行目を確認
    print("137行目", df_iris.loc[137, "gaku_nagasa"]) # 137行目を確認


if __name__ == "__main__":
    main()