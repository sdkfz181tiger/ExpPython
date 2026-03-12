# coding: utf-8

"""
[ アルトレ第二版 ]
3.12: 数字文字列を数値に変換する
※プログラムの場合、配列の要素は0から始まる
"""

def text_to_int(text):
    val = 0
    i = 0
    while text[i] != "#":
        tmp = int(text[i])
        val = val * 10 + tmp
        i = i + 1
    return val

def main():
    """ メイン処理 """

    print("Test01:", text_to_int(["3", "8", "5", "#"]))

if __name__ == "__main__":
    main()