# coding: utf-8

"""
IANAタイムゾーン
"""

#==========
# Main

from datetime import datetime
from zoneinfo import ZoneInfo

# IANAタイムゾーンデータベース:
# InternetAssgned Numbers Authorityが管理している、
# 世界各地のタイムゾーン情報を収めたデータベース

# 東京のZoneInfo
ASIA_TOKYO = ZoneInfo("Asia/Tokyo")
print(ASIA_TOKYO)
# Asia/Tokyo

# ロサンゼルスのZoneInfo
AMERICA_LOS = ZoneInfo("America/Los_Angeles")
print(AMERICA_LOS)
# America/Los_Angeles

# 指定日時のdatetimeオブジェクト
dt = datetime(2024, 10, 10, tzinfo=ASIA_TOKYO)
print(dt)
# 2024-10-10 00:00:00+09:0

# 東京からロサンゼルスに変更
dt = dt.astimezone(AMERICA_LOS)
print(dt)
# 2024-10-09 08:00:00-07:00