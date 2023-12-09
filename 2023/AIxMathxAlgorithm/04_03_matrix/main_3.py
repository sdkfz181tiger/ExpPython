# coding: utf-8

"""
cos類似度
"""

import numpy as np
import matplotlib.pyplot as plt

# 音楽の趣味を表すベクトル
A = np.array([ 2, 1,-1, 0, 1,-1, 0,-2, 1,-2])
B = np.array([-2,-1,-2,-1, 2, 2, 2,-2, 1, 1])
C = np.array([ 1, 1, 0, 0, 0, 0,-1, 2, 0, 1])
D = np.array([ 1, 2, 1, 1, 0, 0,-1, 1, 0, 2])
E = np.array([-1,-1, 0, 0,-1,-1, 0,-1, 0, 0])
F = np.array([ 2, 2, 2, 2, 1, 1, 1, 0, 1, 1])

people = [A, B, C, D, E, F]
names  = ["Aさん", "Bさん", "Cさん", "Dさん", "Eさん", "Fさん"]

# cos類似度を計算する関数
def calc_cos(v1, v2):
	norm1 = np.linalg.norm(v1)
	norm2 = np.linalg.norm(v2)
	if(norm1 != 0 and norm2 != 0):
		cos = v1 @ v2 / (norm1 * norm2)
	else:
		cos = 0
	return cos

pairs = [] # 計算結果の文字列を格納するリスト
coses = [] # cos類似度を格納するリスト

total = len(people)

# 全員のcos類似度を計算する
for i in range(total - 1):
	for j in range(i+1, total):
		cos = calc_cos(people[i], people[j])
		pair = names[i] + "と" + names[j] + "のcos類似度:" + str(round(cos, 4))
		pairs.append(pair)
		coses.append(cos)
		print(pair)

max_index = coses.index(max(coses)) # 最大値
min_index = coses.index(min(coses)) # 最小値

# 結果
print("最も類似する2人:", pairs[max_index])
print("最も類似しない2人:", pairs[min_index])