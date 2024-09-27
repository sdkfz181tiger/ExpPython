# coding: utf-8

"""
shutilモジュール
"""

#==========
# Main

"""
フォルダ構成
./from
　├ hoge.txt
　├ fuga.txt
　├ piyo.txt
./to
　├ 
"""

import shutil
from pathlib import Path

# ファイルをコピー
shutil.copy("./from/hoge.txt", "./to/a.txt")
#shutil.copy("./from/hoge.txt", "./to/")# ディレクトリを指定
p = Path("./from/a.txt")
print(p.exists())
# True

# ファイルのコピー(メタデータもコピーする)
shutil.copy2("./from/fuga.txt", "./to/b.txt")
#shutil.copy2("./from/fuga.txt", "./to/")# ディレクトリを指定
p = Path("./from/b.txt")
print(p.exists())
# True

# 指定ディレクトリを再起的にコピー
ignore = shutil.ignore_patterns("*.csv", "*.json")
shutil.copytree("./from", "./other",
	            ignore=ignore, dirs_exist_ok=True)
