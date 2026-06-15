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

def main():
    """ Main """
    print("main!!")

    # データフレーム(二次元リスト)
    scores = {
        "math":    [77, 85, 65, 85, 90], 
        "english": [70, 80, 68, 77, 65],
        "history": [65, 75, 80, 85, 45],
        "science": [80, 75, 60, 70, 85],
        "sex":     [0,   1,  1,  0,  0], # 性別
        "grade":   [1,   2,  1,  2,  1]  # 学年
    }
    df = pd.DataFrame(scores, index=[
        "yamada", "kawaguti", "umino", "shimada", "morita"])
    print(df)
    """
              math  english  history  science  sex  grade
    yamada      77       70       65       80    0      1
    kawaguti    85       80       75       75    1      2
    umino       65       68       80       60    1      1
    shimada     85       77       85       70    0      2
    morita      90       65       45       85    0      1
    """

    # 列ごと(math ~ science)の合計値
    print(df.loc[:, "math":"science"].sum())
    """
    math       402
    english    360
    history    350
    science    370
    """

    # 行ごと(math ~ science)の平均値
    print(df.loc[:, "math":"science"].mean(axis=1))
    """
    yamada      73.00
    kawaguti    78.75
    umino       68.25
    shimada     79.25
    morita      71.25
    """

    # 一括集計(math ~ science)
    print(df.loc[:, "math":"science"].describe())
    """
                math    english    history    science
    count   5.000000   5.000000   5.000000   5.000000
    mean   80.400000  72.000000  70.000000  74.000000
    std     9.787747   6.284903  15.811388   9.617692
    min    65.000000  65.000000  45.000000  60.000000
    25%    77.000000  68.000000  65.000000  70.000000
    50%    85.000000  70.000000  75.000000  75.000000
    75%    85.000000  77.000000  80.000000  80.000000
    max    90.000000  80.000000  85.000000  85.000000
    """

    # グループ集計(性別ごとの平均値)
    print(df.loc[:, "math":"sex"].groupby("sex").mean())
    """
         math    english  history    science
    sex                                     
    0    84.0  70.666667     65.0  78.333333
    1    75.0  74.000000     77.5  67.500000
    """

    # ピボットテーブル集計
    # index: 集計軸の列名
    # columns: 集計軸の列名
    # values: 集計対象の列
    # aggfunc: 関数名
    # margins: ブール値
    print(pd.pivot_table(df, 
        index="sex", columns="grade", values="math",
        aggfunc=max, margins=True))
    """
    性別と学年別における、数学の最高得点
    grade   1   2  All
    sex               
    0      90  85   90
    1      65  85   85
    All    90  85   90
    """

    # 行方向の結合
    # 2つのデータフレームは、列名が同じ
    df_other = pd.DataFrame(
        {"math": 50, "english": 50, "history": 50, "science": None,
        "sex": 0, "grade": 1}, index=["tanida"])
    df = pd.concat([df, df_other], axis=0)
    print(df)
    """
              math  english  history  science  sex  grade
    yamada      77       70       65       80    0      1
    kawaguti    85       80       75       75    1      2
    umino       65       68       80       60    1      1
    shimada     85       77       85       70    0      2
    morita      90       65       45       85    0      1
    tanida      50       50       50     None    0      1
    """

    # 列方向の結合
    # 2つのデータフレームは、行名が同じ
    df_other = pd.DataFrame(
        ["walk", "walk", "bus", "train", "walk", "bus"], 
        index=df.index, columns=["trans"])
    df = pd.concat([df, df_other], axis=1)
    print(df)
    """
              math  english  history  science  sex  grade  trans
    yamada      77       70       65       80    0      1   walk
    kawaguti    85       80       75       75    1      2   walk
    umino       65       68       80       60    1      1    bus
    shimada     85       77       85       70    0      2  train
    morita      90       65       45       85    0      1   walk
    tanida      50       50       50     None    0      1    bus
    """

    # 欠損値の確認
    print(df.isnull())
    """
               math  english  history  science    sex  grade  trans
    yamada    False    False    False    False  False  False  False
    ...
    tanida    False    False    False     True  False  False  False
    """

    # 欠損値の補完
    df = df.fillna(10)
    print(df)
    """
              math  english  history science  sex  grade  trans
    yamada      77       70       65      80    0      1   walk
    ...
    tanida      50       50       50      10    0      1    bus
    """

    # ダミー変数化
    df_dummies = pd.get_dummies(df["trans"], drop_first=True, dtype=int)
    print(df_dummies)
    """
              train  walk
    yamada        0     1
    kawaguti      0     1
    umino         0     0
    shimada       1     0
    morita        0     1
    tanida        0     0
    """

    df = pd.concat([df.loc[:, :"grade"], df_dummies], axis=1)
    print(df)
    """
              math  english  history science  sex  grade  train  walk
    yamada      77       70       65      80    0      1      0     1
    kawaguti    85       80       75      75    1      2      0     1
    umino       65       68       80      60    1      1      0     0
    shimada     85       77       85      70    0      2      1     0
    morita      90       65       45      85    0      1      0     1
    tanida      50       50       50      10    0      1      0     0
    """


if __name__ == "__main__":
    main()