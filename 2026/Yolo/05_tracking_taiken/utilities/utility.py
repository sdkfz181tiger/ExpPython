# coding: utf-8

import cv2, os
from moviepy import VideoFileClip, AudioFileClip, AudioArrayClip
from pathlib import Path
from PIL import Image
from ultralytics import YOLO, solutions


def draw_grid(w, h, frame, l_color, l_width,
    f_scale=1.0, f_color=(255, 255, 255), f_thickness=4):
    g_size = int(w / 20)
    rows = int(h / g_size)
    cols = int(w / g_size)
    for r in range(1, rows):
        y = r * g_size
        cv2.line(frame, (0, y), (w, y), l_color, l_width)
        cv2.putText(frame, str(y), (10, y), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            f_scale, f_color, f_thickness)
    for c in range(1, cols):
        x = c * g_size
        cv2.line(frame, (x, 0), (x, h), l_color, l_width)
        cv2.putText(frame, str(x), (x, h-10), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            f_scale, f_color, f_thickness)


def write_audio(path_from, path_to, path_comp):
    print("write_audio")
    clip_from = VideoFileClip(path_from).subclipped()
    clip_to = VideoFileClip(path_to).subclipped()
    clip_comp = clip_to.with_audio(clip_from.audio)
    clip_comp.write_videofile(path_comp, codec="libx264", audio_codec="aac")


def my_decorator(func):

    def wrapper(path_model, path_file):

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

        func(path_model, w, h, count, cap_from, cap_to)

        # Release
        cap_from.release()
        cap_to.release()

        # Audio
        #utility.write_audio(path_from, path_to, path_comp)
    return wrapper