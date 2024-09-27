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

"""
正規表現の特殊文字

\d 数字
\D 数字以外
\s 空白文字
\S 空白文字以外
\w 任意の英数字
\W 英数字以外
. 任意の1文字
^ 先頭
$ 末尾
* 0文字以上の繰り返し
+ 1文字以上の繰り返し
? 0回か1回の繰り返し
{m} m回の繰り返し
{m, n} m回以上、n回以下の繰り返し
[...] 指定したいずれかの文字
[^...] 指定したいずれかの文字以外
(x|y) xかyの選択
"""