# coding: utf-8

"""
[ アルトレ第二版 ]
4.16: シフト演算と加算の繰返しで2進数の乗算を行う
※プログラムの場合、配列の要素は0から始まる
"""

def bim_multiply(m, n):
    x = m
    y = n
    z = 0b0

    # Pythonには、do~while文が無いので、for文で作ると...
    for i in range(4):
        if y & 0b1 == 0b1:
            z = z + x
        x = x << 1
        y = y >> 1

    return z

def main():
    """ メイン処理 """

    # 15 * 2 = 30
    print("Test01:", int(bim_multiply(0b00001111, 0b00000010)))

    # 15 * 3 = 45
    print("Test02:", int(bim_multiply(0b00001111, 0b00000011)))

    # 15 * 4 = 60
    print("Test03:", int(bim_multiply(0b00001111, 0b00000100)))

if __name__ == "__main__":
    main()