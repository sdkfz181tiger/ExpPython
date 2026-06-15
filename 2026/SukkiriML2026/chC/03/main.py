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
        "Yamada": [77, 70, 65], "Kawaguti": [85, 80, 75],
        "Umino":  [65, 68, 80], "Shimada": [85, 77, 85],
        "Morita": [90, 65, 45]
    }
    df = pd.DataFrame(scores, index=["math", "english", "history"])
    print(df)
    """
             Yamada  Kawaguti  Umino  Shimada  Morita
    math         77        85     65       85      90
    english      70        80     68       77      65
    history      65        75     80       85      45
    """

    



if __name__ == "__main__":
    main()