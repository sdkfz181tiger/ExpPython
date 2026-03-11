# coding: utf-8

"""
[ アルトレ第二版 ]
3.9: リスト要素を探索する
※プログラムの場合、配列の要素は0から始まる
"""

# Nodeクラス
class Node:
    def __init__(self, key):
        """ コンストラクタ """
        self.key = key
        self.next = None

node1 = Node("家康")
node2 = Node("秀忠")
node3 = Node("家光")
node4 = Node("慶喜")

node1.next = node2
node2.next = node3
node3.next = node4

top = node1

def search(key):
    node = top
    while node != None:
        print("node.key:", node.key)
        if node.key == key:
            return "探索成功"
        node = node.next
    return "探索失敗"

def main():
    """ メイン処理 """

    print("Test1:", search("家光")) # 探索成功
    print("Test2:", search("吉宗")) # 探索失敗

if __name__ == "__main__":
    main()