# coding: utf-8

"""
DB
特徴:
	テキストを検出するモデル(精度重視50 / 速度重視18)
		DB_TD500: 数字,英語,中国語で学習したモデル
		DB_IC15: 数字,英語で学習したモデル
学習済みモデル:
	https://github.com/opencv/opencv/tree/4.5.5/samples/dnn
"""

import cv2, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Detection(Simple)
def detect_with_vertices(image):
	vertices, confidences = model.detect(image)
	return vertices

# Detection(Rotation)
def detect_with_rotations(image):
	rectangles, confidences = model.detectTextRectangles(image)
	vertices = []
	for rectangle in rectangles:
		points = cv2.boxPoints(rectangle)
		bl = tuple(map(int, points[0]))
		tl = tuple(map(int, points[1]))
		tr = tuple(map(int, points[2]))
		br = tuple(map(int, points[3]))
		vertices.append([bl, tl, tr, br])
	return vertices

# Directory
dir_current = os.path.dirname(__file__)

# Image
img_from = os.path.join(dir_current, "image.jpg")
capture = cv2.VideoCapture(img_from)
W = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
H = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
if not capture.isOpened():
	raise IOError("Can't open image...")

# Model
weights = os.path.join(dir_current, "../models/ocr/db/DB_TD500_resnet50.onnx")
# weights = os.path.join(dir_current, "../models/ocr/db/DB_TD500_resnet18.onnx")
# weights = os.path.join(dir_current, "../models/ocr/db/DB_IC15_resnet50.onnx")
# weights = os.path.join(dir_current, "../models/ocr/db/DB_IC15_resnet18.onnx")
model = cv2.dnn_TextDetectionModel_DB(weights)
if model is None:
	raise IOError("Can't read model...")

scale = 1.0 / 255.0# スケール係数
size = (736, 736)# MSRA-TD500で学習したモデル
# size = (736, 1280)# ICDAR2015で学習したモデル
mean = (122.67891434, 116.66876762, 104.00698793)# 平均減算値
swap = False# チャンネルの順番(True:RGB, False:BGR)
crop = False# クロップ
model.setInputParams(scale, size, mean, swap, crop)
model.setBinaryThreshold(0.3)# 2値化の閾値
model.setPolygonThreshold(0.5)# テキスト輪郭スコアの閾値
model.setMaxCandidates(200)# テキスト候補領域の上限値
model.setUnclipRatio(2.0)# アンクリップ率

# Image
result, image = capture.read()
img_to = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detection
vertices = detect_with_vertices(image)# Simple
# vertices = detect_with_rotations(image)# With rotation

for vertex in vertices:
	vertex = np.array(vertex)
	close = True
	color = (255, 255, 255)
	thickness = 1
	cv2.polylines(img_to, [vertex], close, color, thickness, cv2.LINE_AA)

cv2.imwrite("result.png", img_to)