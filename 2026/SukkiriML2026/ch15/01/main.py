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
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

MY_CSV = "my_wholesales.csv"

def main():
    """ Main """
    print("main!!")

    # クラスタリング
    # 特徴量を元に、データを似ているもの同士でグループ分けする事

    df = pd.read_csv(MY_CSV)
    print(df.head(3))

    # 欠損値の確認(欠損値は無し)
    print(df.isnull().sum())

    # channelと、regionは削除(ダミー変数化すると列数が増えすぎる為)
    df = df.drop(["channel", "region"], axis=1)

    # 標準化
    sc = StandardScaler()
    sc_df = sc.fit_transform(df)
    sc_df = pd.DataFrame(sc_df, columns=df.columns)

    # k-means法
    # n_clusters: クラスタ数
    # random_state: 代表点がランダムで決まってしまう為、0で固定
    model = KMeans(n_clusters=3, random_state=0)
    model.fit(sc_df)
    print(model.labels_)
    """
    0~2までのクラス番号
    [2 2 2 2 0 2 2 ... 1 2 2]
    """

    # クラスタリング結果を追加
    sc_df["cluster"] = model.labels_
    print(sc_df.head(3))
    """
          fresh      milk ...  delicassen  cluster
    0  0.052933  0.523568 ...   -0.066339        2
    1 -0.391302  0.544458 ...    0.089151        2
    2 -0.447029  0.408538 ...    2.243293        2
    """

    # クラスタごとに各特徴量の平均値を集計
    # 結果を棒グラフで確認
    cluster_mean = sc_df.groupby("cluster").mean()
    #cluster_mean.plot(kind="bar")
    #plt.show()

    # クラスタ数2~30でSSE(クラスタ内誤差平方和)を求める
    sses = []
    for n in range(2, 31):
        model = KMeans(n_clusters=n, random_state=0)
        model.fit(sc_df)
        sse = model.inertia_ # SSEを計算
        sses.append(sse)

    print(sses)
    """
    [2184.1520787874542, 
     1650.770187770802, 
     1358.68267333124, 
     ...]
    """

    # 結果を折れ線グラフで確認
    # クラスタ数が5から減少速度が鈍り始めている事がわかる(エルボー法)
    se = pd.Series(sses)
    se.index = range(2, 31)
    se.plot(kind="line")
    #plt.show()

    # クラスタ数を5でモデルを作り、学習結果をcsvファイルに保存
    model = KMeans(n_clusters=5, random_state=0)
    model.fit(sc_df)
    sc_df["cluster"] = model.labels_
    sc_df.to_csv("new.csv", index=False)


if __name__ == "__main__":
    main()