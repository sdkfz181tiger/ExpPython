# coding: utf-8

"""
[ アルトレ第二版 ]
4.13: 逆ポーランド表記法で表された式を計算する
※プログラムの場合、配列の要素は0から始まる
"""

def rpn_calc(rpn):

    tbl = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "+", "-", "*", "/"
    ]

    rpn_stack = []

    for i in range(len(rpn)):

        k = 0
        while tbl[k] != rpn[i]:
            k = k + 1

        if 0 <= k and k <= 9:
            # 数値ならPush
            rpn_stack.append(k)
        else:
            # それ以外ならPop
            y = rpn_stack.pop()
            x = rpn_stack.pop()
            # 計算をする
            if k == 10:
                rpn_stack.append(x + y)
            elif k == 11:
                rpn_stack.append(x - y)
            elif k == 12:
                rpn_stack.append(x * y)
            else:
                rpn_stack.append(x / y)

    return rpn_stack.pop()

def main():
    """ メイン処理 """

    print("Test01:", rpn_calc(["1", "2", "+"]))
    print("Test02:", rpn_calc(["1", "2", "3", "*", "+"]))
    print("Test03:", rpn_calc(["1", "2", "*", "3", "+"]))
    

if __name__ == "__main__":
    main()