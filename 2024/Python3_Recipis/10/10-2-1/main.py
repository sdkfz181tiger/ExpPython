# coding: utf-8

"""
ioモジュール
"""

#==========
# Main

import io

#==========
# StringIO

sio = io.StringIO("This is string io!!")
print(sio.read(10))
# This is st

# 現在のオフセット
print(sio.tell())
# 10

# オフセットを末尾に
print(sio.seek(0, io.SEEK_END))
# 19

# 文字列書き込み
print(sio.write("Hello!!"))
# 4

# 全てのデータ
print(sio.getvalue())
# This is string io!!Hello!!

# ストリームを閉じる
sio.close()

#==========
# BytesIO

bio = io.BytesIO(b"This is bytes io!!")
print(bio.read(10))
# b'This is by'

# 現在のオフセット
print(bio.tell())
# 10

# オフセットを末尾に
print(bio.seek(0, io.SEEK_END))
# 18

# バイトを書き込み
print(bio.write(b"Hello!!"))
# 7

# 全てのデータ
print(bio.getvalue())
# b'This is bytes io!!Hello!!'

# ストリームを閉じる
bio.close()