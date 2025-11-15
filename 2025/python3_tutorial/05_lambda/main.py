# coding: utf-8

"""
Hello World
"""

#==========
# Main

# Lambda式

def make_incrementor(n):
	return lambda x: x+n

func = make_incrementor(5)
print(func(3))# 8
print(func(2))# 7

pairs = [(1, "hop"), (2, "step"), (3, "jump")]
pairs.sort(key = lambda pair: pair[1])

print(pairs)
# [(1, 'hop'), (3, 'jump'), (2, 'step')]