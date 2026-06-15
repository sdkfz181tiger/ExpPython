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
        "Yamada": [77, 70], "Kawaguti": [85, 80],
        "Umino":  [65, 68], "Shimada": [85, 77]
    }
    df = pd.DataFrame(scores, index=["math", "english"])
    print(df)
    """
             Yamada  Kawaguti  Umino  Shimada
    math         77        85     65       85
    english      70        80     68       77
    """

    # インデックス
    print(df.index)
    # Index(['math', 'english'], dtype='str')

    # カラム名
    print(df.columns)
    # Index(['Yamada', 'Kawaguti', 'Umino', 'Shimada'], dtype='str')

    # 行数、列数
    print(df.shape)
    # (2, 4)

    # 先頭x行, 末尾x行
    print(df.head(1))
    print(df.tail(1))

    # 特例列の抽出
    print(df["Kawaguti"])
    """
    math       85
    english    80
    """

    # 特定列(複数)の抽出
    print(df[["Yamada", "Shimada"]])
    """
             Yamada  Shimada
    math         77       85
    english      70       77
    """

    # 特定行を抽出
    print(df.loc["math"])
    """
    Yamada      77
    Kawaguti    85
    Umino       65
    Shimada     85
    """

    # 特定行、特定列を抽出
    print(df.loc[["math"], ["Kawaguti", "Umino"]])
    """
          Kawaguti  Umino
    math        85     65
    """

    # 特定行、特定列を抽出(全ての行、KawagutiからShimadaまでの列)
    print(df.loc[:, "Kawaguti":"Shimada"])
    """
             Kawaguti  Umino  Shimada
    math           85     65       85
    english        80     68       77
    """

    # 特定行を抽出(条件の指定)
    # Shimada列が80未満のデータ
    print(df[df["Shimada"] < 80])
    """
             Yamada  Kawaguti  Umino  Shimada
    english      70        80     68       77
    """

    # 特定行を抽出(複数条件)
    # Shimada列が80未満のデータ & Yamada列が80未満
    print(df[(df["Shimada"] < 80) & (df["Yamada"] < 80)])
    """
             Yamada  Kawaguti  Umino  Shimada
    english      70        80     68       77
    """

    # 特定行を追加
    df.loc["history"] = [65, 75, 80, 85]
    print(df)
    """
             Yamada  Kawaguti  Umino  Shimada
    math         77        85     65       85
    english      70        80     68       77
    history      65        75     80       85
    """

    # 特定列を追加(locではない...)
    df["Morita"] = [90, 65, 45]
    print(df)
    """
             Yamada  Kawaguti  Umino  Shimada  Morita
    math         77        85     65       85      90
    english      70        80     68       77      65
    history      65        75     80       85      45
    """

    # 特定行を削除
    print(df.drop(["english"], axis=0))
    """
             Yamada  Kawaguti  Umino  Shimada  Morita
    math         77        85     65       85      90
    history      65        75     80       85      45
    """

    # 特定列を削除
    print(df.drop(["Umino"], axis=1))
    """
             Yamada  Kawaguti  Shimada  Morita
    math         77        85       85      90
    english      70        80       77      65
    history      65        75       85      45
    """


if __name__ == "__main__":
    main()