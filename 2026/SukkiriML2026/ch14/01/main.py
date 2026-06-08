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
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

COL_X  = ["rm", "ptratio", "lstat"]
COL_Y  = ["price"]
MY_CSV = "my_boston.csv"

def main():
    """ Main """
    print("main!!")

    # 主成分分析
    # 新規の列の個数を少なくして簡潔にデータを表す
    # 一般的に、元のデータ情報量の70~80%程度を反映する様に列の個数を選ぶ

    df = pd.read_csv(MY_CSV)
    print(df.head(3))

    # 欠損値を穴埋め
    df = df.fillna(df.mean(numeric_only=True))

    # ダミー変数化
    dummy = pd.get_dummies(
        df["crime"], drop_first=True, dtype=int)
    df = df.join(dummy)
    df = df.drop(["crime"], axis=1)
    print(df.head(3))

    # データの標準化(主成分分析では必須)
    df = df.astype(float) # float型に変換(fit_transformで警告が出る為)
    sc = StandardScaler()
    sc_df = sc.fit_transform(df)

    # モデルの作成と学習
    # n_components: 固有ベクトル数(既存列をいくつかの"新たな列"にまとめるか)
    # whiten: 白色化(各列の関係は無相関になり、各列の平均値が0で標準偏差が1に)
    model = PCA(n_components=2, whiten=True)
    model.fit(sc_df) # モデルで学習

    print("第一主成分の固有ベクトル")
    print(model.components_[0])
    """
    [-0.2258543   0.35923465  0.04220985  0.3499321  -0.19485285  0.29792086
     -0.29980115  0.30726517  0.32822012  0.16246983 -0.18251937  0.27543839
    -0.2018449   0.03831172 -0.31492126]
    """

    print("第二主成分の固有ベクトル")
    print(model.components_[1])
    """
    [-0.1533893   0.02835867  0.19795373  0.13817925  0.4047141   0.20058802
    -0.29340246 -0.1027543  -0.11546952 -0.34046929  0.05661836 -0.17845386
    0.44390529  0.42253976 -0.27716437]
    """

    # 主成分得点
    # 既存のsc_dfを新しい二つの軸に当てはめる
    new = model.transform(sc_df)
    new_df = pd.DataFrame(new)
    print(new_df.head(3))

    """
    0列が一番最適な列

              0         1
    0  1.490417 -0.680415
    1  0.703223 -0.252517
    2 -1.403756 -0.613175
    """

    # 主成分付加量
    # 既存の列と、新しい列との相関係数
    new_df.columns = ["pc1", "pc2"]
    df = pd.DataFrame(sc_df, columns=df.columns)
    df = pd.concat([df, new_df], axis=1)

    # 主成分付加量の計算
    df_corr = df.corr() # 計算
    df_corr = df_corr.loc[:"very_low", "pc1":]

    print("pc1との相関を確認")
    print(df_corr["pc1"].sort_values(ascending=True)) # 大きい順に並べ替え
    print("pc2との相関を確認")
    print(df_corr["pc2"].sort_values(ascending=True)) # 大きい順に並べ替え

    # 相関係数から、pc1を"田舎度"、pc2を"住環境の良さ"とする判断を行う
    new_df.columns = ["countryside", "exclusive residential"] # 列名の変更
    new_df.plot(kind="scatter", x="countryside", y="exclusive residential")
    plt.show()


if __name__ == "__main__":
    main()