# coding: utf-8

"""
一般的な文字列操作
"""

#==========
# Main


# 文字列を作る
msg1 = "おはよう"
msg2 = 'こんにちは'
print(msg1)
print(msg2)

# 複数行に分ける
msg3 = ("こんばんわ、" 
"明日は"
"晴れると"
"良いですね。")
print(msg3)

# エスケープシーケンス
msg4 = "ここで改行\nしてみます。"
print(msg4)

# raw文字列でエスケープシーケンスを無効に
msg5 = r"ここで改行\nしてみます。"
print(msg5)

