# coding: utf-8

"""
[ アルトレ第二版 ]
4.12: 2分探索木からデータを探索する
※プログラムの場合、配列の要素は0から始まる
"""

# Index位置を調整しているので注意!!
btree = [
    [13, 1, 2],
    [10, 4,-1],
    [15, 3, 5],
    [14,-1,-1],
    [ 8,-1,-1],
    [16,-1,-1]
]

def lookup(val):
    t = 0
    while t != -1:
        if btree[t][0] == val:
            return True
        elif val < btree[t][0]:
            t = btree[t][1]
        else:
            t = btree[t][2]
    return False

def main():
    """ メイン処理 """
    
    print("Test01:", lookup(8));
    print("Test02:", lookup(10));
    print("Test02:", lookup(13));
    print("Test02:", lookup(14));
    print("Test03:", lookup(15));
    print("Test04:", lookup(99));

if __name__ == "__main__":
    main()