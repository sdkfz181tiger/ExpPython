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

MY_CSV = "my_boston.csv"

def main():
    """ Main """
    print("main!!")

    # 次元削減と主成分分析

    # 次元削減とは
    # 複数ある既存の特徴量を組み合わせ、新しい特徴量としてまとめる事
    # 例: 数学と理科 => 理系, 国語と英語と社会 => 文系

    # 主成分分析とは(固有ベクトル)
    # 各特徴量の相関を考慮し、傾向が似ているかどうかを判断し簡潔にする事

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
    # n_components: 固有ベクトル数(既存列をいくつの"新たな列"にまとめるか)
    # whiten: 白色化(各列の関係は無相関になり、各列の平均値が0で標準偏差が1に)
    model = PCA(n_components=2, whiten=True)
    model.fit(sc_df) # モデルで学習

    print("第一主成分の固有ベクトル")
    print(model.components_[0])
    """
    [-0.23265443  0.36616284  0.04517974  0.35503904 -0.20084616  0.30527702
     -0.30707163  0.30948249  0.33128121  0.16496587  0.27862981 -0.20302074
      0.04112365 -0.32030142]
    """

    print("第二主成分の固有ベクトル")
    print(model.components_[1])
    """
    [-0.14681922  0.02281697  0.19632056  0.13501227  0.41326429  0.194608
     -0.28852895 -0.10302306 -0.11673939 -0.34444414 -0.18315489  0.44817178
      0.42053215 -0.27406254]
    """

    # 主成分得点
    # 既存のsc_dfを新しい二つの軸に当てはめる
    new = model.transform(sc_df) # numpy型
    new_df = pd.DataFrame(new) # DataFrame型へ
    print(new_df.head(3))
    """
    0列目が一番最適な列
    1列目は二番目に最適な列

              0         1
    0  1.517109 -0.708638
    1  0.548444 -0.185088
    2 -1.426543 -0.586736
    """

    # 主成分付加量を確認して結果を評価する
    # 標準化済みデータと、主成分得点との相関係数を求めると、主成分付加量となる
    new_df.columns = ["pc1", "pc2"]
    df = pd.DataFrame(sc_df, columns=df.columns)
    df = pd.concat([df, new_df], axis=1)

    # 主成分付加量の計算
    df_corr = df.corr() # 計算
    df_corr = df_corr.loc[:"very_low", "pc1":]
    print(df_corr)
    """
                   pc1       pc2
    zn       -0.569300 -0.216191
    indus     0.895993  0.033598
    chas      0.110554  0.289082
    ...
    """

    print("pc1との相関を確認")
    print(df_corr["pc1"].sort_values(ascending=True)) # 小さい順に並べ替え
    """
    pc1との相関を確認
    very_low   -0.783771
    dis        -0.751398
    zn         -0.569300
    ...
    """

    print("pc2との相関を確認")
    print(df_corr["pc2"].sort_values(ascending=False)) # 大きい順に並べ替え
    """
    pc2との相関を確認
    price       0.659933
    low         0.619234
    rm          0.608532
    ...
    """

    # 相関係数から、pc1を"田舎度"、pc2を"住環境の良さ"とする判断を行う
    # (絶対値が0.55以上の項目を元に考察)
    new_df.columns = ["countryside", "exclusive residential"] # 列名の変更
    new_df.plot(kind="scatter", x="countryside", y="exclusive residential")
    #plt.show()

    # 主成分分析を行うと、元データの情報を削る事になる
    # (新規の列の個数を少なくして簡潔にデータを表す)
    # 一般的に、元のデータ情報量の70~80%程度を反映する様に列の個数を選ぶ

    # 寄与率
    # 新しい列全体の分散(合計)と、新しい列の分散の比率の事
    # (新しい列は、元のデータの全情報量のxx%を反映している)

    model = PCA(whiten=True)
    tmp = model.fit_transform(sc_df)
    print(tmp.shape)
    # (100, 14)

    ratio = model.explained_variance_ratio_
    print(ratio)
    """
    第一列の寄与率, 第二列の寄与率...
    第一列の寄与率が0.41である事から、第一列だけで全体の41%を反映していると言える
    [0.42769329 0.15487544 0.10865349 0.06821818 0.0625151  0.05842945
     0.03126293 0.02516658 0.01980351 0.01694334 0.01162264 0.00984072
     0.00297382 0.00200152]
    """

    # 累積寄与率(寄与率の合計値)から、必要な列数を求める
    array = []
    for i in range(len(ratio)):
        total = sum(ratio[0: i+1])
        array.append(total)

    # 全体の80%を反映するには、新規の列が5列必要だとわかる
    # pd.Series(array).plot(kind="line")
    # plt.show()

    # モデルの作成と学習
    # 主成分分析から得られた結果(新規に5列を追加)
    model = PCA(n_components=5, whiten=True)
    model.fit(sc_df)
    new = model.transform(sc_df)

    # 新規に追加された5列を、csvファイルに保存
    col = ["pc1", "pc2", "pc3", "pc4", "pc5"]
    new_df = pd.DataFrame(new, columns=col)
    new_df.to_csv("new.csv", index=False)


if __name__ == "__main__":
    main()