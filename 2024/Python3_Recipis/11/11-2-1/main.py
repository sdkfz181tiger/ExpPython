# coding: utf-8

"""
tempfileモジュール
"""

#==========
# Main

import tempfile
from pathlib import Path

#==========
# 一時的なファイルを作る(ファイルシステム上に存在するとは限らない)
tmp_file = tempfile.TemporaryFile()
print(tmp_file)
# <_io.BufferedRandom name=3>

# ファイルを閉じる
tmp_file.close()

#==========
# 一時的なファイル(ファイルシステム上に存在する)
tmp_named = tempfile.NamedTemporaryFile()
print(tmp_named)
# <tempfile._TemporaryFileWrapper object at 0x10e243620>

# パス
p = Path(tmp_named.name)
print(p.exists()) # ファイルが存在している
# True

# ファイルを閉じる
tmp_named.close()
print(p.exists()) # ファイルが削除されている
# False

#==========
# 一時的なディレクトリを作る

tmp_dir = tempfile.TemporaryDirectory()
print(tmp_dir)
# <TemporaryDirectory '/var/folders/xxx/T/tmppa5lpxr7'>

# パス
d = Path(tmp_dir.name)
print(d.exists()) # ディレクトリが存在している
# True

# ファイルを作る
f1 = d / "hoge.txt"
f1.touch()
print(f1.exists())
# True

f2 = d / "fuga.txt"
f2.touch()
print(f2.exists())
# True

f3 = d / "piyo.txt"
f3.touch()
print(f3.exists())
# True

# 一時ディレクトリを削除
tmp_dir.cleanup()

print(f1.exists())
print(f2.exists())
print(f3.exists())
# False
# False
# False