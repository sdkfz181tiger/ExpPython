# coding: utf-8

"""
[ アルトレ第二版 ]
4.11: 再帰的な手続きを用いて、n桁の2進数を全て出力する
※プログラムの場合、配列の要素は0から始まる
"""

bins = [None] * 32 # 32個の未定義の値(binは予約語なのでbinsに)
n = None           # 2進数の桁数

def print_bins():
    print("   ->", bins[0:n]) # 0 ~ n未満までを出力

def binary_number(k):
    #print("print_number:", k)
    if n <= k:
        print_bins()
    else:
        bins[k] = 0
        binary_number(k + 1)
        bins[k] = 1
        binary_number(k + 1)

def test(number_of_digits):
    global n
    n = number_of_digits
    binary_number(0)

def main():
    """ メイン処理 """
    
    # Test
    test(4)

if __name__ == "__main__":
    main()