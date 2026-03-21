# coding: utf-8

"""
[ アルトレ第二版 ]
4.20: 行列の乗算で2年後の格付推移行列を求める
※プログラムの場合、配列の要素は0から始まる
"""

# 1年後の推移行列が格納されている3x3の二次元配列
# 小数の演算時、2進数で無限小数になると誤差が発生してしまう...
matrix = [
    [7, 2, 1],
    [2, 7, 1],
    [0, 2, 8]
]

# 2年後の推移行列を格納する3x3の二次元配列
matrixN = [[0 for _ in range(3)] for _ in range(3)]

def main():
    """ メイン処理 """

    for i in range(3):
        for j in range(3):
            matrixN[i][j] = 0
            for k in range(3):
                matrixN[i][j] = matrixN[i][j] + matrix[i][k] * matrix[k][j]
            matrixN[i][j] /= 100 # 誤差対策...

    print("Test:", matrixN)

if __name__ == "__main__":
    main()