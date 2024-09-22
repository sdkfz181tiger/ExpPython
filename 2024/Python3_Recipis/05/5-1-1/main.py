# coding: utf-8

"""
型ヒント
"""

#==========
# Main

from random import random
from dataclasses import dataclass

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
foods: list[str] = ["カレーライス", "ミートスパゲティ", "ハンバーグ"]
languages: set[str] = {"Python", "JAVA", "Cpp"}
developers: dict[str, str] = {"Python": "Guido", "JAVA": "James", "Cpp": "Bjarne"}

# タプル
snacks_ok: tuple[str, str, str] = ("カール", "ドンタコス", "のり塩")# OK
snasks_ok: tuple[str, ...] = ("カール", "ドンタコス", "のり塩")# OK
snacks_ng: tuple[str] = ("カール", "ドンタコス", "のり塩")# NG

# データクラス
@dataclass
class Member:
	name: str
	hp: int
	mp: int
	gold: int

# Member型のリスト
members: list[Member] = [
	Member("yusha", 100, 30, 40),
	Member("senshi", 200, 0, 30),
	Member("soryo", 80, 70, 80),
	Member("maho", 50, 100, 120)
]

# ランダムでメンバーを選出
def get_member(arr: Member) -> Member:
	rdm: int = int(len(arr) * random())
	return arr[rdm]

member: Member = get_member(members)
print(f"name: {member.name}, hp: {member.hp}, mp: {member.mp}, gold: {member.gold}")
# name: senshi, hp: 200, mp: 0, gold: 30
