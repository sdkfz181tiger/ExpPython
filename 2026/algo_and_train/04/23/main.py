# coding: utf-8

"""
[ アルトレ第二版 ]
4.23: プログラムのテストケース
※プログラムの場合、配列の要素は0から始まる
"""

def func(a, b, c, d):
    n = 0

    if a < 10 or b < 20:
        n = 10
    else:
        n = 20

    if 10 < n and 10 < d:
        n = n + 1
    else:
        n = n - 1

    return n

def main():
    """ メイン処理 """
    
    print("テストケース1:", func(9, 19, 10, 10))
    print("テストケース2:", func(10, 20, 11, 11))
    
if __name__ == "__main__":
    main()