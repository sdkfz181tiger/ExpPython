# coding: utf-8

"""
[ アルトレ第二版 ]
3.4: 二つの配列を連結する
※プログラムの場合、配列の要素は0から始まる
"""

def con_cat(x, y):
    len_x = len(x)
    len_y = len(y)
    z = [None] * (len_x+len_y)
    print(z)
    for k in range(len_x):
        z[k] = x[k]
    print(z)
    for k in range(len_y):
        z[k+len_y] = y[k]
    print(z)
    return z

def main():
    """ メイン処理 """
    print("Test01:", con_cat(["A", "B", "C"], ["D", "E", "F"]))

if __name__ == "__main__":
    main()