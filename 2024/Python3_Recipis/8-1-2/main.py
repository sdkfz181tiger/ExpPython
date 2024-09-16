# coding: utf-8

"""
日付と時刻
"""

#==========
# Main

from datetime import time

# timeオブジェクト
print(time())
# 00:00:00

print(time(hour=15, minute=30, second=45))
# 15:30:45

my_time = time(hour=15, minute=30, second=45, microsecond=900)
print(my_time)
# 15:30:45.000900

print(my_time.hour, my_time.minute, my_time.second, my_time.microsecond)
# 15 30 45 900

print(my_time.isoformat())
# 15:30:45.000900

print(my_time.strftime("%H:%M:%S"))
# 15:30:45