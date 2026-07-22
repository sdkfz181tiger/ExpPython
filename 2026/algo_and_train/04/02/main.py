# coding: utf-8

"""
[ アルトレ第二版 ]
4.2: nxnの奇数魔法陣を作成する
※プログラムの場合、配列の要素は0から始まる
"""

square = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#square = [[0]*9 for i in range(9)]

def magic_square(n):
    
    i = 0
    j = n // 2
    square[i][j] = 1 # 最上位中央

    for k in range(2, n*n+1):

        # 1つ目のif
        if (k % n) == 1:
            i = i + 1
        else:
            i = i - 1
            j = j + 1

        # 2つ目のif
        if i < 0:
            i = n - 1

        # 3つ目のif
        if (n-1) < j:
            j = 0

        # i, jにkを代入
        square[i][j] = k

def main():
    """ メイン処理 """

    print("Before:", square)
    magic_square(3)
    print("After:", square)

if __name__ == "__main__":
    main()