# coding: utf-8

"""
[ アルトレ第二版 ]
3.6: 配列の要素の値を別の配列の要素番号に使用する
※プログラムの場合、配列の要素は0から始まる
"""

def sum_array(a, b):
    n = len(b)
    x = 0
    for i in range(0, n):
        print("b[{}]:{}".format(i, b[i]))
        x = x + a[b[i]-1]
    return x

def main():
    """ メイン処理 """
    
    print("Test:", sum_array([3,8,5,4,16,13,7,9,6,5], [3,5,8])) # 30

if __name__ == "__main__":
    main()