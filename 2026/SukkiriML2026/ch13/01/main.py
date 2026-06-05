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
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

MY_CSV = "my_cinema.csv"

def main():
    """ Main """
    print("main!!")

    # 回帰の予測性能評価

    df = pd.read_csv(MY_CSV)
    print(df.head(3))
    print(df.tail(3))

    df = df.fillna(df.mean(numeric_only=True)) # 欠損値を平均値で穴埋め
    print(df.isnull().sum()) # 欠損値を確認

    x = df.loc[:, "sns1":"original"]
    y = df["sales"]

    model = LinearRegression()
    model.fit(x, y)

    # 予測
    pred = model.predict(x)
    
    # 予測値と実際の値の誤差を平均二乗誤差で求める
    mse = mean_squared_error(pred, y)
    print("mse:", mse)
    # mse: 151986.03957624524

    # 二乗平均平方根誤差を求める
    # 平方根を取っている為、外れ値の影響を大きく受けてしまう
    rmse = math.sqrt(mse)
    print("rmse:", rmse)
    # rmse: 389.8538695155471


if __name__ == "__main__":
    main()