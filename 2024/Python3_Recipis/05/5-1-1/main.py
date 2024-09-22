# coding: utf-8

"""
型ヒント
"""

#==========
# Main

# 型ヒント
data1: int = 1
data2: float = 1.0
data3: bool = True
data4: str = "Hello"
data5: bytes = b"abc"

# 関数(戻り値がある場合)
def say_hello(name: str) -> str:
    return f"Hello, {name}!!"

print(say_hello("Michel"))
# Hello, Michel!!

# 関数(戻り値が無い場合)
def say_byebye(name: str) -> None:
    print(f"Byebye, {name}!!")

print(say_hello("Jackson"))
# Hello, Jackson!!

# リスト、セット、辞書
foods: list[str] = ["のりしお", "カラムーチョ", "わさビーフ"]
languages: set[str] = {"のりしお", "カラムーチョ", "わさビーフ"}
developers: dict[str, str] = {"のりしお": "カルビー", "カラムーチョ": "湖池屋", "わさビーフ": "山芳製菓"}

# タプル
snacks_ok: tuple[str, str, str] = ("のりしお", "カラムーチョ", "わさビーフ")# OK
snasks_ok: tuple[str, ...] = ("のりしお", "カラムーチョ", "わさビーフ")# OK
snacks_ng: tuple[str] = ("のりしお", "カラムーチョ", "わさビーフ")# NG