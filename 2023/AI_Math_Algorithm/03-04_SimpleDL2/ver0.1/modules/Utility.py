# coding: utf-8

import numpy as np
import pickle

"""
Utility関数
"""

# 座標が円の内側か外側かを判定
def is_inside(x, y, r):
	return x**2 + y**2 <= r**2

# onehot表現に変換
def to_categorical(label_data, num_classes):
	onehot = np.zeros((len(label_data), num_classes))
	for i in range(len(label_data)):
		onehot[i, label_data[i]] = 1
	return onehot

# Modelオブジェクトを保存
def save_model(file_name, model): 
	with open(file_name, "wb") as f:
		pickle.dump(model, f)

# Modelオブジェクトの読込
def load_model(file_name):
	with open(file_name, "rb") as f:
		return pickle.load(f)
