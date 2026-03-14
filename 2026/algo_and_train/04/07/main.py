# coding: utf-8

"""
[ アルトレ第二版 ]
4.7: 文字列を圧縮する
※プログラムの場合、配列の要素は0から始まる
チャレンジ: Pythonには、do-while構文が存在しない為、while文で実装する事
"""

HEX = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9", 
    "A", "B", "C", "D", "E", "F"
]

def dec_to_hex(c):
    return HEX[c]

def compression(s):

    p = []

    i = 0
    c = 1

    while s[i] != "#":
        i = i + 1
        # 1文字前と比較...
        if s[i-1] == s[i]:
            c = c + 1
        else:
            if 2 < c:
                # 3文字以上の時...
                p.append("*")
                p.append(dec_to_hex(c))
                p.append(s[i-1])
            else:
                # 3文字未満の時...
                while 0 < c:
                    p.append(s[i-c])
                    c = c - 1
                c = 1
    p.append("#")
    return p

def main():
    """ メイン処理 """

    print("Test01:", compression(["I", "#"]))
    print("Test02:", compression(["I", "E", "#"]))
    print("Test03:", compression(["I", "E", "E", "#"]))
    print("Test04:", compression(["I", "E", "E", "E", "#"]))
    print("Test05:", compression(["I", "E", "E", "E", "E", "#"]))
    print("Test06:", compression(["I", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "#"]))

if __name__ == "__main__":
    main()