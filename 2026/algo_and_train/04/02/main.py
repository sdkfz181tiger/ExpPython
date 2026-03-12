# coding: utf-8

"""
[ アルトレ第二版 ]
4.2: nxnの奇数魔法陣を作成する
※プログラムの場合、配列の要素は0から始まる
"""

square = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def magic_square(n):
    i = 0
    j = n // 2
    square[i][j] = 1

    for k in range(2, n*n+1):
        if (k % n) == 1:
            i = i + 1
        else:
            i = i - 1
            j = j + 1

        if i < 0:
            i = n - 1

        if (n-1) < j:
            j = 0

        square[i][j] = k

def main():
    """ メイン処理 """

    print("Before:", square)
    magic_square(3)
    print("After:", square)

if __name__ == "__main__":
    main()