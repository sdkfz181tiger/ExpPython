# coding: utf-8

"""
[ アルトレ第二版 ]
2.4: 二分探索法の問題
※プログラムの場合、配列の要素は0から始まる
"""

def binary_search(T, data):

    low = 0              # 探索範囲の左端の要素番号
    high = len(data) - 1 # 探索範囲の右端の要素番号

    # TODO: この続きのコードを作る事


def main():
    """ メイン処理 """

    # Test
    result = binary_search([3, 5, 6, 9, 11, 14, 18], 14)
    print("result:", result)

    

if __name__ == "__main__":
    main()