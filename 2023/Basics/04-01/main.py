# coding: utf-8

# 04-01: OpenCVの使い方

import cv2
import numpy as np
import matplotlib.pyplot as plt

print("cv2:", cv2.__version__)
print("numpy:", np.__version__)

# 画像読込(BGR)
img_bgr = cv2.imread("sample.png")
# print(img_bgr)# 画像データ
# plt.imshow(img_bgr)# 画像用意
# plt.show()# 画像表示

img_arr = np.array(img_bgr)
print(img_arr.shape)# 画角確認

# 画像変換(BGR->RGB)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# 画像変換(BGR->HSV)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
# グレースケール
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# cv2.imwrite("out_rgb.png", img_rgb) # 画像保存
# cv2.imwrite("out_hsv.png", img_hsv)
# cv2.imwrite("out_gray.png", img_gray)

# トリミング (//は切り捨て割り算)
# size = img_rgb.shape
# img_trim_tl = img_rgb[:size[0]//2, :size[1]//2]# 左上
# img_trim_br = img_rgb[size[0]//2:, size[1]//2:]# 右下
# cv2.imwrite("out_trim_tl.png", img_trim_tl)# 画像保存
# cv2.imwrite("out_trim_br.png", img_trim_br)

# リサイズ
# img_resized = cv2.resize(img_rgb, (img_rgb.shape[1]//2, img_rgb.shape[0]//2))
# cv2.imwrite("img_resized.png", img_resized)# 画像保存

# 回転
# arr = np.array(img_rgb.shape[:2]) / 2
# mat = cv2.getRotationMatrix2D(tuple(arr), 45, 1.0)
# img_rot = cv2.warpAffine(img_rgb, mat, img_rgb.shape[:2])
# cv2.imwrite("img_rot.png", img_rot)# 画像保存

# 閾値処理
# retval, img_thre = cv2.threshold(img_gray, 95, 128, cv2.THRESH_BINARY)
# cv2.imwrite("img_thre.png", img_thre)# 画像保存

# 輪郭抽出
retval, thre = cv2.threshold(img_gray, 33, 33, 33)
contours, hierarchy = cv2.findContours(thre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_cont = cv2.drawContours(img_rgb, contours, -1, (0, 0, 255), 3)

# 輪郭点の描画
for contour in contours:
    for point in contour:
        cv2.circle(img_cont, point[0], 3, (0, 255, 0), -1)

cv2.imwrite("img_cont.png", img_cont)# 画像保存
