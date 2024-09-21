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
# 具象パス(I/Oの伴う機能を提供)

# 現在のディレクトリ
print(Path.cwd())
# /Users/xxx/yyy/zzz

# ホームディレクトリ
print(Path.home())
# /Users/xxx

# 存在を確認
cp1 = Path("./dir1/dir2/dir3/hoge.txt")
print(cp1.exists())
# True

cp2 = Path("./dir1/dir2/dir3/uhyo.txt")
print(cp2.exists())
# False

# ファイルかどうか
print(cp1.is_file())
# True

# ディレクトリかどうか
print(cp1.is_dir())
# False

# ファイル/ディレクトリを作成する
cp3 = Path("./dir1/dir2/dir3/poyo.txt")
cp3.touch(exist_ok=True)# ファイル
#cp3.mkdir(exist_ok=True)# ディレクトリ

# ファイルに書き込み
cp3.write_text("This is poyo.txt!!")

# ファイルの内容を確認
print(cp3.read_text())

# ファイル/ディレクトリを削除
cp3.unlink(missing_ok=True)# ファイル
#cp3.rmdir()# ディレクトリ(空である必要がある)
