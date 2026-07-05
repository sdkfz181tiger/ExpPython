# coding: utf-8

"""
1, Install
    $ python3 -m pip install ultralytics
"""

import cv2, os
import utilities.utility as utility
from moviepy import VideoFileClip, AudioFileClip, AudioArrayClip
from pathlib import Path
from PIL import Image
from ultralytics import YOLO, solutions

def main():
    """ Main """
    print("main")

    # Prediction
    start_prediction("../assets/chaplin_01.mp4")


@utility.my_decorator
def start_prediction(w, h, count, cap_from, cap_to):
    print("start_prediction")

    # Model
    model = YOLO("yolo26n-pose.pt")

    # Render
    for n in range(count):
        ret, frame = cap_from.read()# Read
        if ret==False: break

        # Track
        frame_tracked = model.track(
            frame, persist=True, verbose=False)[0].plot()

        # Grid
        #utility.draw_grid(w, h, frame_tracked, (255, 255, 255), 1)
        cap_to.write(frame_tracked)


if __name__ == "__main__":
    main()