# coding: utf-8

"""
pathlibモジュール
"""

#==========
# Main

"""
フォルダ構成
./dir1/dir2/dir3/
　├ hoge.txt
　├ fuga.txt
　├ piyo.txt
"""

from pathlib import Path, PurePath

#==========
# 純粋パス(I/Oの伴わない機能を提供)
pp1 = PurePath("./dir1/dir2/dir3/hoge.txt")
print(pp1)
# dir1/dir2/dir3/hoge.txt

# 複数のパスを連結
pp2 = PurePath("dir1", "dir2", "dir3", "fuga.txt")
print(pp2)
# dir1/dir2/dir3/fuga.txt

# / で連結
dir1 = PurePath("dir1")
dir2 = PurePath("dir2")
dir3 = PurePath("dir3")
pp3 = dir1 / dir2 / dir3 / PurePath("piyo.txt")
print(pp3)
# dir1/dir2/dir3/piyo.txt

# 各要素を取得
print(pp3.parts)
# ('dir1', 'dir2', 'dir3', 'piyo.txt')

# 絶対パスか
print(pp3.is_absolute())
# False

# パターンに一致するか
print(pp3.match("*.txt"))
# True

# 上位パス
print(pp3.parent)
# dir1/dir2/dir3

# 末尾の名前
print(pp3.name)
# piyo.txt

# 末尾の拡張子
print(pp3.suffix)
# .txt

# 末尾の拡張子を除いたもの
print(pp3.stem)
# piyo

# パスのnameを引数で渡したものに変更したパスにして返す
print(pp3.with_name("uhyo.txt"))
# dir1/dir2/dir3/uhyo.txt

print(pp3.with_suffix(".json"))
# dir1/dir2/dir3/uhyo.json

print(pp3.with_stem("uhya"))
# dir1/dir2/dir3/uhya.txt


