# coding: utf-8

"""
[ アルトレ第二版 ]
3.13: 10進整数を8桁の2進数に変換する
※プログラムの場合、配列の要素は0から始まる
"""

def dec_to_bin(n):
    arr = [None] * 8 # binは予約語なのでarrに...
    j = n
    for k in range(7, -1, -1):
        arr[k] = j % 2 # 余り
        j = j // 2 # 商
    return arr

def main():
    """ メイン処理 """

    print("Test01:", dec_to_bin(25)) # [0,0,0,1,1,0,0,1]
    print("Test02:", dec_to_bin(26)) # [0,0,0,1,1,0,1,0]
    print("Test03:", dec_to_bin(27)) # [0,0,0,1,1,0,1,1]

if __name__ == "__main__":
    main()