# coding: utf-8

"""
[ アルトレ第二版 ]
3.11: プログラム実行途中の配列の内容を考える
※プログラムの場合、配列の要素は0から始まる
"""

data = [5, 2, 3, 4, 1]

def main():
    """ メイン処理 """

    for i in range(0, len(data)-1):
        print("i:", i)
        for j in range(len(data)-1, i, -1):
            print("j:", j)
            if data[j] < data[j-1]:
                print("change: ", j, j-1)
                tmp = data[j]
                data[j] = data[j-1]
                data[j-1] = tmp
        print(data)

if __name__ == "__main__":
    main()