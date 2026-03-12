# coding: utf-8

"""
[ アルトレ第二版 ]
4.3: 1月1日からの経過日数を求める
※プログラムの場合、配列の要素は0から始まる
"""

mdays = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
]

# 平年なら0, うるう年なら1を返す
def is_leap_year(year):
    leapyear = 0
    if (year % 4 == 0) and ((year%100!=0) or (year%400==0)):
        leapyear = 1
    return leapyear

def elapsed_days(y, m, d):
    days = d
    for i in range(m-1):
        days = days + mdays[is_leap_year(y)][i]
    return days

def main():
    """ メイン処理 """

    print("Test01:", is_leap_year(2024)) # うるう年
    print("Test02:", is_leap_year(2026)) # うるう年ではない
    print("Test03:", is_leap_year(2300)) # うるう年ではない

    print("Test04:", elapsed_days(2024, 4, 1)) # 92
    print("Test05:", elapsed_days(2026, 4, 1)) # 91

if __name__ == "__main__":
    main()