# coding: utf-8

"""
文字列のチェックメソッド
"""

#==========
# Main

# 文字列のみの場合にTrue
print("abc".isalpha())

# 数値か文字列のみの場合にTrue
print("abc123".isalnum())

# 文字列が数値を表す場合にTrue
print("123".isdigit())

# 文字列が十進数を表す場合にTrue
print("123".isdecimal())

# 文字列が全て小文字の場合にTrue
print("abc".islower())

# 文字列が全て大文字の場合にTrue
print("ABC".isupper())

