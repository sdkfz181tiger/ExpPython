# coding: utf-8

"""
[ アルトレ第二版 ]
3.2: 1からNまでの整数の総和を求める
"""

def sum(num):
    x = 0
    for i in range(1, num+1):
        x += i
    return x

def main():
    """ メイン処理 """
    print("Test01:", sum(3)) # 1+2+3 = 6
    print("Test02:", sum(5)) # 1+2+3+4+5 = 15

if __name__ == "__main__":
    main()