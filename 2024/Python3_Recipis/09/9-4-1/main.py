# coding: utf-8

"""
列挙型
"""

#==========
# Main

import enum

@enum.unique
class Eto(enum.Enum):
	NE = enum.auto() # 1
	USI = enum.auto() # 2
	TORA = enum.auto() # 3
	U = enum.auto() # 4
	TATU = enum.auto() # 5
	MI = enum.auto() # 6
	UMA = enum.auto() # 7
	HITUJI = enum.auto() # 8
	SARU = enum.auto() # 9
	TORI = enum.auto() # 10
	INU = enum.auto() # 11
	I = enum.auto() # 12

print(Eto.HITUJI) # Eto.HITUJI
print(Eto["HITUJI"]) # Eto.HITUJI
print(Eto(8)) # Eto.HITUJI

eto = Eto.HITUJI
print(eto.name) # HITSUJI
print(eto.value) # 8

# 列挙型の比較
print(Eto.SARU == Eto.SARU) # True
print(Eto.SARU == Eto.TORA) # False