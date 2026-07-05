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
    #start_tracking("yolo26n.pt", "../assets/cats_05.mp4")

    # Segmentation
    start_tracking("yolo26n-seg.pt", "../assets/sample_07.mp4")

    # Posing
    #start_tracking("yolo26n-pose.pt", "../assets/chaplin_01.mp4")

    # Counting
    #start_counting("yolo26n.pt", "../assets/sample_11.mp4")


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
            frame, persist=True, verbose=False)[0].plot()

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