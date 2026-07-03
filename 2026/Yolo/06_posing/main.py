# coding: utf-8

"""
1, Install
    $ python3 -m pip install ultralytics
"""

import cv2, os
from moviepy import VideoFileClip, AudioFileClip, AudioArrayClip
from pathlib import Path
from PIL import Image
from ultralytics import YOLO, solutions

def main():
    """ Main """
    print("main")

    # Prediction
    start_prediction(
        "yolo26n-pose.pt", 
        path_file="../assets/sample_02.mp4")


def start_prediction(path_model, path_file):
    print("start_prediction:", path_model, path_file)
    
    # Model
    # yolo11n < yolo11s < yolo11m ...
    model = YOLO(path_model)

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

    # Render
    for n in range(count):
        ret, frame = cap_from.read()# Read
        if ret==False: break

        # Track
        frame_tracked = model.track(
            frame, persist=True, verbose=False)[0].plot()
        cap_to.write(frame_tracked)

    # Release
    cap_from.release()
    cap_to.release()
    
    # Audio
    write_audio(path_from, path_to, path_comp)


def draw_grid(w, h, frame, l_color, l_width):
    g_size = int(w / 20)
    rows = int(h / g_size)
    cols = int(w / g_size)
    for r in range(1, rows):
        y = r * g_size
        cv2.line(frame, (0, y), (w, y), l_color, l_width)
        for c in range(1, cols):
            x = c * g_size
            cv2.line(frame, (x, 0), (x, h), l_color, l_width)


def write_audio(path_from, path_to, path_comp):
    print("write_audio!!")
    clip_from = VideoFileClip(path_from).subclipped() # From
    clip_to = VideoFileClip(path_to).subclipped() # To
    clip_comp = clip_to.with_audio(clip_from.audio) # Comp
    clip_comp.write_videofile(path_comp, codec="libx264", audio_codec="aac")


if __name__ == "__main__":
    main()