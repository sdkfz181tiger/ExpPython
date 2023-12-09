# coding: utf-8

"""
ハガキの郵便番号を抽出する
"""

import cv2, os, pickle
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# SVC
print("Hello SVC!!")

PATH_HAGAKI = "./hagaki1.png" # ハガキ画像
PATH_PKL = "./digits.pkl" # 学習済データ

def detect_zipcode():
	# はがき画像
	imgDef = cv2.imread(PATH_HAGAKI)
	# 画像サイズ
	h, w = imgDef.shape[:2]
	# 画像を右上のみに
	imgDef = imgDef[0:h//2, w//3:]
	# 画像を二値化
	gray = cv2.cvtColor(imgDef, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (3, 3), 0)
	imgGray = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)[1]
	# 輪郭を抽出
	cnts = cv2.findContours(imgGray, 
		cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
	# 抽出した矩形をリストに変換
	result1 = []
	for pt in cnts:
		# 矩形を抜き出す
		x, y, w, h = cv2.boundingRect(pt)
		# 大きすぎ/小さすぎは除去
		if not(50 < w < 70): continue
		result1.append([x, y, w, h])
	# 抽出した矩形をソート
	result1 = sorted(result1, key=lambda x: x[0])
	# 近すぎる矩形を除去
	result2 = []
	lastx = -100
	for x, y, w, h in result1:
		if(x - lastx) < 10: continue
		result2.append([x, y, w, h])
		lastx = x
	# 矩形を描画
	for x, y, w, h in result2:
		cv2.rectangle(imgDef, (x, y), (x+w, y+h), (0, 255, 0), 2)
	return result2, imgDef

def detect_number(cnts, img):
	# 学習済データ
	with open(PATH_PKL, "rb") as fp:
		clf = pickle.load(fp)
	# 矩形リストにある数字を認識する
	for i, pt in enumerate(cnts):
		x, y, w, h = pt
		# 矩形を小さくして取り出す
		x += 8
		y += 8
		w -= 16
		h -= 16
		imgRect = img[y:y+h, x:x+w]
		# 学習済データに合わせる
		imgRectGray = cv2.cvtColor(imgRect, cv2.COLOR_BGR2GRAY)# グレースケール
		imgRectGray = cv2.resize(imgRectGray, (8, 8))# リサイズ
		imgRectGray = 15 - imgRectGray // 16 # 白黒反転
		imgRectGray = imgRectGray.reshape(-1, 64)# 一次元に変換
		# 予測
		pred = clf.predict(imgRectGray)
		# 出力
		plt.subplot(1, 7, i+1)
		plt.imshow(imgRect)
		plt.axis("off")
		plt.title(str(pred))
	plt.show()

# Main

# 画像から数字を抜き出す
cnts, img = detect_zipcode()
# 抜き出した数字を認識する
detect_number(cnts, img)

#画面に描画(確認)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.savefig("result", dpi=200)
# plt.show()

