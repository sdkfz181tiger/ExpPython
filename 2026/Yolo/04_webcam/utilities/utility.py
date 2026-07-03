# coding: utf-8

import cv2, os
from moviepy import VideoFileClip, AudioFileClip, AudioArrayClip
from pathlib import Path
from PIL import Image
from ultralytics import YOLO, solutions


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
    print("write_audio")
    clip_from = VideoFileClip(path_from).subclipped()
    clip_to = VideoFileClip(path_to).subclipped()
    clip_comp = clip_to.with_audio(clip_from.audio)
    clip_comp.write_videofile(path_comp, codec="libx264", audio_codec="aac")