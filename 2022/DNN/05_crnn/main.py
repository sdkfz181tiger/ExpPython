# coding: utf-8

"""
CRNN
特徴:
	テキストを認識するモデル
		CRNN-CTC: 精度 > 速度
		DenseNet-CTC: 精度 < 速度
学習済みモデル:
	https://github.com/opencv/opencv/tree/4.5.5/samples/dnn
"""

import cv2, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# TextDetector
class TextDetector:

	def __init__(self):
		# Model
		weights = os.path.join(dir_current, "../models/ocr/db/DB_TD500_resnet50.onnx")
		# weights = os.path.join(dir_current, "../models/ocr/db/DB_TD500_resnet18.onnx")
		# weights = os.path.join(dir_current, "../models/ocr/db/DB_IC15_resnet50.onnx")
		# weights = os.path.join(dir_current, "../models/ocr/db/DB_IC15_resnet18.onnx")
		self._model = cv2.dnn_TextDetectionModel_DB(weights)
		if self._model is None:
			raise IOError("Can't read model...")

		scale = 1.0 / 255.0# スケール係数
		size = (736, 736)# MSRA-TD500で学習したモデル
		# size = (736, 1280)# ICDAR2015で学習したモデル
		mean = (122.67891434, 116.66876762, 104.00698793)# 平均減算値
		swap = False# チャンネルの順番(True:RGB, False:BGR)
		crop = False# クロップ
		self._model.setInputParams(scale, size, mean, swap, crop)
		self._model.setBinaryThreshold(0.3)# 2値化の閾値
		self._model.setPolygonThreshold(0.5)# テキスト輪郭スコアの閾値
		self._model.setMaxCandidates(200)# テキスト候補領域の上限値
		self._model.setUnclipRatio(2.0)# アンクリップ率

	def detect(self, image):
		img_to = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		vertices, _ = self._model.detect(image)
		for vertex in vertices:
			vertex = np.array(vertex)
			close = True
			color = (255, 255, 255)
			thickness = 1
			cv2.polylines(img_to, [vertex], close, color, thickness, cv2.LINE_AA)
		cv2.imwrite("result.png", img_to)
		return vertices

	def get_clips(self, image, vertices):
		clips = []
		size = (100, 32)
		for vertex in vertices:
			source_poins = np.array(vertex, dtype=np.float32)
			target_poins = np.array([[0, size[1]], [0, 0], [size[0], 0], [size[0], size[1]]], dtype=np.float32)
			transform_matrix = cv2.getPerspectiveTransform(source_poins, target_poins)
			clip = cv2.warpPerspective(image, transform_matrix, size)
			clips.append(clip)
		return clips

# TextRecognizer
class TextRecognizer:

	def __init__(self):
		# Model
		# weights = os.path.join(dir_current, "../models/ocr/crnn-ctc/crnn.onnx")# 英語, 数字
		weights = os.path.join(dir_current, "../models/ocr/crnn-ctc/crnn_cs.onnx")# 英語, 数字, 記号
		# weights = os.path.join(dir_current, "../models/ocr/crnn-ctc/crnn_cs_CN.onnx")# 英語, 数字, 記号, 中国語
		self._model = cv2.dnn_TextRecognitionModel(weights)
		if self._model is None:
			raise IOError("Can't read model...")

		# Vocabularies
		vocabularies = self.load_vocabularies()
		if vocabularies is None:
			raise IOError("Can't load vocabularies...")
		self._model.setVocabulary(vocabularies)

	def load_vocabularies(self):
		# Alphabet
		# file = os.path.join(dir_current, "../models/ocr/alphabet_36.txt")# 英語, 数字
		file = os.path.join(dir_current, "../models/ocr/alphabet_94.txt")# 英語, 数字, 記号
		# file = os.path.join(dir_current, "../models/ocr/alphabet_3944.txt")# 英語, 数字, 記号, 中国語
		# Vocabularies
		vocabularies = None
		with open(file, mode="r", encoding="utf-8") as f:
			vocabularies = f.read().splitlines()
		return vocabularies

	def recognize(self, clip):
		# Grayscale
		clip = cv2.cvtColor(clip, cv2.COLOR_BGR2GRAY)
		return self._model.recognize(clip)






# Directory
dir_current = os.path.dirname(__file__)

# Image
img_from = os.path.join(dir_current, "image.jpg")
capture = cv2.VideoCapture(img_from)
W = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
H = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
if not capture.isOpened():
	raise IOError("Can't open image...")

# Image
result, image = capture.read()

# Convert to 3 channels
channels = 1 if len(image.shape) == 2 else image.shape[2]
if channels == 1:
	image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
if channels == 4:
	image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

# TextDetector
text_detector = TextDetector()
vertices = text_detector.detect(image)
clips = text_detector.get_clips(image, vertices)

# TextRecognizer
text_recognizer = TextRecognizer()

texts = []
for clip in clips:
	print(clip)
	#text = text_recognizer.recognize(clip)
	#texts.append(text)