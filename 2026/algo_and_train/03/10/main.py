# coding: utf-8

"""
[ アルトレ第二版 ]
3.10: 二次元配列からデータを探索する
※プログラムの場合、配列の要素は0から始まる
"""

mdata = [
    [ 3, 5, 8,11,15],
    [17,20,25,31,33],
    [40,43,51,62,71]
]

i_max = 3
j_max = 5

def array_search(n):
    print("array_search:", n)
    i = i_max - 1
    j = 0
    while 0 <= i and j < j_max:
        if mdata[i][j] == n:
            return "OK"
        elif n < mdata[i][j]:
            i = i - 1
        else:
            j = j + 1
    return "NG"

def main():
    """ メイン処理 """

    print("Test01:", array_search(11)) # OK
    print("Test02:", array_search(16)) # NG
    print("Test02:", array_search(15)) # OK

if __name__ == "__main__":
    main()