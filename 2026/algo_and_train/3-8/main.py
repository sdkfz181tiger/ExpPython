# coding: utf-8

"""
[ アルトレ第二版 ]
3.8: k番目のデータまでを並べ替える
※プログラムの場合、配列の要素は0から始まる
"""

# data[0] ~ data[3]までは昇順に並んでいる
data = [2, 5, 7, 9, 4, 6, 3, 1, 8]

def sort(k):
    tmp = data[k]
    i = k - 1
    while data[i] > tmp:
        data[i + 1] = data[i]
        i = i - 1
    data[i + 1] = tmp

def main():
    """ メイン処理 """
    print("Before:", data)
    sort(4) # data[0] ~ data[4]まで並べ替える
    print("After:", data)

if __name__ == "__main__":
    main()