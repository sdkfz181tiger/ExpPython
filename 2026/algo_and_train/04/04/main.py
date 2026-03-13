# coding: utf-8

"""
[ アルトレ第二版 ]
4.4: 自然数nまでの素数を求める
※プログラムの場合、配列の要素は0から始まる
"""

import math

def prime_number(n):

    prime = [0] * (n+1)
    print(prime)

    m = math.floor(math.sqrt(n))
    print("m:", m)

    for i in range(2, m):
        j = i * 2
        while j <= n:
            prime[j] = 1 # <- α
            j = j + i
    print(prime)

    for i in range(2, n-1):
        if prime[i] == 0:
            print(i)

def main():
    """ メイン処理 """

    prime_number(16) # 2,3,5,7,11,13

if __name__ == "__main__":
    main()