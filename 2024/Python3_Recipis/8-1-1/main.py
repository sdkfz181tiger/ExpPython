# coding: utf-8

"""
日付と時刻
"""

#==========
# Main

from datetime import date

# dateオブジェクト
my_date = date(1945, 8, 15)
print(my_date)
# 1945-08-15
print(my_date.year, my_date.month, my_date.day, my_date.weekday())
# 1945 8 15 2

# ISO
print(my_date.isoformat())
# 1945-08-15

print(date.fromisoformat("1945-08-15"))
# 1945-08-15

# Format
print(my_date.strftime("%Y/%m/%d"))
# 1945/08/15

print(my_date.strftime("%Y %b %d (%a)"))
# 1945 Aug 15 (Wed)

print(date.today())
# 2024-08-15

# フォーマット
print(f"終戦記念日:{my_date:%Y年%m月%d日}")
# 終戦記念日:1945年08月15日
