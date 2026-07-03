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
    start_prediction("../assets/sample_20.mp4")


def start_prediction(path_file):
    print("start_prediction:", path_file)

    path = Path(path_file)
    path_from = path
    path_to   = path.name
    path_comp = Path(f"{path.stem}_comp{path.suffix}")
    
    # Video(From)
    cap_from   = cv2.VideoCapture(path_from)
    w          = int(cap_from.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
    h          = int(cap_from.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
    count      = int(cap_from.get(cv2.CAP_PROP_FRAME_COUNT))# Count
    fps        = int(cap_from.get(cv2.CAP_PROP_FPS))# Fps
    resolution = (w, h)
    print("Video W:%d H:%d COUNT:%d FPS:%d" % (w, h, count, fps))

    # Video(To)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    cap_to = cv2.VideoWriter(
        path_to, fourcc, fps, resolution)

    # Model
    model = YOLO("yolo26n.pt")

    # Render
    for n in range(count):
        ret, frame = cap_from.read()# Read
        if ret==False: break

        # Track
        frame_tracked = model.track(
            frame, persist=True, verbose=False)[0].plot()

        # Grid
        utility.draw_grid(w, h, frame_tracked, (255, 255, 255), 1)
        cap_to.write(frame_tracked)

    # Release
    cap_from.release()
    cap_to.release()
    
    # Audio
    #utility.write_audio(path_from, path_to, path_comp)


if __name__ == "__main__":
    main()