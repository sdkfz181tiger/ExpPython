# coding: utf-8

"""
[ アルトレ第二版 ]
4.18: モンテカルロ法を用いて円周率の近似値を求める
※プログラムの場合、配列の要素は0から始まる
"""

import random

def circle_ratio():
    total_count = 10000
    in_cnt = 0
    for i in range(total_count):
        x = random.random()
        y = random.random()
        if (x*x + y*y) <= 1:
            in_cnt = in_cnt + 1
    print(4 * in_cnt / total_count)

def main():
    """ メイン処理 """
    
    circle_ratio()

if __name__ == "__main__":
    main()