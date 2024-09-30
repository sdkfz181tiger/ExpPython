# coding: utf-8

"""
デバッグ
"""

#==========
# Main

import sys

def test_method():
	print(f"hop")
	for i in range(10):
		print(f"step: {i}")
		breakpoint() # ブレークポイント
		print(f"jump: {i}")

def main():
	test_method()

if __name__ == "__main__":
	main()

#==========
# デバッガーが動いた時、
# 次のオプションで様々な情報を得る事が可能
#
# h(help): ヘルプコマンド
# w(where): スタックトレース
# n(next): 次の行に進む
# l(list): 指定した範囲のソースコードを表示する
# c(continue): 次のブレークポイントまで進む
# p(expression): 現時点でのexpressionの値を出力
# q(quit): デバッガーの修了
#
