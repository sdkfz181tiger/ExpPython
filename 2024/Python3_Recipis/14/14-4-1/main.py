# coding: utf-8

"""
base64モジュール
"""

#==========
# Main

import base64

#==========
# 文字列をbase64に変換
text = "Pythonは簡単に習得でき、それでいて強力な言語の一つです!!"

# Encode
encoded = base64.b64encode(text.encode())
print(encoded)

# Decode
decoded = base64.b64decode(encoded)
print(decoded.decode())

# Encode(+と/の代わりに@と#で置き換える)
encoded = base64.b64encode(text.encode(), altchars=b"@#")
print(encoded)

# Decode(+と/の代わりに@と#で置き換える)
decoded = base64.b64decode(encoded, altchars=b"@#")
print(decoded.decode())

#==========
# 画像データをbase64に変換
with open("./i_apple.png", mode="rb") as f:
    encoded = base64.b64encode(f.read())
    print(encoded)