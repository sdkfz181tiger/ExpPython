# coding: utf-8

"""
[ アルトレ第二版 ]
2.5: 最小値を求める問題
※プログラムの場合、配列の要素は0から始まる
"""

class List:

    def __init__(self, name):
        self.name = name
        self.next = None

def check(node):

    while node != None:
        print(node.name)
        node = node.next

def main():
    """ メイン処理 """

    # 初期化
    london = List("ロンドン")
    roma = List("ローマ")
    pari = List("パリ")
    london.next = roma
    roma.next = pari

    first = london # 先頭はロンドン
    print("== 処理前 ==")
    check(first) # チェック

    # TODO: 続きのコードを実装する事

    pre = None
    follow = None

    follow = first
    while follow.next != None:
        pre = follow
        follow = follow.next

    pre.next = None

    print("== 処理後 ==")
    check(first) # チェック


if __name__ == "__main__":
    main()