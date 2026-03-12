# coding: utf-8

"""
[ アルトレ第二版 ]
4.1: ゲームの得点を計算する
※プログラムの場合、配列の要素は0から始まる
"""

def num(mc):
    mark_ct = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    n = 0
    while mc != mark_ct[n]:
        n = n + 1
    return n + 1

def calc_score(mark):
    score = 0
    for i in range(len(mark)):
        if mark[i] == "+":
            score = score + num(mark[i + 1]) + 10
        elif mark[i] == "-":
            score = score + num(mark[i - 1]) + 10
        else:
            score = score + num(mark[i])
        print("i:", i, "score:", score)
    return score

def main():
    """ メイン処理 """
    
    print("Test01:", calc_score(["1", "+", "2", "-", "9", "5"]))

if __name__ == "__main__":
    main()