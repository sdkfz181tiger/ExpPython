# coding: utf-8

"""
[ アルトレ第二版 ]
4.9: 配列上にヒープを作成する
※プログラムの場合、配列の要素は0から始まる
"""

heap = [] # 空のヒープ(要素数0)

n = 0 # 要素数

def swap(i, j):
    print("swap:", i, j)
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp

def make_heap(num):
    global n
    print("make_heap:", num)

    heap.append(num)
    r = n          # 追加した要素番号
    p = (r-1) // 2 # 追加したノードの親の要素番号
    n = n + 1

    # Heapの再構築
    while 0 < r and heap[r] < heap[p]:
        swap(p, r) # 要素番号rと、要素番号pを交換
        r = p # 親の要素番号へ...
        p = (r-1) // 2 # 更にその親の要素番号へ...

def main():
    """ メイン処理 """

    print("Before:", heap)
    make_heap(5)
    print("Step:", heap)
    make_heap(8)
    print("Step:", heap)
    make_heap(3)
    print("After:", heap)

if __name__ == "__main__":
    main()