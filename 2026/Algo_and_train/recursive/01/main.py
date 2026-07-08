# coding: utf-8

"""
再帰処理ハンズオン

科目B: https://www.fe-siken.com/kakomon/sample/b7.html
"""

#==========
# Lv1: カウントダウン
def count_down(n):
    print("count_down:", n)
    if n <= 0: # 処理が終わる条件(重要!!)
        print("finish:", n)
        return
    else:
        count_down(n-1)

count_down(5) # 5, 4, 3, 2, 1, 0


#==========
# Lv2: 配列から
chars = ["糖", "ゴ", "リ", "オ", "う", "と", "が", "り", "あ"]
def reverse_msg(i):
    print(chars[i])
    if i <= 0: # 処理が終わる条件(重要!!)
        return
    else:
        reverse_msg(i-1)

reverse_msg(len(chars)-1)


#==========
# Lv3: 数列の和(カウントダウン)
def sum_nums_1(n):
    print("sum_nums_1:", n)
    if n <= 0: # 処理が終わる条件(重要!!)
        print("finish:", n)
        return 0
    else:
        return n + sum_nums_1(n-1)

print(sum_nums_1(5)) # 5+4+3+2+1+0の結果


#==========
# Lv4: 配列の和
# TODO1: 4 ~ 0 のカウントダウン処理を実装する事!!
# TODO2: numsの配列にある値の合計値を求める事!!
# HINT: nums[i]を使います...!!
# PROBREM: i <= 0だと合計値が22に...!!
nums = [3, 1, 5, 9, 7] # 配列内の値の和を求める
def sum_nums(i):
    print("sum_nums:", i)
    if i <= 0: # 処理が終わる条件(重要!!)
        print("finish:", i)
        return 0
    else:
        return nums[i] + sum_nums(i-1)

print(sum_nums(4)) # 7+9+5+1+3の結果


#==========
# Lv5: 数列の和(カウントアップ)
def sum_nums_2(n, limit):
    print("sum_nums_2:", n, limit)
    if limit < n: # 処理が終わる条件(重要!!)
        print("finish:", n, limit)
        return 0
    else:
        return n + sum_nums_2(n+1, limit)

print(sum_nums_2(0, 5)) # 0+1+2+3+4+5の結果
