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
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

COL_X = ["pclass", "age", "sib_sp", "parch", "fare"]
COL_Y = "survived"
MY_CSV = "my_survived.csv"

def main():
    """ Main """
    print("main!!")

    # ランダムフォレスト
    # 複数の決定木を生成し、多数決するアンサンブル方式
    # 決定木は、特徴量と訓練データをランダムに選び様々なものが作られる
    # 通常の決定木に比べて過学習を防ぐことができる

    df = pd.read_csv(MY_CSV)
    print(df.head(3))
    print(df.tail(3))

    # ピボットテーブルで確認
    # (客室クラス別の死亡/生存の平均年齢)
    print(df.pivot_table(
        index="pclass", 
        columns="survived", 
        values="age"))

    # ピボットテーブルを参考にして欠損値を穴埋め
    # 決定木では、外れ値の影響はほぼ無いので外れ値は考慮しない
    # 標準化処理もほぼ影響しないので考慮しない
    df = fill_age(df, 1, 0, 23) # 客室クラス1での死亡者の年齢を23に
    df = fill_age(df, 1, 1, 35) # 客室クラス1での生存者の年齢を35に
    df = fill_age(df, 2, 0, 33) # 客室クラス2での死亡者の年齢を33に
    df = fill_age(df, 2, 1, 25) # 客室クラス2での生存者の年齢を25に
    df = fill_age(df, 3, 0, 26) # 客室クラス3での死亡者の年齢を26に
    df = fill_age(df, 3, 1, 20) # 客室クラス3での生存者の年齢を20に

    # 特徴量と正解データに分割
    x = df[COL_X]
    y = df[COL_Y]

    # sex列をダミー変数化
    dummy = pd.get_dummies(df["sex"], drop_first=True, dtype=int)
    x = pd.concat([x, dummy], axis=1) # 列方向に連結
    print(x.head(3))
    print(x.tail(3))

    # 訓練データと検証データに分割
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=0)

    # ランダムフォレストで学習
    # n_estimators: 決定木の数
    model_rf = RandomForestClassifier(n_estimators=200, random_state=0)
    model_rf.fit(x_train, y_train)

    # ランダムフォレストScore
    print("ランダムフォレストScore(訓練データ):", model_rf.score(x_train, y_train))
    print("ランダムフォレストScore(検証データ):", model_rf.score(x_test, y_test))
    # ランダムフォレストScore(訓練データ): 0.9859550561797753
    # ランダムフォレストScore(検証データ): 0.8938547486033519 <- 驚き!!

    # 通常の決定木Score
    model_n = tree.DecisionTreeClassifier(random_state=0)
    model_n.fit(x_train, y_train)
    print("通常の決定木Score(訓練データ):", model_n.score(x_train, y_train))
    print("通常の決定木Score(検証データ):", model_n.score(x_test, y_test))
    # 通常の決定木Score(訓練データ): 0.9859550561797753
    # 通常の決定木Score(検証データ): 0.8268156424581006

    # ランダムフォレストの重要度を確認
    importance = model_rf.feature_importances_
    print(pd.Series(importance, index=x_train.columns))

    """
    pclass    0.089058
    age       0.330516
    sib_sp    0.047386
    parch     0.030274
    fare      0.250802
    male      0.251963
    """


def fill_age(df, pclass, survived, value):
    df.loc[
        (df["pclass"] == pclass) &
        (df["survived"] == survived) &
        (df["age"].isnull()), "age"] = value
    return df



if __name__ == "__main__":
    main()