# coding: utf-8

"""
osモジュール
"""

#==========
# Main

import os
import shutil

path_dir = "./dir"

# 現在の作業パス
print(os.getcwd())
# /Users/xxx/Documents/xxx...

# ディレクトリを作る
if not os.path.isdir(path_dir): 
	os.mkdir(path_dir)

# 作業ディレクトリに移動
os.chdir(path_dir)
print(os.getcwd())

# ファイルを10個作る
for i in range(10):
	file_name = f"test_{i}.txt"
	with open(file_name, "w") as file:
	  file.write(f"Hello, this is myfile({i})!!")

# ディレクトリの中を確認
print(os.listdir("."))

# ディレクトリを削除
os.chdir("../")
# shutil.rmtree(path_dir)

