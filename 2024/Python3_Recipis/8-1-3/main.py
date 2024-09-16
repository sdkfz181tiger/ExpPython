# coding: utf-8

"""
日付と時刻
"""

#==========
# Main

from datetime import datetime

# datetimeオブジェクト
my_dt = datetime.now()
print(my_dt)
# 2024-08-15 15:37:54.024181

# dateオブジェクト
my_date = my_dt.date()
print(my_date)
# 2024-08-15

# timeオブジェクト
my_time = my_dt.time()
print(my_time)
# 15:39:04.389520

# IOSフォーマット
print(my_dt.isoformat())
# 2024-08-15T15:40:39.196797

print(datetime.fromisoformat("2024-08-15T15:40:39.196797"))
# 2024-08-15 15:40:39.196797

