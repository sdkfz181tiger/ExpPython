# coding: utf-8

"""
numpy基礎
"""

import numpy as np

# ベクター
vec = np.array([1, 2])
print(vec)

# マトリクス
mat_a = np.array([[3, 9], [7, 5]])
mat_b = np.array([[2, 0], [8, 5]])
print("mat_a:", mat_b)
print("mat_b:", mat_b)

# +, -
print("a + b =", mat_a + mat_b)
print("a - b =", mat_a - mat_b)

# スカラー積
print("a * 3 =", mat_a * 3)

# アダマール積
print("a * b =", mat_a * mat_b)

# 内積
print("a dot b =", np.dot(mat_a, mat_b))

# マトリクス * ベクター
print("A * x =", mat_a @ vec)

# 使用例1
#	合計金額と合計重量

# 注文数量
order = np.array([3, 5, 1, 10, 2])

# 商品表(商品の単価、重量を格納した行列)
items = np.array([
		[50, 90],
		[100, 150],
		[250, 350],
		[80, 15],
		[120, 30]
	])

# 行列演算: 列数 == 行数であれば計算可能
result = order @ items

# 商品表(マトリクス) x 注文数量(ベクター)
print("合計金額, 合計重量:", result)

# 使用例2
#	ポートフォリオの期待収益率

# 銘柄毎の利益率
p_rate = np.array([0.02, 0.03, 0.04, 0.01, 0.06])
# 銘柄毎の組入比率
p_weight = np.array([0.2, 0.15, 0.2, 0.2, 0.25])

print("機体収益率:", p_rate @ p_weight)






