# coding: utf-8

"""
1, Install
    $ python3 -m pip install ultralytics
"""

import cv2
from PIL import Image
from ultralytics import YOLO

def main():
    """ Main """
    print("main")

    # Model
    model = YOLO("yolo11n.pt")

    # from PIL
    im1 = Image.open("../assets/sample_01.png")
    results = model.predict(source=im1, save=True)  # save plotted images


if __name__ == "__main__":
    main()