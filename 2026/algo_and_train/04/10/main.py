# coding: utf-8

"""
[ アルトレ第二版 ]
4.10: スタックを再起的な手続きで操作する
※プログラムの場合、配列の要素は0から始まる
"""

stack = [
    [1, 2, 3], # スタックA
    [1, 2, 3], # スタックB
    [1, 2, 3]  # スタックC
]

def push(n, val):
    stack[n].append(val)

def pop(n):
    return stack[n].pop()

def empty(n):
    if len(stack[n])<=0: return 0
    return 1

def proc():

    print("proc")
    if empty(0) == 0:
        return
    else:
        push(2, pop(0))
        proc()
        push(1, pop(2))

def main():
    """ メイン処理 """

    print("Before:", stack)
    proc()
    print("After:", stack)

if __name__ == "__main__":
    main()