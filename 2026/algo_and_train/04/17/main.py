# coding: utf-8

"""
[ アルトレ第二版 ]
4.17: base64を用いてバイナリデータをテキストに変換する
※プログラムの場合、配列の要素は0から始まる
"""

data = [0b11111100, 0b00001111, 0b11000000] # <- わかりやすく!!
#data = [0b11001111, 0b00111100, 0b11110011]

encode = [0b00000000] * 4

def main():
    """ メイン処理 """

    print("== data ==");
    for d in data:
        print("data:", bin(d))

    # 手順(1) ~ (4)
    encode[0] = data[0] >> 2
    encode[1] = ((data[0] & 0b00000011) << 4) | (data[1] >> 4)
    encode[2] = ((data[1] & 0b00001111) << 2) | ((data[2] & 0b11000000) >> 6)
    encode[3] = data[2] & 0b00111111

    print("== encode ==");
    for e in encode:
        print(bin(e))

if __name__ == "__main__":
    main()