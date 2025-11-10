# coding: utf-8

"""
Python3認定基礎試験サンプルコード
"""

print('spam eggs')# spam eggs
print("spam eggs")# spam eggs

print('doesn\'t')# doesn't (\使う場合)
print("doesn't")# doesn't (\使わない場合)
print('"YES", they said.')# "YES", they said.
print("\"YES\", they said.")# "YES", they said.
print('"Isn\'t", they said.')# "Isn't", they said.

print("""\
きさま!
見ているなっ!\
""")

print("無駄" * 10 + "ァ!!")

print("花京院くん、"
"恐れることはないんだよ。"
"友だちになろう。")

message = "ドアぐらい開けて出ていけ・・・・・"
print(message)# ドアぐらい開けて出ていけ・・・・・

message = "この世界の空間から姿をまったく消すスタンドよ"
print(message)# この世界の空間から姿をまったく消すスタンドよ
print(message[2])# 世
print(message[3])# 界

#  +---+---+---+---+---+
#  | W | o | r | l | d |
#  +---+---+---+---+---+
#  0   1   2   3   4
# -5  -4  -3  -2  -1

message = "この世界の空間から姿をまったく消すスタンドよ"
#message[3] = "間" # ここでエラー

# 変数を使った連結
emo1 = "動揺"
emo2 = "恐怖"
print("「" + emo1 + "する」それはつまり「" + emo2 + "している」ということでは無いのかね。")

# 文字列のスライス
message = "そうかそうかポルナレフ、階段を降りたな。このDIOの仲間になりたいという訳だな。"
print(message[6])# ポ
print(message[6:11])# ポルナレフ
print(message[22])# D
print(message[22:25])# DIO
print(message[:11])# そうかそうかポルナレフ
print(message[26:])# 仲間になりたいという訳だな。
print(message[-4:])# 訳だな。

message = "「長所」と「短所」は表裏一体・・・ままならぬものよ・・・"
print("文字数は" + str(len(message)) + "です")# 文字数は28です

