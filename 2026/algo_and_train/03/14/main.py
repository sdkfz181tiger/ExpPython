# coding: utf-8

"""
[ アルトレ第二版 ]
3.14: ビット演算の結果を表示する
※プログラムの場合、配列の要素は0から始まる
"""

def bit_or(a, b):
    mask = 0b10000000
    c = a | b
    print("c:", bin(c))
    for i in range(0, 8):
        print("mask:", bin(mask))
        if (c & mask) == 0b00000000:
            print("0")
        else:
            print("1")
        mask = mask >> 1

def main():
    """ メイン処理 """

    print("Test01:", bit_or(0b10010000, 0b00000110))

if __name__ == "__main__":
    main()