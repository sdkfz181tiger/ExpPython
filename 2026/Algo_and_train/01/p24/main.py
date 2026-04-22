# coding: utf-8

"""
[ アルトレ第二版 ]
1.3: 二次元配列の要素の値
※プログラムの場合、配列の要素は0から始まる
"""

def main():
    """ メイン処理 """

    # 全ての要素が0である、3行5列の配列を作る
    rows = 3
    cols = 4
    a = [[0] * cols for i in range(rows)] 
    print(a)

    # 配列の中身を作る
    for i in range(rows):
        for j in range(cols):
            print("i:", i, "j:", j,  "値:", 2 * i + j)
            a[i][j] = 2 * i + j
    print(a)


if __name__ == "__main__":
    main()