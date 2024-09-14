# coding: utf-8

"""
文字列の変換
"""

#==========
# Main

# 文字列を全て大文字に変換
print("abc".upper())

# 文字列を全て小文字に変換
print("ABC".lower())

# 大文字を小文字に、小文字を大文字に変換
print("abcABC".swapcase())

# 先頭を大文字に、その他を小文字に変換
print("aBcDeFg".capitalize())

# 先頭、末尾から文字を削除
print("aaa/bbb/ccc".strip("ac"))
# /bbb/ となる

# 先頭から文字を削除
print("aaa/bbb/ccc".lstrip("a/"))
# bbb/ccc となる

# 末尾から文字を削除
print("aaa/bbb/ccc".rstrip("c/"))
# aaa/bbb となる

# 文字列を置き換える(1個目まで)
print("HELLO, WORLD!!".replace("L", "l", 1))
# HElLO, WORLD となる