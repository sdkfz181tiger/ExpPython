# coding: utf-8

"""
argparseモジュール
"""

#==========
# Main

from argparse import ArgumentParser

# パーサー
parser = ArgumentParser(description="Example command")

# 文字列を受け取る-sオプションを定義
parser.add_argument("-s", "--string", 
	                type=str, 
	                help="string to display", 
	                required=True)

# 数値を受け取る-nオプションを定義
parser.add_argument("-n", "--num", 
	                type=int, 
	                help="number of tymes repeatedly display string",
	                default=2)

# 引数をパースし、得られた値を変数に格納
args = parser.parse_args()
print(args.string * args.num)

# コマンドで実行

# Run
#    $ python3 main.py -s hello -n 5
# Result
#    hellohellohellohellohello

# helpコマンド

# Run
#    $ python3 -h
# Result
#    usage: main.py [-h] -s STRING [-n NUM]
#    
#    Example command
#    
#    options:
#      -h, --help            show this help message and exit
#      -s STRING, --string STRING
#                            string to display
#      -n NUM, --num NUM     number of tymes repeatedly display string

