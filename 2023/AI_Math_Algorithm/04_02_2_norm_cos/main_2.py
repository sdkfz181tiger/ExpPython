# coding: utf-8

"""
ノルムのテスト
"""

import numpy as np
import matplotlib.pyplot as plt

# ベクトル
vec_a = np.array([4, 3])

# ノルム(マンハッタン距離) -> 4 + 3
print(np.linalg.norm(vec_a, 1))

# ノルム(ユークリッド距離) -> √(16 + 9)
print(np.linalg.norm(vec_a, 2))

# ノルム(ミンコフスキ距離) -> ^3√(64 + 27)
print(np.linalg.norm(vec_a, 3))

# ベクトルの正規化
vec_u = vec_a / np.linalg.norm(vec_a)

# ベクトルが単位ベクトルか確認
print(np.linalg.norm(vec_u))