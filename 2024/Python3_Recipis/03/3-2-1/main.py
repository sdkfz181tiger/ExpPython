# coding: utf-8

"""
with文, context manager
"""

#==========
# Main

import contextlib
import traceback

#==========
# with文

# with文
with open("hoge.txt") as f:
    print(f.read())
# Hello, python3!!

# with文を使わない場合
f = None
try:
    f = open("hoge.txt")
    print(f.read())
finally:
    if f: 
        f.close()
# Hello, python3!!

#==========
# コンテキストマネージャー

# コンテキストマネージャーを作る
class MyContextManager:

    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print("__enter__: ファイルを開きます")
        self.file_obj = open(self.file_name)
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("__exit__: ファイルを閉じます")
        self.file_obj.close()

# コンテキストマネージャーを使う
with MyContextManager("hoge.txt") as f:
    print(f.read())

# __enter__: ファイルを開きます
# Hello, python3!!
# __exit__: ファイルを閉じます

# デコレーターを使う

@contextlib.contextmanager
def my_open_context_manager(file_name):
    file_obj = open(file_name)
    try:
        print("__enter__: ファイルを開きます")
        yield file_obj
    except Exception as e:
        print(f"__exit__: {type(e)}")
        print(f"__exit__: {e}")
        print(f"__exit__: {list(traceback.TracebackException.from_exception(e).format())}")
        raise
    finally:
        print("__exit__: ファイルを閉じます")
        file_obj.close()

# コンテキストマネージャーを使う
with my_open_context_manager("hoge.txt") as f:
    print(f.read())

# __enter__: ファイルを開きます
# Hello, python3!!
# __exit__: ファイルを閉じます


