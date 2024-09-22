# coding: utf-8

"""
型ヒント
"""

#==========
# Main

from random import random
from typing import Union, Optional, Literal, Any

# Union: 複数の型を指定
def get_test_union(param: Union[int, str]) -> int:
    if isinstance(param, int): return param
    if isinstance(param, str): return int(param)
    return -1

print(get_test_union(777))# 数値を返す
print(get_test_union("777"))# 文字列を数値に変換して返す

# Optional: 指定した型とNoneの値を許可
def get_test_optional(param: Optional[int]):
    pass

get_test_optional(666)# OK
get_test_optional(None)# OK

# Literal: 特定の値のみ許可
FILE_TYPE = Literal["csv", "json", "xml"]

def get_test_literal(path: str, file_type=FILE_TYPE):
    pass

get_test_literal("hoge.csv", "csv")# OK
get_test_literal("fuga.json", "json")# OK
get_test_literal("piyo.html", "html")# NG

# Any: 任意の型を許可
def get_test_any(param: Any) -> Any:
    if isinstance(param, int): print(f"{param} is int!!")
    if isinstance(param, str): print(f"{param} is str!!")
    pass

# 返り値がint型か、str型が返る関数
def get_rdm_data():
    if random() < 0.5: return 1
    return "Hello"

data: Any = get_rdm_data()# 型付けされていない関数の値
get_test_any(data)
# Hello is str!!


