# coding: utf-8

"""
アルトレ第二版
3.5: 配列の要素の並びを逆順にする
※プログラムの場合、配列の要素は0から始まる
"""

def main():
    """ メイン処理 """

    array = [1, 2, 3, 4, 5]
    print("Before:", array)

    left = 0
    right = len(array) - 1
    while left < right:
        print("Change left:", left, "<-> right:", right)
        tmp = array[right]
        array[right] = array[left]
        array[left] = tmp
        left = left + 1
        right = right - 1

    print("After:", array)
    

if __name__ == "__main__":
    main()