# coding: utf-8

"""
[ アルトレ第二版 ]
3.15: 再帰関数の戻り値を求める
※プログラムの場合、配列の要素は0から始まる
"""

def F(n):
    if n <= 1:
        return 1
    else:
        return n + F(n - 1)

def main():
    """ メイン処理 """

    print("Test01:", F(3)) # 6
    print("Test02:", F(4)) # 10
    print("Test03:", F(5)) # 15

if __name__ == "__main__":
    main()