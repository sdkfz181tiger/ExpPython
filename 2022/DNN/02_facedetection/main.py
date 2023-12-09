# coding: utf-8

"""
OpenCV Face Detector
特徴:
	3種類位のモデルが提供されている
	float32: 通常の単精度浮動小数精度のモデル
	float16/uint8: 軽量化/高速化されたモデル
学習済みモデル:
	https://github.com/opencv/opencv/tree/4.5.5/samples/dnn
"""

import cv2, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

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
weights = os.path.join(dir_current, "../models/ofd/opencv_face_detector_fp16.caffemodel")
config = os.path.join(dir_current, "../models/ofd/opencv_face_detector_fp16.prototxt")
model = cv2.dnn_DetectionModel(weights, config)
if model is None:
	raise IOError("Can't read model...")

scale = 1.0# スケール係数
size = (W, H)# 入力サイズ
mean = (104.0, 177.0, 123.0)# 平均減算値
swap = False# チャンネルの順番(True:RGB, False:BGR)
crop = False# クロップ
model.setInputParams(scale, size, mean, swap, crop)

# Image
result, image = capture.read()
img_to = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detection
thre_confidence = 0.6# 信頼度の閾値(60%以上の信頼度で検出)
thre_nms = 0.4# NMSの閾値(識別範囲が40%重複している場合は結合)
_, _, boxes = model.detect(image, thre_confidence, thre_nms)
for box in boxes:
	cv2.rectangle(img_to, box, (255, 255, 255), 1, cv2.LINE_AA)
cv2.imwrite("result.png", img_to)