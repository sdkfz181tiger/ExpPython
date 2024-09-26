# coding: utf-8

"""
日付と時刻
"""

#==========
# Main

from datetime import datetime, timedelta

# timedeltaモジュール

# 現在
dt_now = datetime.now()
print(dt_now)
# 2024-09-15 15:50:55.201163

# 1週間後
delta = timedelta(days=7)
dt_1week = dt_now + delta
print(dt_1week)
# 2024-09-22 15:54:50.995689

# 2週間後
delta = timedelta(days=7)
dt_2week = dt_now + delta * 2
print(dt_2week)
# 2024-09-29 15:55:58.139488

# 終戦
dt_war = datetime(1945, 8, 15)
print(dt_war)
# 1945-08-15 00:00:00

# 終戦から現在までの経過日数
dt_delta = dt_now - dt_war
print(dt_delta)
# 28886 days, 15:50:55.201163