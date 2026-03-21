# coding: utf-8

"""
[ アルトレ第二版 ]
4.22: プログラムの検証と改良
※プログラムの場合、配列の要素は0から始まる
"""

r_max = 9
c_max = 9

# 9行9列の九九表
x = [[99 for c in range(c_max)] for r in range(r_max)]

def sub(r):
    print("2乗する処理(重い処理)を実行!!")
    return r*r

def main():
    """ メイン処理 """

    for r in range(r_max):
        for c in range(c_max):
            if x[r][c] > sub(r):
                x[r][c] = sub(r)
            print("r:", r, "c:", c, "r*c:", x[r][c])

if __name__ == "__main__":
    main()