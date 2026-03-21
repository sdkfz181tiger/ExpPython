# coding: utf-8

"""
[ アルトレ第二版 ]
4.21: 最小二乗法を用いて回帰式を求める
※プログラムの場合、配列の要素は0から始まる
"""

def regression_equation(x_data, y_data, n):

    sx = 0
    sy = 0
    sxx = 0
    sxy = 0

    for i in range(n):
        sx = sx + x_data[i]
        sy = sy + y_data[i]

    mx = sx / n
    my = sy / n

    for i in range(n):
        sxx = sxx + (x_data[i] - mx) * (x_data[i] - mx)
        sxy = sxy + (x_data[i] - mx) * (y_data[i] - my)

    a = sxy / sxx
    b = my - a * mx

    print("a:", a, "b:", b)

def main():
    """ メイン処理 """
    
    x_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y_data = [0, 3, 4, 3, 4, 3, 4, 5, 3, 4]
    n = 10
    regression_equation(x_data, y_data, n)

if __name__ == "__main__":
    main()