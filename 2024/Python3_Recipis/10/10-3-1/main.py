# coding: utf-8

"""
sysモジュール
"""

#==========
# Main

import sys

# コマンドライン引数を取得する
print(sys.argv)
# Run
#    $python3 main.py -a abc
# Result
# ['main.py', '-a', 'abc']

# Pythonのバージョン
print(sys.version_info)
# sys.version_info(major=3, minor=12, 
#      micro=0, releaselevel='final', serial=0)

# システム終了
sys.exit("プログラムを終了します")


