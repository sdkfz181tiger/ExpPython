# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-1: 
	タプルの操作
"""

print("Hello, Python!!")

# タプル
actions = ("Hop", "Step", "Jump", "Punch", "Kick")

# スライス
print(actions[0:3])# Hop, Step, Jump
print(actions[2:]) # Jump, Punch, Kick
print(actions[:3]) # Hop, Step, Jump

# インデックスを取得
print(actions.index("Step"))
print(actions.index("Punch"))

# タプルの場合、内容を変更することは出来ない
actions[1] = "Skip"
actions[3] = "Chop"
