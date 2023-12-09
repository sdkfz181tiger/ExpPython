# coding: utf-8

"""
YOLOv4
特徴:
	物体検出で使われるモデル
	精度と速度はトレードオフの関係
	他にも2つのモデルが存在する
		Scaled(高精度) / Tiny(速度重視)
学習済みモデル:
	https://github.com/opencv/opencv/tree/4.5.5/samples/dnn
"""

import cv2, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Classes
def get_classes(file):
	classes = None
	with open(file, mode="r", encoding="utf-8") as f:
		classes = f.read().splitlines()
	return classes

# Colors
def get_colors(total):
	colors = []
	for i in range(total):
		colors.append(np.random.randint(0, 256, [3]).tolist())
	return colors

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
weights = os.path.join(dir_current, "../models/yolov4/yolov4/yolov4.weights")
config = os.path.join(dir_current, "../models/yolov4/yolov4/yolov4.cfg")
model = cv2.dnn_DetectionModel(weights, config)
if model is None:
	raise IOError("Can't read model...")

scale = 1.0 / 255.0# スケール係数
# size = (320, 320)# 入力サイズ(4つのモデルに対応)
# size = (416, 416)
size = (512, 512)
# size = (608, 608)
mean = (0.0, 0.0, 0.0)# 平均減算値
swap = True# チャンネルの順番(True:RGB, False:BGR)
crop = False# クロップ
model.setInputParams(scale, size, mean, swap, crop)
model.setNmsAcrossClasses(False)# (True:全体, False:クラスごと)

# Classes
file = os.path.join(dir_current, "../models/yolov4/coco.names")
classes = get_classes(file)
if classes is None:
	raise IOError("Can't read names...")

# Colors
colors = get_colors(len(classes))

# Image
result, image = capture.read()
img_to = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to 3 channels
channels = 1 if len(image.shape) == 2 else image.shape[2]
if channels == 1:
	image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
if channels == 4:
	image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

# Detection
thre_confidence = 0.6# 信頼度の閾値(60%以上の信頼度で検出)
thre_nms = 0.4# NMSの閾値(識別範囲が40%重複している場合は結合)
class_ids, confidences, boxes = model.detect(image, thre_confidence, thre_nms)

# Convert from 2d array to 1d array
class_ids = np.array(class_ids).flatten()
confidences = np.array(confidences).flatten()

for class_id, confidence, box in zip(class_ids, confidences, boxes):
	name = classes[class_id]# Name
	msg = "{0} ({1:.3f})".format(name, confidence)
	point = (box[0], box[1]-5)
	font = cv2.FONT_HERSHEY_SIMPLEX
	scale = 0.5
	color = colors[class_id]# Color
	thickness = 1
	cv2.rectangle(img_to, box, color, 1, cv2.LINE_AA)
	cv2.putText(img_to, msg, point, font, scale, color, thickness, cv2.LINE_AA)

cv2.imwrite("result.png", img_to)