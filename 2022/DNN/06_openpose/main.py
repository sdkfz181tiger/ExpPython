# coding: utf-8

"""
OpenPose
特徴:
	人物姿勢推定をするモデル(Lightweight)
学習済みモデル:
	https://github.com/opencv/opencv/tree/4.5.5/samples/dnn
"""

import cv2, enum, math, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Joints
class joints(enum.IntEnum):
	NOSE = 0
	SPINE_SHOULDER = enum.auto()# 1
	SHOULDER_RIGHT = enum.auto()# 2
	ELBOW_RIGHT    = enum.auto()# 3
	HAND_RIGHT     = enum.auto()# 4
	SHOULDER_LEFT  = enum.auto()# 5
	ELBOW_LEFT     = enum.auto()# 6
	HAND_LEFT      = enum.auto()# 7
	HIP_RIGHT      = enum.auto()# 8
	KNEE_RIGHT     = enum.auto()# 9
	FOOT_RIGHT     = enum.auto()# 10
	HIP_LEFT       = enum.auto()# 11
	KNEE_LEFT      = enum.auto()# 12
	FOOT_LEFT      = enum.auto()# 13
	EYE_RIGHT      = enum.auto()# 14
	EYE_LEFT       = enum.auto()# 15
	EAR_RIGHT      = enum.auto()# 16
	EAR_LEFT       = enum.auto()# 17

# BoneList
bones = [
    (joints.SPINE_SHOULDER, joints.SHOULDER_RIGHT),
    (joints.SPINE_SHOULDER, joints.SHOULDER_LEFT),
    (joints.SHOULDER_RIGHT, joints.ELBOW_RIGHT),
    (joints.ELBOW_RIGHT,    joints.HAND_RIGHT),
    (joints.SHOULDER_LEFT,  joints.ELBOW_LEFT),
    (joints.ELBOW_LEFT,     joints.HAND_LEFT),
    (joints.SPINE_SHOULDER, joints.HIP_RIGHT),
    (joints.HIP_RIGHT,      joints.KNEE_RIGHT),
    (joints.KNEE_RIGHT,     joints.FOOT_RIGHT),
    (joints.SPINE_SHOULDER, joints.HIP_LEFT),
    (joints.HIP_LEFT,       joints.KNEE_LEFT),
    (joints.KNEE_LEFT,      joints.FOOT_LEFT),
    (joints.SPINE_SHOULDER, joints.NOSE),
    (joints.NOSE,           joints.EYE_RIGHT),
    (joints.EYE_RIGHT,      joints.EAR_RIGHT),
    (joints.NOSE,           joints.EYE_LEFT),
    (joints.EYE_LEFT,       joints.EAR_LEFT)
]

# Colors
def get_colors():
	colors = [(255, 0, 0), (255, 85, 0), (255, 170, 0), (255, 255, 0), 
		(170, 255, 0), (85, 255, 0), (0, 255, 0), (0, 255, 85), (0, 255, 170), 
		(0, 255, 255), (0, 170, 255), (0, 85, 255), (0, 0, 255), (85, 0, 255), 
		(170, 0, 255), (255, 0, 255), (255, 0, 170), (255, 0, 85)]
	return colors

# Draw
def draw_bone(image, p_from, p_to, color, thickness=4):
	mean_x = int((p_from[0] + p_to[0]) / 2.0)
	mean_y = int((p_from[1] + p_to[1]) / 2.0)
	center = (mean_x, mean_y)
	diff = p_from - p_to
	length = math.sqrt(diff[0] * diff[0] + diff[1] * diff[1])
	axes = (int(length / 2.0), thickness)
	angle = int(math.degrees(math.atan2(diff[1], diff[0])))
	polygon = cv2.ellipse2Poly(center, axes, angle, 0, 360, 1)
	cv2.fillConvexPoly(image, polygon, color, cv2.LINE_AA)

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
weights = os.path.join(dir_current, "../models/openpose/human-pose-estimation.onnx")
model = cv2.dnn_KeypointsModel(weights)
if model is None:
	raise IOError("Can't read model...")

scale = 1.0 / 255.0# スケール係数
size = (256, 456)
mean = (128.0, 128.0, 128.0)# 平均減算値
swap = False# チャンネルの順番(True:RGB, False:BGR)
crop = False# クロップ
model.setInputParams(scale, size, mean, swap, crop)
model.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
model.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Colors
colors = get_colors()

# Image
result, image = capture.read()
img_to = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to 3 channels
channels = 1 if len(image.shape) == 2 else image.shape[2]
if channels == 1:
	image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
if channels == 4:
	image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

# Aspect Ratio
rows, cols, _ = image.shape
size = (256, int((256 / cols) * rows))
model.setInputSize(size)

# Estimate
thre_confidence = 0.6
keypoints = model.estimate(image, thre_confidence)

# Draw keypoints
for index, keypoint in enumerate(keypoints):
	point = tuple(map(int, keypoint.tolist()))
	radius = 5
	color = colors[index]
	thickness = -1
	cv2.circle(img_to, point, radius, color, thickness, cv2.LINE_AA)

# Draw bones
for bone in bones:
	p_from = keypoints[bone[0]]
	p_to = keypoints[bone[1]]
	if (p_from == [-1, -1]).all() or (p_to == [-1, -1]).all():
		continue
	draw_bone(img_to, p_from, p_to, colors[bone[1]])

cv2.imwrite("result.png", img_to)