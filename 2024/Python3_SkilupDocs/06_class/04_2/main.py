# coding: utf-8

"""
素数を返すジェネレータ関数
    next()で呼ばれたときに値を計算する方法で、
    シーケンスを行う
"""

import math

#==========
# Main

# 素数を返すジェネレータ関数(デフォルトでは2から開始)
def gen_prime(x=2):
    while True:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0: break
        else:
            yield x
        x += 1

def main():

    # 最初の10個の素数を表示
    #i = gen_prime()# 2からの10個
    i = gen_prime(10000)# 10000からの10個
    for c in range(10):
        print(next(i), end=" ")
    print("")

if __name__ == "__main__":
    main()
