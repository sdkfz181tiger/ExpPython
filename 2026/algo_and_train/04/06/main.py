# coding: utf-8

"""
[ アルトレ第二版 ]
4.6: 整列済の二つの配列を併合する
※プログラムの場合、配列の要素は0から始まる
"""

def merge(slist1, slist2):

    num1 = len(slist1)
    num2 = len(slist2)

    list = [None] * (num1 + num2)
    i = 0
    j = 0
    k = 0

    while i < num1 and j < num2:
        if slist1[i] < slist2[j]:
            list[k] = slist1[i]
            i = i + 1
        else:
            list[k] = slist2[j]
            j = j + 1
        k = k + 1

    while i < num1-1: # <- α
        list[k] = slist[i]
        i = i + 1
        k = k + 1

    while j < num2-1: # <- β
        list[k] = slist2[j]
        j = j + 1
        k = k + 1

    return list

def main():
    """ メイン処理 """

    print("Test:", merge([2,4,6,10,15], [6,11,17,25]))

if __name__ == "__main__":
    main()