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
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

MY_CSV = "my_iris.csv"

def main():
    """ Main """
    print("main!!")

    # ロジスティック回帰
    # 分類する為の回帰式を作成し、それを利用して分類を行います。
    # 基本的には、確率が最も大きい結果を採用します。

    df = pd.read_csv(MY_CSV)
    print(df.head(3))
    print(df.tail(3))

    df = df.fillna(df.mean(numeric_only=True)) # 欠損値を平均値で穴埋め
    print(df.isnull().sum()) # 欠損値を確認
    
    x = df.loc[:, :"kaben_haba"] # 全ての行、kaben_habaまでの列
    y = df["type"]
    
    # 特徴量を標準化(ロジスティック回帰には必須)
    sc = StandardScaler()
    sc_x = sc.fit_transform(x)

    # 訓練データ、検証データに分割
    x_train, x_test, y_train, y_test = train_test_split(
        sc_x, y, test_size=0.2, random_state=0)

    # ロジスティック回帰
    # C: 正則化項の定数(小さくすると過学習を抑えられる可能性がある)
    # solver: 最適化アルゴリズムを指定
    # multi_class: <- Deprecated
    model = LogisticRegression(random_state=0,
        C=0.1, solver="lbfgs")

    # 正解率を確認する
    model.fit(x_train, y_train)
    print("Score(訓練データ):", model.score(x_train, y_train))
    print("Score(検証データ):", model.score(x_test, y_test))

    # 係数を確認する
    print(model.coef_)

    """
    # 特徴量が4つ、正解データが3つなので、下記の様な式になる
    # 回帰式: a * x1 + b * x2 + c * x3 + d
    [[-0.53168668  0.48573155 -0.52638431 -0.83213317] <- virginicaの式の係数
    [ 0.09482289 -0.44707757 -0.00107471 -0.04407356]  <- versicolorの式の係数
    [ 0.4368638  -0.03865398  0.52745902  0.87620673]] <- setosaの式の係数
    """

    # 実際にテスト(結果のみ)
    new_x = [[1, 2, 3, 4]]
    print("Test:", model.predict(new_x))
    # Test: ['Iris-virginica']

    # 実際にテスト(確率込み)
    print("Classes:", model.classes_)
    # Classes: ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
    print("Test:", model.predict_proba(new_x))
    # Test: [[4.02790964e-05 3.02983301e-03 9.96929888e-01]]


if __name__ == "__main__":
    main()