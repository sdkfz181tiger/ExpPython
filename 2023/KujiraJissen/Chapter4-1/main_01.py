# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter4-1: 
	じゃんけんゲームを作ってみよう
"""

import random

print("Hello, Python!!")

# じゃんけんの手
hands = ["グー", "チョキ", "パー", "終了する"]

print("== じゃんけんゲーム ==")
while True:
	# じゃんけんの手を説明
	msg = ""
	for i, hand in enumerate(hands):
		msg += "{0}:{1}, ".format(i, hand)
	print(msg)

	# 手を決める
	com = random.randint(0, len(hands)-2)
	you = int(input("出す手を数値で入力してください"))

	# 終了判定
	if you == 3: break
	# エラー判定
	if you < 0 or len(hands) <= you:
		print("0 ~ 3の数値を入力してください")
		continue
	# じゃんけん判定
	print("=========")
	print("Com:{0}".format(hands[com]))
	print("You:{0}".format(hands[you]))

	# 結果
	result = (you-com+3) % 3
	if result == 0: print("あいこです")
	if result == 1: print("負けました...")
	if result == 2: print("勝ちました!!")
	print("=========")
