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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold

MY_CSV = "my_cinema.csv"

def main():
    """ Main """
    print("main!!")

    # K分割交差検証
    # 訓練&検証データをK個に分割し、組み合わせを変えつつ学習を行う方法です
    # (外れ値が偏って分割された場合、学習結果に悪影響が出てしまう為)
    # ex:
    # 仮にデータをA, B, Cに3分割した場合、次のパターンでそれぞれ学習を行う
    # 1, A&Bを訓練データ、Cを検証データ
    # 2, C&Aを訓練データ、Bを検証データ
    # 3, B&Cを訓練データ、Aを検証データ
    # 最終的に、それぞれの学習結果の平均値を取る

    df = pd.read_csv(MY_CSV)
    print(df.head(3))
    print(df.tail(3))

    df = df.fillna(df.mean()) # 欠損値を埋める

    x = df.loc[:, "sns1":"original"]
    y = df["sales"]

    # KFold
    # n_splits: 分割数
    kf = KFold(n_splits=3, shuffle=True, random_state=0)

    model = LinearRegression()

    # cv: 分割条件
    # scoring: 評価指標の指定(決定係数)
    c_validate = cross_validate(
        model, x, y, 
        cv=kf, scoring="r2", 
        return_train_score=True)
    print(c_validate)

    """
    {
    'fit_time': array([0.01137495, 0.00104189, 0.00094008]), 
    'score_time': array([0.00089383, 0.00068784, 0.0006578 ]), 
    'test_score': array([0.72465051, 0.71740834, 0.75975591]), <- 検証データでの3回の決定係数値 
    'train_score': array([0.76928501, 0.76368104, 0.75780074]) <- 訓練データでの決定係数値
    }
    """

    # 平均値を計算
    result = sum(c_validate["test_score"]) / len(c_validate["test_score"])
    print("result:", result)
    # result: 0.7339382541774341


if __name__ == "__main__":
    main()