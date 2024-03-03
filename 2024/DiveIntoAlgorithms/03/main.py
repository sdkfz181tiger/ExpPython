# coding: utf-8

"""
ユークリッドの互除法
"""

#==========
# Main

import math

def main():
	print("main!!")

	n1 = 140
	n2 = 56

	print("gcd_odd:{0}".format(gcd_odd(n1, n2)))
	print("gcd_diff:{0}".format(gcd_diff(n1, n2)))

# 余りを利用して計算する
def gcd_odd(a, b):
	higher = max(a, b)
	lower = min(a, b)
	remain = higher % lower
	if remain == 0: return lower
	return gcd_odd(lower, remain)

# 引き算を利用して計算する
def gcd_diff(a, b):
	higher = max(a, b)
	lower = min(a, b)
	diff = higher - lower
	if diff == 0: return lower
	return gcd_diff(lower, diff)

if __name__ == "__main__":
	main()
