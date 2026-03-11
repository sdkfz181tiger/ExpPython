# coding: utf-8

"""
アルトレ第二版
3.3: 配列内に格納されているある数値を求める
※プログラムの場合、配列の要素は0から始まる
"""

def func(data):
    n = len(data)
    a = data[n-1] # 最後の要素"5"
    for i in range(n-2, -1, -1):
        if a < data[i]:
            a = data[i]
    return a

def main():
    """ メイン処理 """
    print("Test01:", func([3,8,5,4,16,13,7,9,6,5]))

if __name__ == "__main__":
    main()