# coding: utf-8

"""
日付と時刻
"""

#==========
# Main

import time

# timeモジュール

# UTCの現在時刻
print(time.gmtime())
# time.struct_time(
#  tm_year=20xx, tm_mon=x, tm_mday=x, 
#  tm_hour=x, tm_min=x, tm_sec=x, 
#  tm_wday=x, tm_yday=x, tm_isdst=0)

# ローカルの現在時刻雨(日本)
print(time.localtime())
# time.struct_time(
#  tm_year=20xx, tm_mon=x, tm_mday=x, 
#  tm_hour=x, tm_min=x, tm_sec=x, 
#  tm_wday=x, tm_yday=x, tm_isdst=0)

# フォーマット文字列
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 20xx-xx-xx xx:xx:xx

# エポックからの秒数
print(time.time())
# 1627307806.632527

# Sleep
for i in range(5):
	print(time.time())
	time.sleep(0.5)
# 1627307965.210623
# 1627307965.715698
# 1627307966.2172
# 1627307966.72234
# 1627307967.225332

