# coding: utf-8
import datetime, json, os, shutil
from pathlib import Path

print(Path.home()) # ホームディレクトリ

# Path
path = Path("/home/xxxxxxx/Desktop/test.txt")
print(path.name)# ファイル名
print(path.stem)# ファイル名(拡張子なし)
print(path.suffix)# ファイル名(拡張子のみ)
print(path.parent)# 親ディレクトリ

# shutil
shutil.copy2("test.txt", "copied.txt")
shutil.move("copied.txt", "archives/.")
shutil.move("archives/copied.txt", "archives/copied2.txt")