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

    # Series(一次元リスト)
    scores = pd.Series([77, 85, 65, 85],
        index=["Yamada", "Kawaguti", "Umino", "Shimada"])
    print(scores)
    """
    Yamada      77
    Kawaguti    85
    Umino       65
    Shimada     85
    """

    # インデックス
    print(scores.index)
    # Index(['Yamada', 'Kawaguti', 'Umino', 'Shimada'], dtype='str')

    # 特定列を参照
    print(scores["Umino"])
    # 65

    # 重複排除
    print(scores.unique())
    # [77 85 65]

    # データの個数
    print(scores.value_counts())
    """
    85    2
    77    1
    65    1
    """

    # 並べ替え(ascending: 昇順)
    print(scores.sort_values(ascending=True))

    # 各要素に関数を適用
    def fixed_score(score):
        return score * 1.2

    print(scores.map(fixed_score))
    """
    Yamada       92.4
    Kawaguti    102.0
    Umino        78.0
    Shimada     102.0
    """

    # 条件による抽出
    print(scores[scores >= 80])
    """
    Kawaguti    85
    Shimada     85
    """


if __name__ == "__main__":
    main()