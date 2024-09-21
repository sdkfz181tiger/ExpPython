# coding: utf-8

"""
正規表現オブジェクト
"""

#==========
# Main

import re

# 検索対象の文字列
target1 = "abcdefghijk"

# 正規表現オブジェクト
regex1 = re.compile("d.f")
print(regex1.search(target1))
print(regex1.match(target1))# 先頭とマッチするか
print(regex1.fullmatch(target1))# 全体とマッチするか

regex2 = re.compile("[d-g]+")
print(regex2.search(target1))
print(regex2.match(target1))# 先頭とマッチするか
print(regex2.fullmatch(target1))# 全体とマッチするか

# 正規表現オブジェクト
regex3 = re.compile("[()-+]")

print(regex3.split("(080)1234-5678"))# 分割
# ['', '080', '1234', '5678']

print(regex3.split("080-1234-5678"))# 分割
# ['080', '1234', '5678']

print(regex3.split("+81-80-1234-5678"))# 分割
# ['', '81-80-1234-5678']

# マッチオブジェクト
result = re.match(r"(\d+)-(\d+)-(\d+)", "080-1234-5678")
print(result.group(0))# 全体
# 080-1234-5678
print(result.group(1))# サブグループ
# 080
print(result.group(2))# サブグループ
# 1234
print(result.group(3))# サブグループ
# 5678

