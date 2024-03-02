# coding: utf-8

"""
ロシア農民の掛け算
"""

#==========
# Main

import math
import pandas as pd

n1 = 89
n2 = 18

def main():
	print("main!!")

	# 半分にする配列を用意
	halving = [n1]
	while(min(halving) > 1):
		half = math.floor(min(halving)/2)
		halving.append(half)

	# 倍にする配列を用意
	doubling = [n2]
	while(len(doubling) < len(halving)):
		double = max(doubling) * 2
		doubling.append(double)

	# 2つの配列をデータフレームに格納
	half_double = pd.DataFrame(zip(halving, doubling))

	# 半分の列が奇数である行だけ抽出(行, 列)
	half_double = half_double.loc[half_double[0]%2 == 1,:]
	print(half_double)

	# 倍の列の合計を計算する(全ての行、1列目を対象)
	answer = sum(half_double.loc[:, 1])
	print("{0} x {1} = {2}".format(n1, n2, answer))

if __name__ == "__main__":
	main()
