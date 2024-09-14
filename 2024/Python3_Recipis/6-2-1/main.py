# coding: utf-8

"""
文字列フォーマット
"""

#==========
# Main

import math

menu1 = "カレーライス"
menu2 = "ウーロン茶"
msg1 = f"お待たせしました、{menu1}と{menu2}です。"
print(msg1)
# お待たせしました、カレーライスとウーロン茶です。

price_a = 500
price_b = 200
msg2 = f"お会計は{price_a + price_b}円になります。"
print(msg2)
# お会計は700円になります。

msg3 = f"変数の値は{price_a=}と、{price_b=}です。"
print(msg3)
# 変数の値はprice_a=500と、price_b=200です。

# 30文字で左寄せ,右寄せ中央寄せ(空白で埋める)
greeting = "Hello, World!!"
print(f"|{greeting:<30}|")
# |Hello, World!!                |
print(f"|{greeting:>30}|")
# |                Hello, World!!|
print(f"|{greeting:^30}|")
# |        Hello, World!!        |

# 30文字で左寄せ,右寄せ中央寄せ(_で埋める)
print(f"|{greeting:_<30}|")
# |Hello, World!!________________|
print(f"|{greeting:_>30}|")
# |________________Hello, World!!|
print(f"|{greeting:_^30}|")
# |________Hello, World!!________|

# 基数変換
num = 2024
print(f"{num:b}")# 2進数 -> 11111101000
print(f"{num:o}")# 8進数 -> 3750
print(f"{num:d}")# 10進数 -> 2024
print(f"{num:x}")# 16進数(小文字) -> 7e8
print(f"{num:X}")# 16進数(大文字) -> 7E8

# 固定小数点表示
print(f"{math.pi} -> {math.pi:f}")
# 3.141592653589793 -> 3.141593

# 小数点以下が2桁で、全体を8桁にして右寄せにする(空白は_で埋める)
print(f"{math.pi:_>8.2f}")
# ____3.14



