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
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

COL_X  = ["rm", "ptratio", "lstat"]
COL_Y  = ["price"]
MY_CSV = "my_boston.csv"

def main():
    """ Main """
    print("main!!")

    # ラッソ回帰
    # 特徴: 不要な特徴量を削除した上で回帰式を作成
    # 回帰式は以下の様な式になる。
    # y = a * x1 + b * x2 + c * x3 + d
    # 上記回帰式との4つのデータとの誤差を、
    # それぞれe1, e2, e3としたとき、
    # E = e1^2 + e2^2 + e3^2 (誤差の二乗和)
    # F = |a| + |b| + |c| + |d| (係数の絶対値の和) <- リッジ回帰との違い
    # L = E + F
    # 上記Lが最小となるような回帰式の係数a, bを求める。
    # 更に、F(正則化項)に対して定数を掛け算し、最適な値を導き出す。
    # (定数は、0以上の値で、0.01刻みでテストを繰り返す)
    # L = E + 0.5 x F

    df = pd.read_csv(MY_CSV)
    print(df.head(3))
    print(df.tail(3))

    df = df.loc[:, "zn":"price"] # 全ての行、zn~priceまでの列
    print(df.isnull().sum()) # 欠損値を確認
    df = df.fillna(df.mean()) # 欠損値を平均値で穴埋め
    df = df.drop([76], axis=0) # 外れ値の行を削除
    print(df.isnull().sum()) # 欠損値を確認

    # 訓練データと正解データに分割
    x = df[COL_X]
    y = df[COL_Y]

    # 標準化
    sc1 = StandardScaler()
    sc_x = sc1.fit_transform(x)
    print(sc_x.shape) # (99, 3)

    sc2 = StandardScaler()
    sc_y = sc2.fit_transform(y)

    # 累乗列と交互作用特徴量を一括追加
    pf = PolynomialFeatures(degree=2, include_bias=False)
    pf_x = pf.fit_transform(sc_x)
    print(pf_x.shape) # (99, 9) <- 特徴量が増えている

    # 追加された特徴量の列名を確認
    # ['x0' 'x1' 'x2' 'x0^2' 'x0 x1' 'x0 x2' 'x1^2' 'x1 x2' 'x2^2']
    print(pf.get_feature_names_out())

    # 線形回帰で過学習が起こる事を確認
    # 特徴量を増やした事によって、過学習が起こりやすくなっている
    x_train, x_test, y_train, y_test = train_test_split(pf_x, sc_y,
        test_size=0.3, random_state=0)
    model = LinearRegression()
    model.fit(x_train, y_train)
    # スコア(過学習が起きている)
    print("訓練データスコア(通常):", model.score(x_train, y_train)) # 0.87...
    print("テストデータスコア(通常):", model.score(x_test, y_test)) # 0.78...

    # リッジ回帰で過学習が抑えられるか確認
    # alpha: 正規化項につく定数
    # 最低値が0であり、実際には0.01刻みでテストを繰り返す
    model_lasso = Lasso(alpha=0.1)
    model_lasso.fit(x_train, y_train)
    print("訓練データスコア(ラッソ):", model_lasso.score(x_train, y_train)) # 0.82...
    print("テストデータスコア(ラッソ):", model_lasso.score(x_test, y_test)) # 0.85...

    # 回帰式の係数を確認する
    weight = model_lasso.coef_
    print(weight)

    """ 回帰式の係数(無駄な係数が0になっている!!)
    [ 0.40942617
    -0.08310439
    -0.28771435
    0.15000106
    -0.
    -0.03744993
    -0.
    0.
    0.]
    """


if __name__ == "__main__":
    main()