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

    # Tracking
    #start_tracking("yolo26n-obb.pt", "../assets/sample_13.mp4")

    # Tracking(横断歩道) plotの引数調整
    start_tracking("yolo26n.pt", "../assets/crossing_01.mp4") # 横断歩道

    # Tracking(Parking) plotの引数調整
    # classes=[9, 10]
    #start_tracking("yolo26n-obb.pt", "../assets/parking_02.mp4") # Parking

    # Segmentation
    #start_tracking("yolo26n-seg.pt", "../assets/cats_07.mp4") # Cats

    # Posing
    #start_tracking("yolo26n-pose.pt", "../assets/chaplin_01.mp4") # Chaplin

    # Counting
    #start_counting("yolo26n.pt", "../assets/sample_11.mp4") # Traffics


@utility.my_decorator
def start_tracking(path_model, w, h, count, cap_from, cap_to):
    print("start_tracking:", path_model)

    # Model
    model = YOLO(path_model)

    # Render
    for n in range(count):
        ret, frame = cap_from.read()# Read
        if ret==False: break

        # Track
        frame_tracked = model.track(
            frame, 
            persist=True, 
            verbose=False)[0].plot(
            labels=False, 
            conf=False)

        # Grid
        #utility.draw_grid(w, h, frame_tracked, (255, 255, 255), 1)
        cap_to.write(frame_tracked)


@utility.my_decorator
def start_counting(path_model, w, h, count, cap_from, cap_to):
    print("start_counting:", path_model)

    # Model
    counter = solutions.ObjectCounter(
        model=path_model, show=False, 
        region=[(0, 600), (1080, 600)],
        classes=[2, 3, 5, 7],
        line_width=4)

    # Render
    for n in range(count):
        ret, frame = cap_from.read()# Read
        if ret==False: break

        # Counter
        frame_counter = counter(frame).plot_im

        # Grid
        #utility.draw_grid(w, h, frame_counter, (255, 255, 255), 1)
        cap_to.write(frame_counter)


if __name__ == "__main__":
    main()