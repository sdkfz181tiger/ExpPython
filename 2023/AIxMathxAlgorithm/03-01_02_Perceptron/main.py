# coding: utf-8

"""
多層パーセプトロン
	AND,OR,NAND回路をXOR回路に応用
"""

# 活性化関数(ステップ関数)
def step(x):
	return 0 if x <= 0 else 1

# 単純パーセプトロン
def perceptron(x1, x2, w1, w2, b):
	return step(x1*w1 + x2*w2 + b)

# 多層パーセプトロン(単純パーセプトロンの学習済データを利用)
def multi_perceptron(x1, x2):
	z1 = perceptron(x1, x2, -0.01, -0.02, 0.03)# NAND
	z2 = perceptron(x1, x2, 0.01, 0.01, 0.0)# OR
	return perceptron(z1, z2, 0.01, 0.02, -0.02)# AND

#==========
# 検証(単純パーセプトロンの学習済データを利用)

# 検証
y = multi_perceptron(0, 0)
print("0, 0 ->", y)
y = multi_perceptron(1, 0)
print("1, 0 ->", y)
y = multi_perceptron(0, 1)
print("0, 1 ->", y)
y = multi_perceptron(1, 1)
print("1, 1 ->", y)