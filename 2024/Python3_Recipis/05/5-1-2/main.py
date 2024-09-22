# coding: utf-8

"""
型ヒント
"""

#==========
# Main

from random import random
from dataclasses import dataclass

# データクラス
@dataclass
class Chip:
    name: str
    maker: str
    price: int

# Chip型のリスト
chips: list[Chip] = [
    Chip("のりしお", "カルビー", 120),
    Chip("カラムーチョ", "湖池屋", 130),
    Chip("わさビーフ", "山芳製菓", 110)
]

# ランダムでChipを選出
def get_chip(arr: list[Chip]) -> Chip:
    rdm: int = int(len(arr) * random())
    return arr[rdm]

chip: Chip = get_chip(chips)
print(f"{chip.name}({chip.maker}): {chip.price}yen")
# カラムーチョ(湖池屋): 130yen
