# coding: utf-8

"""
順列と組み合わせ
"""

#==========
# Main

import itertools

li_alpha = "ABC"
li_nums  = "12"

# 組み合わせ(デカルト積)
print(list(itertools.product(li_alpha, li_nums)))
# [('A', '1'), ('A', '2'), ('B', '1'), 
# ('B', '2'), ('C', '1'), ('C', '2')]

# 順列
print(list(itertools.permutations(li_alpha)))
# [('A', 'B', 'C'), ('A', 'C', 'B'), 
# ('B', 'A', 'C'), ('B', 'C', 'A'), 
# ('C', 'A', 'B'), ('C', 'B', 'A')]

# 順列(長さを2)
print(list(itertools.permutations(li_alpha, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), 
# ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 組み合わせ
print(list(itertools.combinations(li_alpha, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 組み合わせ(同じ値の繰り返しを含む)
print(list(itertools.combinations_with_replacement(li_alpha, 2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), 
# ('B', 'B'), ('B', 'C'), ('C', 'C')]
