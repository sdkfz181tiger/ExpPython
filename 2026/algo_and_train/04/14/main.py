# coding: utf-8

"""
[ アルトレ第二版 ]
4.14: リストを自己再編成探索する
※プログラムの場合、配列の要素は0から始まる
"""

first = None # リストの先頭要素の参照を格納する

class Node:

    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

def organizing_search(key):
    global first
    
    temp = None
    current = first
    while current != None:
        if current.key == key:
            # Keyを発見
            if current != first:
                # 先頭でなければ、繋ぎ直し
                temp.next = current.next
                current.next = first
                first = current
            return current.value
        else:
            # Keyが見つからない時は次のNodeへ...
            temp = current
            current = current.next
    return -1

def trace():
    current = first
    while current != None:
        print("trace:", current.key)
        current = current.next

def main():
    """ メイン処理 """
    global first

    nodeA = Node("A", 4)
    nodeB = Node("B", 10)
    nodeC = Node("C", 17)
    nodeD = Node("D", 9)
    nodeE = Node("E", 5)

    first = nodeA
    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD
    nodeD.next = nodeE

    print("Test01:", organizing_search("C"))
    trace()

if __name__ == "__main__":
    main()