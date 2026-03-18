# coding: utf-8

"""
[ アルトレ第二版 ]
4.19: 近似解を2分法で求める手順を考える
※プログラムの場合、配列の要素は0から始まる
"""

def f(x):
    return x**2 - 10

def main():
    """ メイン処理 """

    # f(a) x f(b)が -(マイナス)になるaとbを用意する
    a = 1
    b = 4
    print("a:", a, "b:", b, "a x b:", f(a) * f(b))

    # 中点を求める
    m = (a + b) / 2
    print("m:", m)

    # aとbの距離
    d = abs(a - b)
    print("d:", d)

    # aとbの距離が十分小さくなるまで...
    while 0.01 < d:
        print("d:", d)

        if (f(a) * f(m)) < 0:
            # 解はmより左にあるので、bの値をmに...
            b = m
        elif (f(b) * f(m)) < 0:
            # 解はmより右にあるので、aの値をmに...
            a = m

        m = (a + b) / 2 # 中点
        d = abs(a - b) # 距離

    print("result:", m)

if __name__ == "__main__":
    main()