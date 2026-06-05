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
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

MY_CSV = "my_survived.csv"

def main():
    """ Main """
    print("main!!")

    # 分類の予測性能評価

    # 雨が降る/降らない2択を予測するモデルにおいて、
    # リスクとコストいずれかを重視するかによって予測モデルが変わる
    # 適合率(precision): "降ると予測"した件数の内、"実際に降った"件数の割合
    # 再現率(recall): "実際に降った"件数の内、"降ると予測"した件数の割合
    # 適合率はコスト重視、再現率はリスク重視と言える

    df = pd.read_csv(MY_CSV)
    print(df.head(3))
    print(df.tail(3))

    x = df[["pclass", "age"]]
    y = df["survived"]

    model = tree.DecisionTreeClassifier(max_depth=2, random_state=0)
    model.fit(x, y)

    # 適合率(precision)と再現率(recall)を計算
    pred = model.predict(x)
    report = classification_report(
        y_pred=pred, y_true=y)
    print(report)

    """
                      precision    recall  f1-score   support

               0       0.78      0.65      0.71       549
               1       0.56      0.70      0.62       342

        accuracy                           0.67       891
       macro avg       0.67      0.68      0.67       891
    weighted avg       0.69      0.67      0.68       891
    """


if __name__ == "__main__":
    main()