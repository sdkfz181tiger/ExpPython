# coding: utf-8

import cv2
import numpy as np

print("OpenCV:", cv2.__version__)

#==========
# 画像の生成(h:256, w:256のRGB画像)
img = np.zeros((256, 256, 3), np.uint8)

# 画像全てのピクセルをBlueに
img[:, :] = [255, 0, 0]
cv2.imwrite("img_b.png", img)

# 画像全てのピクセルをGreenに
img[:, :] = [0, 255, 0]
cv2.imwrite("img_g.png", img)

# 画像全てのピクセルをGreenに
img[:, :] = [0, 0, 255]
cv2.imwrite("img_r.png", img)

#==========
# ndarray型の操作

# 0行0列をWhiteに
img[0, 0] = [255, 255, 255]

# 全ての行の0列をWhiteに
img[:, 0] = [255, 255, 255]

# 全ての行の全ての列をWhiteに
img[:, :] = [255, 255, 255]