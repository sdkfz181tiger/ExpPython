# coding: utf-8

"""
1, Install
	$ python3 -m pip install imgsim
	$ python3 -m pip install torchvision
"""

import cv2, imgsim
import torchvision.models as models

def main():
	print("main")	

	vtr = imgsim.Vectorizer()

	img_a = cv2.imread("./target.jpg")
	vec_a = vtr.vectorize(img_a)

	for i in range(1, 100):
		path = "./ip/2016h28h_ip_qs/{:02}.jpg".format(i)
		img_b = cv2.imread(path)
		vec_b = vtr.vectorize(img_b)
		dist = imgsim.distance(vec_a, vec_b)
		if 8 < dist: continue
		print(path, "distance:", dist)

# Appを起動
if __name__ == "__main__":
	main()