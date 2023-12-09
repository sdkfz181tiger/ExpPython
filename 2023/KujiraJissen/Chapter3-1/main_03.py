# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-1: 
	リストの操作
"""

print("Hello, Python!!")

# リスト
actions = ["Hop", "Step", "Jump", "Punch", "Kick"]

# スライス
print(actions[0:3])# Hop, Step, Jump
print(actions[2:]) # Jump, Punch, Kick
print(actions[:3]) # Hop, Step, Jump

# 追加
actions.append("Search")
actions.append("Destroy")
actions.append("Unbush")
actions.append("Evade")
print(actions)

# 削除(特定の要素)
actions.remove("Punch")
actions.remove("Kick")
print(actions)

# 削除(スライス)
del actions[0:3]
print(actions)

# インデックスを取得
print(actions.index("Search"))
print(actions.index("Destroy"))
