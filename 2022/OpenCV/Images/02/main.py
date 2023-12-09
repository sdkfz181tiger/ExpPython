# coding: utf-8

import cv2
import numpy as np

# 色成分を直接操作する

img_sentai = cv2.imread("./images/img_sentai.png", -1)

img_s_b = img_sentai.copy()
img_s_b[:, :, (1, 2)] = 0  # BGRの1番目(G)と2番目(R)を0に
img_s_g = img_sentai.copy()
img_s_g[:, :, (0, 2)] = 0  # BGRの0番目(B)と2番目(R)を0に
img_s_r = img_sentai.copy()
img_s_r[:, :, (0, 1)] = 0  # BGRの0番目(B)と1番目(G)を0に

cv2.imwrite("./sentai_01_b.png", img_s_b)
cv2.imwrite("./sentai_01_g.png", img_s_g)
cv2.imwrite("./sentai_01_r.png", img_s_r)