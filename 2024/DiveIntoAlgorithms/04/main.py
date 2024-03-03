# coding: utf-8

"""
久留島アルゴリズムによる魔法陣
"""

#==========
# Main

import math, random

WHERE = {"up_right":[-1, 1], "down_left":[1, -1], "up_left":[-1, -1], "down_right":[1, 1]}

def main():
	print("main!!")

	# Luo Shuの魔法陣
	#luoshu = [[4,9,2],[3,5,7],[8,1,6]]
	#result = check_square(luoshu)
	#print("result:{0}".format(result))

	# nxnの魔法陣を作る(奇数にする事)
	n = 11
	square = create_square(n)

	# 久留島アルゴリズムは斜めに移動するので開始マスをずらして2回実行する
	r = math.floor(n / 2) - 1
	c = math.floor(n / 2)
	square = fill_square(square, r, c, math.floor((n**2)/2)-4)# 1回目
	#print_square(square)

	r = math.floor(n / 2)
	c = math.floor(n / 2)
	square = fill_square(square, r, c, math.floor((n**2)/2))# 2回目
	print_square(square)

	result = check_square(square)
	print("魔法陣判定: {0}".format(result))

# nxnの行列を作る
def create_square(n):
	square = [[0 for c in range(n)] for r in range(n)]
	r = math.floor(n/2)
	c = math.floor(n/2)
	square[r][c] = int((n**2 + 1)/2)
	square[r+1][c] = 1
	square[r-1][c] = n**2
	square[r][c+1] = n**2 + 1 - n
	square[r][c-1] = n
	return square

# ルールに従って魔法陣を作る
def fill_square(square, r, c, remain):
	size = len(square)
	#print("fill_square[{0}, {1}]:{2}".format(r, c, square[r][c]))
	# Finished
	if remain <= 0: return square

	# Random walk
	where_to_go = []
	if 0 < r and c < size-1:      where_to_go.append("up_right")  # Up Right
	if r < size-1 and 0 < c:      where_to_go.append("down_left") # Down Left
	if 0 < r and 0 < c:           where_to_go.append("up_left")   # Up Left
	if r < size-1 and c < size-1: where_to_go.append("down_right")# Down Right

	# Next
	next_to_go = random.choice(where_to_go)
	next_r = WHERE[next_to_go][0] + r
	next_c = WHERE[next_to_go][1] + c

	# Countdown
	if(square[next_r][next_c] == 0): 

		# Rule1: up_right
		if next_to_go == "up_right":
			square[next_r][next_c] = rule1(square[r][c], size, True)

		# Rule1: down_left
		if next_to_go == "down_left":
			square[next_r][next_c] = rule1(square[r][c], size, False)

		# Rule2: up_left
		if next_to_go == "up_left" and (r+c) != size:
			square[next_r][next_c] = rule2(square[r][c], size, True)

		# Rule2: down_right
		if next_to_go == "down_right" and (r+c) != (size-2):
			square[next_r][next_c] = rule2(square[r][c], size, False)

		# Rule3: up_left
		if next_to_go == "up_left" and (r+c) == size:
			square[next_r][next_c] = rule3(square[r][c], size, True)

		# Rule3: down_right
		if next_to_go == "down_right" and (r+c) == (size-2):
			square[next_r][next_c] = rule3(square[r][c], size, False)

		return fill_square(square, next_r, next_c, remain-1)# 1マス埋めて再起処理

	return fill_square(square, next_r, next_c, remain)# 既に埋まっているので次へ

# ルール1(Trueで右上,Falseで左下)
def rule1(x, n, upright):
	return (x + ((-1)**upright) * n)%n**2

# ルール2(Trueで左上,Falseで右下)
def rule2(x, n, upleft):
	return (x + ((-1)**upleft))%n**2

# ルール3(Trueで左上,Falseで右下) 逆対角線を越える場合に適用
def rule3(x, n, upleft):
	return (x + ((-1)**upleft * (-n+1)))%n**2

# 魔法陣かどうかを判定
def check_square(square):
	size     = len(square)
	rowsums  = [sum(row) for row in square]
	colsums  = [sum(row[c] for row in square) for c in range(size)]
	maindiag = [sum(square[i][i] for i in range(size))]
	antidiag = [sum(square[size-i-1][size-i-1] for i in range(size))]
	sums     = rowsums + colsums + maindiag + antidiag
	return len(list(set(sums))) == 1# 全て同じ数字であれば魔法陣である

# 魔法陣を出力する
def print_square(square):
	size = len(square)
	labels = ["["+str(i)+"]" for i in range(size)]
	line = "{:>6}" * (len(labels) + 1)
	print(line.format("", *labels))
	for label, row in zip(labels, square):
		print(line.format(label, *row))

if __name__ == "__main__":
	main()
