# coding: utf-8

"""
[ アルトレ第二版 ]
4.15: 隣接行列で表されたグラフを探索する
※プログラムの場合、配列の要素は0から始まる
"""

matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0]
]

n = 6
visit = [0, 0, 0, 0, 0, 0]

def graph_search(node):
    visit[node] = 1
    print("node:", node)

    # jを0からn-1まで1づつ増やす
    for j in range(n):
        if matrix[node][j] == 1 and visit[j] == 0:
            graph_search(j)

def main():
    """ メイン処理 """
    
    graph_search(0) # 0, 1, 3, 4, 2, 5 (インデックスは0からなので注意!!)

if __name__ == "__main__":
    main()