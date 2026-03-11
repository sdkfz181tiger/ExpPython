# coding: utf-8

"""
アルトレ第二版
3.7: 二つの正の整数の最大公約数を求める
※プログラムの場合、配列の要素は0から始まる
"""

def gcd(a, b):
    m = a
    n = b
    while m != n: # <- α (5回実行される)
        if n < m:
            m = m - n
        else:
            n = n - m
    return m

def main():
    """ メイン処理 """
    print("Test:", gcd(98, 42))

if __name__ == "__main__":
    main()