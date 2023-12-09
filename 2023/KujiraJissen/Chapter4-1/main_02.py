# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter4-1: 
	日付を使ってみよう
"""

import datetime

print("Hello, Python!!")

# 現在の日付(datetime型)
d_now = datetime.datetime.now()
print(d_now.strftime("%Y/%m/%d %H:%M:%S"))

# 現在の日付(date型)
d_today = datetime.date.today()

# 特定の日付
d_date = datetime.date(1945, 6, 1)
print("D-Day:", d_date)

# x後の日付を取得
# monthes, yearsは、閏年の関係で実装はされていない

# 3日後
d_after1 = d_date + datetime.timedelta(days=3)
print("3 days after:", d_after1)

# 3週間後
d_after2 = d_date + datetime.timedelta(weeks=3)
print("3 weeks after:", d_after2)

# 日付の差(date型 - date型)
d_diff = d_today - d_date
print("Diff:", d_diff)
