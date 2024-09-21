# coding: utf-8

"""
正規表現
"""

#==========
# Main

import re

# 検索対象の文字列
target = "abcdefghijk"

# 文字列に正規表現にマッチするか
print(re.search("d.f", target))
# <re.Match object; span=(3, 6), match='def'>

# 文字列の先頭部分に正規表現にマッチするかどうか
print(re.match("d.f", target))
# None
print(re.match("a.c", target))
# <re.Match object; span=(0, 3), match='abc'>

# フラグ
print(re.search("\w", "いろはにほへとABCDEFG"))
# い

# フラグ(UnicodeではなくASCII)
print(re.search("\w", "いろはにほへとABCDEFG", flags=re.A))
# A