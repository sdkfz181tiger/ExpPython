# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter3-1: 
	セットの操作
"""

print("Hello, Python!!")

# セット
actions1 = {"Hop", "Step", "Jump", "Punch", "Kick"}
actions2 = {"Eat", "Drink"}
actions3 = {"Hop", "Skip", "Crouch", "Kick"}
actions4 = {"Jump", "Punch"}

# OR
print(actions1 | actions2)

# AND
print(actions1 & actions3)

# 減算
print(actions1 - actions4)

# 含まれるかどうか
print("Step" in actions1)# True
print("Skip" in actions1)# False
